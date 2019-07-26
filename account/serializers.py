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
        fields = ('id','first_name','last_name','email','password','date_of_birth','address','state', 'gender', 'phone_number','profile_pic')


class ProfileSerializer(serializers.ModelSerializer):
    # userorganizations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id',
                'first_name',
                'last_name',
                'email',
                'password',
                'date_of_birth',
                'address',
                'state', 
                'gender', 
                'phone_number',
                'profile_pic',
                # 'createdorgs',
                # 'createdgroups',
                # 'userorganizations',
                # 'usergroups',
                # 'createdprocesses',
                # 'createdstage',
                # 'createdtask',
                # 'userforms',
                # 'userdocuments',
                # 'tasks_to_user',
                # 'userformresponse')
        )

    def update(self, instance, validated_data):       
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.email = validated_data.get('email',instance.email)
        instance.password = validated_data.get('password',instance.password)
        instance.date_of_birth = validated_data.get('date_of_birth',instance.date_of_birth)
        instance.address = validated_data.get('address',instance.address)
        instance.state = validated_data.get('state',instance.state)
        instance.gender = validated_data.get('gender',instance.gender)
        instance.phone_number = validated_data.get('phone_number',instance.phone_number)
        instance.profile_pic = validated_data.get('profile_pic',instance.profile_pic)
        return instance
            
        
