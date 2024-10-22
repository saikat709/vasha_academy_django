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
        username = self.request.query_params.get('username').strip()
        number = "+" + username if not username.startswith("+") else username
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
    def getbyusername(self, request, username):
        # number = "+"+number if not number.startswith("+") else number
        print(username)
        user = Customer.objects.filter(username=username).first()
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
    def sendotp(self, request, username, is_mail):
        otp = send_otp_code(sent_to=username, is_email=is_mail)
        return Response(
            data = otp,
            status = status.HTTP_200_OK,
        )

    @action(detail=False,methods=['POST'])
    def login(self, request):
        username = self.request.data.get('username')
        password = self.request.data.get('password')
        user = Customer.objects.filter(username = username).first()
        print(user)
        if user is not None and authenticate(username=username, password=password):
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
