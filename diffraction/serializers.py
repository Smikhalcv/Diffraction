from rest_framework import serializers

class AboutCompanySerializer(serializers.Serializer):
    information = serializers.CharField()

class DirectionOfActivity(serializers.Serializer):
    direction = serializers.CharField(max_length=250)