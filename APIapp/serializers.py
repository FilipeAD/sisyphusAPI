from rest_framework import serializers
from .models import UserProfile, Exercises
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CalorieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        field = 'calorieIntake'

class CalorieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        field = 'calorieIntake'


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercises
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'
        #write only
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # Hash password so it cannot be seen normaly
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        
        token['username'] = user.username
        token['id'] = user.id
        token['email'] = user.email
        token['password'] = user.password
        
        
       

        return token
    