from random import randint

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import  Http404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from customer.models import Customer
from vashaacademy.utils import make_payment
from .forms import ResultForm
from .models import Course, Result, Exam, Enrollment
from .serializer import QuestionSerializer
import requests

# Create your views here.
@login_required(login_url="/customer/login")
def course(request, id, *args, **kwargs):
    course_ins = Course.objects.filter(id=id).first()
    title = course_ins.title
    course_res = { }
    print(Result.objects.filter(exam = course_ins.exams.all().first(), customer = request.user).first())
    for exam in course_ins.exams.all():
        res = Result.objects.filter(exam = exam, customer = request.user).first()
        course_res[exam] =  res.score if res else 0
    print(course_res)

    return render(request, "course_details.html",
          context = { 'title': title, 'course_res': course_res.items() }
        )

@login_required(login_url="/customer/login")
def exam(request, id, *args, **kwargs):
    exam = get_object_or_404(Exam, id=id)
    result = Result.objects.filter(exam = exam, customer = request.user).first()
    form = ResultForm(request.POST or None, result)
    if form.is_valid():
        request.session['finished'] = True
        ins = form.save()
        ins.save()
        # print(ins)
        # print(ins.score)
        return redirect("course:result", id=ins.id)
    else:
        exam = get_object_or_404(Exam, id=id)
        questions = QuestionSerializer(exam.questions, many=True).data
        # print(questions)
        return render(request, "exam.html",
                      context = {
                                 'title': exam.title,
                                 'data': {
                                            'id': exam.id,
                                            'duration': exam.duration,
                                            'questions': questions
                                         }
                      }
        )

@login_required(login_url="/customer/login")
def result(request, id,  *args, **kwargs):
    finished = request.session.get('finished')
    if not finished:
        return Http404()
    request.session['finished'] = None
    result = get_object_or_404(Result, id=id)
    print(result.customer == request.user)
    return render(request, "result.html", {'score': result.score })


@login_required(login_url="/customer/login")
def initiate_payment(request, course_id):
    print(course_id)
    course = Course.objects.filter(id=course_id).first()
    price = course.price if not course.discount else int(course.price*(1-course.discount/100))
    user_id = request.GET.get("user_id")
    # if request.method == "POST":
    tran_id = randint(1,99999999999999999999)
    enrollment = Enrollment.objects.filter(tran_id = tran_id).first()
    while enrollment is not None:
        tran_id = randint(1, 99999999999999999999)
        enrollment = Enrollment.objects.filter(tran_id=tran_id)
    return redirect(make_payment(user_id=request.user.id, course_id=course_id, tran_id=tran_id, amount=price))


@csrf_exempt
def payment_success(request, user_id, course_id):
    if request.method == "POST":
        course = Course.objects.filter(id=course_id).first()
        customer = Customer.objects.filter(id=user_id).first()
        tran_id = request.POST.get('mer_txnid')
        amount = int(float(request.POST.get('amount')))
        # enrolled = Enrollment.objects.filter(course=course, customer=customer)
        # if enrolled is not None:
        #     enrolled.delete()
        # Enrollment.objects.create(course=course, customer=customer, amount=amount, tran_id=tran_id)
        return render(request, "payment_success.html", {'course': course})
    return Http404()


def payment_failed(request):
    return render(request, "payment_failed.html")




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
