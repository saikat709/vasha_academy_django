from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import  Http404
from .forms import ResultForm
from .models import Course, Result, Exam
from .serializer import QuestionSerializer

# Create your views here.
@login_required(login_url="/customer/login")
def course(request, id, *args, **kwargs):
    course_ins = Course.objects.filter(id=id).first()
    title = course_ins.title
    course_res = {}

    for exam in course_ins.exams.all():
        res = Result.objects.filter(exam = exam, customer = request.user).first()
        course_res[exam] =  res.score if res else 0

    return render(request, "course_details.html",
          context = { 'title': title, 'course_res': course_res.items() }
        )

@login_required(login_url="/customer/login")
def exam(request, id, *args, **kwargs):
    form = ResultForm(request.POST or None)
    if form.is_valid():
        request.session['finished'] = True
        ins = form.save()
        return redirect("course:result", id=ins.id)
    else:
        exam = get_object_or_404(Exam, id=id)
        questions = QuestionSerializer(exam.questions, many=True).data
        return render(request, "exam.html",
                      context = {'title': exam.title,
                                 'data': { 'id': exam.id,
                                        'duration': exam.duration,
                                        'questions': questions }
                      }
        )

@login_required(login_url="/customer/login")
def result(request,id,  *args, **kwargs):
    finished = request.session.get('finished')
    if not finished:
        return Http404()
    request.session['finished'] = None
    result = get_object_or_404(Result, id=id)
    return render(request, "result.html", {'score': result.score })



# class AttendenceViewset(viewsets.ModelViewSet):
#     queryset=Attendcourse.objects.all()
#     #serializer_class=Attendserializer
#
#     @action(detail=True, methods=['post'],permission_classes=[IsAuthenticated])
#     def start(self,request,pk):
#            user_instance=request.user
#            course_instance=get_object_or_404(Coursetype,id=pk)
#            attend,created=Attendcourse.objects.update_or_create(
#           user=user_instance,
#           courses=course_instance,
#           defaults={'start_time': timezone.now()}
#     )
#            return Response ("Your exam starts")
#
#     @action(detail=True, methods=['post'],permission_classes=[IsAuthenticated])
#     def submit(self,request,pk):
#         user_instance=request.user
#         course_instance=get_object_or_404(Coursetype,id=pk)
#         course_question=course_instance.question.all()
#         user_answer=UserAnswer.objects.filter(user=user_instance,question__in=course_question)
#         i=0
#         for q in user_answer:
#                 i=i+q.get_result
#         Attendcourse.objects.update_or_create(
#
#           user=user_instance,
#           course=course_instance,
#           defaults={'total_number': i}
#           )
#
#         return Response ('your time has over')
#
#
#     @background(schedule=30)
#     def check_time_over(self,request,pk):
#          present_time = timezone.now()
#          examinee=request.user
#          course_instance=get_object_or_404(Coursetype,id=pk)
#          attendcourse_instance=get_object_or_404(Attendcourse,user=examinee,course=course_instance)
#          end_time=course_instance.duration+attendcourse_instance.start_time
#          if present_time>end_time:
#              return self.submit(request, pk)
#          return None
