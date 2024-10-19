from django.db.models.expressions import result
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response

from course.models import Course, Exam, Result
from course.serializer import CourseSerializer, ExamSerializer, ResultSerializer
from customer.models import Customer


class CourseViewSets(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ExamViewSets(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ResultViewSets(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    @action(methods=["GET", ], detail=False, url_path="getbynumber/(?P<customer_id>[^/.]+)")
    def getbycustomer(self, request, customer_id):
        customer = Customer.objects.filter(id=customer_id).first()
        results = Result.objects.filter(customer = customer)
        result = ResultSerializer(results, many=True).data
        print(result)
        return Response(
            data=result, status=status.HTTP_200_OK
        )

    @action(methods=["GET", ], detail=False, url_path="getbyexamandcustomer/(?P<customer_id>[^/.]+)/(?P<exam_id>[^/.]+)")
    def getbyexamandcustomer(self, request, customer_id=None, exam_id=None):
        customer = Customer.objects.filter(id=customer_id).first()
        exam = Exam.objects.filter(id=exam_id).first()
        result = Result.objects.filter(customer=customer, exam= exam).first()
        result = result if result is None else ResultSerializer(result, many=False).data
        print(result)
        return Response(
            data=result,
            status=status.HTTP_200_OK
        )