from rest_framework.views import APIView

import schedule
import time

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from .serializers import UserSerializer
from .models import UserProfile, Exercises
from rest_framework.decorators import api_view, APIView
from django.shortcuts import get_object_or_404


# Create your views here.

def fetchexerciseAPI():
    serializer_class = Exercises

    muscleGroup = [ 'abdominals', 
                    'abductors', 
                    'adductors', 
                    'biceps', 
                    'calves', 
                    'chest',
                    'forearms',
                    'glutes',
                    'hamstrings',
                    'lats',
                    'lower_back',
                    'middle_back',
                    'neck',
                    'quadriceps',
                    'traps',
                    'triceps'
                    ]
    
    for muscle in muscleGroup:
        offset = 10
        
        api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}&&offset={}'.format(muscle, offset)
    
        response = requests.get(api_url, headers={'X-Api-Key': 'b9jGthrmp3JZxgUsYKy4KA==6pyIKaRO50A5sMVx'})

        if response.status_code == requests.codes.ok:
            offset+=10
            
            serializer = serializer_class(data=response.data)

            if serializer.is_valid():
                serializer.save()

        else:
            print("Error:", response.status_code, response.text)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    return Response(status=status.HTTP_201_CREATED);

    schedule.every(10).seconds.do(job)
    schedule.every(10).minutes.do(job)
    schedule.every().hour.do(job)
    schedule.every().day.at("10:30").do(job)
    schedule.every(5).to(10).minutes.do(job)
    schedule.every().monday.do(job)
    schedule.every().wednesday.at("13:15").do(job)
    schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
    schedule.every().minute.at(":17").do(job)


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

    serializer_class = Exercises

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
        





    



