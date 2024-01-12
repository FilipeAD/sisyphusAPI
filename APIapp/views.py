from rest_framework.views import APIView

import schedule
import time

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from .serializers import UserSerializer, ExerciseSerializer
from .models import UserProfile, Exercises
from rest_framework.decorators import api_view, APIView
from django.shortcuts import get_object_or_404


# Create your views here.


class UserListCreateView(APIView):
    '''
        Create and List Users
    '''

    serializer_class = UserSerializer

    def get(self, request:Request, *args, **kwargs):

        user = UserProfile.objects.all()
        serializer = self.serializer_class(instance=user, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK);

    def post(self,request:Request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message":"User Created",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED);
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UserRetrieveUpdateDeleteView(APIView):

    serializer_class = UserSerializer

    def get(self,request:Request, pk:int):

        user = get_object_or_404(UserProfile, id=pk)
        serializer = self.serializer_class(instance=user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request:Request, pk:int):

        user = get_object_or_404(UserProfile, id=pk)
        serializer = self.serializer_class(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"User Updated",
                "data": serializer.data
            }
            
            return Response(response, status=status.HTTP_200_OK);
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request:Request,pk:int):

        user = get_object_or_404(UserProfile, id=pk)
        user.delete()

        return Response("Product deleted", status=status.HTTP_204_NO_CONTENT);


class ExercisesListCreateView(APIView):
    '''
        Create and List Exercises
    '''

    serializer_class = ExerciseSerializer

    def get(self, request:Request, *args, **kwargs):

        exercise = Exercises.objects.all()
        serializer = self.serializer_class(instance=exercise, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK);

    def post(self,request:Request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message":"Exercise Created",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED);
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Calories(APIView):
    
    def get(self, request:Request, height:int, weight:int, age:int, sex:str, activityLevel:str):

        if sex == 'male':
        
            BMR = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)

        elif sex == 'female':
        
            BMR = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)

        
        match activityLevel:
            case 'Sedentary':
                multiplyer = 1.2
            case 'Lightly active':
                multiplyer = 1.375
            case 'Moderately active':
                multiplyer = 1.55
            case 'Active':
                multiplyer = 1.725
            case 'Very active':
                multiplyer = 1.9

        result = BMR * multiplyer

        return result
    
    def put(self,request:Request, *args, **kwargs):
        pass

    
        



        



