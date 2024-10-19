from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from customer.models import Customer, LoginInfo
from customer.serializers import CustomerSerializer
from vashaacademy.utils import send_otp_code


class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(methods=["GET",], detail=False )
    def exists(self, request):
        exists = False
        number = self.request.query_params.get('number').strip()
        number = "+"+number if not number.startswith("+") else number
        print(number)
        user = Customer.objects.filter(number=number).first()
        print(user)
        if user is not None:
           exists = True
        return Response(
            data= exists,
            status=status.HTTP_200_OK
        )

    @action(methods=["GET", ], detail=False, url_path="getbynumber/(?P<number>[^/.]+)")
    def getbynumber(self, request, number):
        # number = "+"+number if not number.startswith("+") else number
        print(number)
        user = Customer.objects.filter(number=number).first()
        user = CustomerSerializer(user).data
        return Response(
            data=user, status=status.HTTP_200_OK
        )

    @action(methods=["GET"], detail=False)
    def authenticate(self, request):
        token = self.request.query_params.get('token')
        info = LoginInfo.objects.filter(token=token).first()
        customer = CustomerSerializer(info.user)
        return Response(
            data = customer.data,
            status = status.HTTP_200_OK
        )

    @action(methods=["POST"], detail=False)
    def sendotp(self, request):
        otp = send_otp_code()
        return Response(
            data = otp,
            status = status.HTTP_200_OK,
        )

    @action(detail=False,methods=['POST'])
    def login(self, request):
        number = self.request.data.get('number')
        password = self.request.data.get('password')
        user = Customer.objects.filter(number = number).first()
        print(user)
        if user is not None and authenticate(username=number, password=password):
            info = LoginInfo(user= user)
            info.save()
            return Response(
                data = info.token,
                status = status.HTTP_200_OK
            )
        return Response(
            data = "Wrong password or Number",
            status = status.HTTP_406_NOT_ACCEPTABLE
        )


    @action(detail=False, methods=['Post'])
    def logout(self, request):
        token = self.request.query_params.get('token')
        info =  LoginInfo.objects.filter(token=token).first()
        print(info)
        if info:
            info.delete()
            info.save()
            print(info)

        return Response(
            data = 'Successfully logged out.',
            status= status.HTTP_200_OK
        )


        # @action(detail=False, methods=['Post'])
        # def add(self, request):
        #     serializer = self.get_serializer(data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(
        #             data={'message': 'Your registration is completed'},
        #             status=status.HTTP_201_CREATED
        #         )
        #     return Response(
        #         data={'error': 'Registration is not get well,Try again'},
        #         status=status.HTTP_400_BAD_REQUEST)
        #
