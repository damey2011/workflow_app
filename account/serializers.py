from .models import User 
from django.core.validators import RegexValidator
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

class LoginSerializer(serializers.ModelSerializer):
    #This takes precedencer over the extra_kwargs
    email = serializers.EmailField(max_length=150, help_text = "Required. Enter a valid email address")
    class Meta:
        model = User
        fields = ('email','password')

class SignUpSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=150, help_text = "Required. Enter a valid email address",     
                        validators=[UniqueValidator(queryset=get_user_model().objects.all(), message="A user with that email already exists.")])
    password = serializers.CharField(max_length=150)
    
    class Meta:
        model = User
        fields = ('id','first_name','last_name','email','password','first_name', 'last_name', 'date_of_birth','address','state', 'gender', 'phone_number','profile_pic')


class ProfileSerializer(serializers.ModelSerializer):
    userorganizations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('id',
                'first_name',
                'last_name',
                'email',
                'password',
                'first_name', 
                'last_name', 
                'date_of_birth',
                'address',
                'state', 
                'gender', 
                'phone_number',
                'profile_pic',
                'createdorgs',
                'createdgroups',
                'userorganizations',
                'usergroups',
                'createdprocesses',
                'createdstage',
                'createdtask',
                'userforms',
                'userdocuments',
                'stages_to_user',
                'userformresponse')

    
        
