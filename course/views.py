from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Coursetype, Attendcourse, Course, Result


# Create your views here.
@login_required(login_url="/login")
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


@login_required(login_url="/login")
def exam(request, id, *args, **kwargs):
    title = "Title"
    questions = [1,1,1,1,1]
    return render(request, "exam.html",
                  context = {'title': title,
                             'data': {
                                'id': 91,
                                'questions': questions
                            }
                  }
    )




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
