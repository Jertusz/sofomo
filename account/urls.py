# 3rd party
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path("register/", views.RegisterUser.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    # path("cars/", views.CarDetails.as_view()),
    # path("cars/<int:pk>/", views.DeleteCar.as_view()),
    # path("rate/", views.AddRate.as_view()),
    # path("popular/", views.PopularCars.as_view()),
]
