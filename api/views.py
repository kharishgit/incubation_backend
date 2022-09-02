from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from . models import RegisterCompany,Booking

# Create your views here.

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

import api
from .serializers import BookingSerializer, UserSerializer, UserSerializerWithToken,RegisterSerializer,UpdateBooking

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUser(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name = data['name'],
            username = data['email'],
            email = data['email'],
            password = make_password(data['password']),
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail':'User with this email is already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Registercompany(request):
    data = request.data

    register = RegisterCompany.objects.create(
        name = data['name'],
        address = data['address'],
        city = data['city'],
        email = data['email'],
        company_name = data['company_name'],
        describe_your_team_and_background = data['describe_your_team_and_background'],
        describe_your_company_and_product = data['describe_your_company_and_product'],
        what_is_unique_about_your_solution = data['what_is_unique_about_your_solution'],
        what_is_your_value_proposition_for_the_customer = data['what_is_your_value_proposition_for_the_customer'],
        who_are_your_competetitors_and_what_is_your_competative_advantage = data['who_are_your_competetitors_and_what_is_your_competative_advantage'],
        explain_your_revenue_model = data['explain_your_revenue_model'],
        what_is_the_potential_market_size_of_the_product = data['what_is_the_potential_market_size_of_the_product'],
        how_do_you_market = data['how_do_you_market']
    )
    serializer = RegisterSerializer(register, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def bookingslot(request):
    booking = Booking.objects.all()
    serializer = BookingSerializer(booking, many=True)
    return Response (serializer.data)

@api_view(['PUT'])
def updateBooking(request, id):
    update = Booking.objects.get(id=id)
    change = UpdateBooking(instance=update,data=request.data)
    if change.is_valid():
        change.save()
    else:
        print('dshdddddddddddd')
    return Response(change.data)
    
    


