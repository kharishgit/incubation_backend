from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('userprofile/', views.getUserProfile, name='userprofile'),
    path('getuser/', views.getUser, name='getuser'),
    path('register/', views.registerUser, name='register'),
    path('registercompany/', views.Registercompany, name='Register'),
    path('booking/', views.bookingslot, name='booking'),
    path('update/<int:id>/', views.updateBooking, name='update')

]
