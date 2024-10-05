from rest_framework import serializers

from notice.models import Notice, FAQ, PdfBooks


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['__all__']


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['__all__']

class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfBooks
        fields = ['__all__']