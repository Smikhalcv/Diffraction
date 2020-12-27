from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AboutCompany, DirectionOfActivity
from .serializers import AboutCompanySerializer, DirectionOfActivity
# Create your views here.

class AboutCompanyView(APIView):
    """Отображает информацию о компании"""
    def get(self, request):
        information = AboutCompany.objects.get(id=1)
        directions = information.directions.all()

        information_serializer = AboutCompanySerializer(information)
        directions_serializer = DirectionOfActivity(directions, many=True)
        return Response({
            'about_company': information_serializer.data,
            'directions': directions_serializer.data
        })