from django.urls import path

from diffraction.views import AboutCompanyView

urlpatterns = [
    path('about_company/', AboutCompanyView.as_view()),
]