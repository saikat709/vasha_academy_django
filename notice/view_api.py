from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from notice.models import Notice, FAQ, PdfBooks
from notice.serializers import NoticeSerializer, FaqSerializer, PdfSerializer


class NoticeViewSets(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class FaqViewSets(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = FAQ.objects.all()
    serializer_class = FaqSerializer

class PdfViewSets(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PdfBooks.objects.all()
    serializer_class = PdfSerializer
