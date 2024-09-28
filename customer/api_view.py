from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from customer.models import Customer
from customer.serializers import ExamineeSerializer


class ExamViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = ExamineeSerializer

    @action(detail=False,methods=['Post'])
    def add(self,request):
     serializer=self.get_serializer(data=request.data)
     if serializer.is_valid():
         serializer.save()
         return Response (
            data={'message':'Your registration is completed'},
            status=status.HTTP_201_CREATED
         )
     return Response ({'error':'Registration is not get well,Try again'},status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False,methods=['Post'])
    def login(self,request):
       if request.method == 'POST':
        username=request.data.get('username')
        password=request.data.get('password')
        print(username,password)

        user=None

        if '@' in username:
            try:
                user=Customer.objects.get(email=username)
                print(user)
                if not user.check_password(password):
                  user = None
            except Customer.ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username,password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key,'user_id':user.id}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


    @api_view(['POST'])
    def logout(self,request):
          if request.method == 'POST':
               try:
                    request.user.auth_token.delete()
                    return Response(
                        {'message': 'Successfully logged out.'},
                        status=status.HTTP_200_OK)
               except:
                    return Response(
                        {'error': 'Logout process donot go well.'},
                        status=status.HTTP_200_OK)

