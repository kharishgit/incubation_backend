from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from . models import RegisterCompany, Booking


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only = True)
    _id = serializers.SerializerMethodField(read_only = True)
    isAdmin = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only= True)
    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterCompany
        fields = [
            'name','address','city','email','company_name','describe_your_team_and_background','describe_your_company_and_product',
            'what_is_unique_about_your_solution','what_is_your_value_proposition_for_the_customer','explain_your_revenue_model',
            'what_is_the_potential_market_size_of_the_product','how_do_you_market'
        ]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields = ['time','date','section','status','company']

class UpdateBooking(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields = ['status','company']
        

 


