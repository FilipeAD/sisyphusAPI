from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token-obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    path('user/', views.UserListCreateView.as_view(), name='user-list|create'),
    path('user/<int:pk>/' , views.UserRetrieveUpdateDeleteView.as_view(), name='user-Detail|Update|Delete'),

    path('exercises/' , views.ExercisesListCreateView.as_view(), name='exercises-list|create'),
    path('exercises/<str:type>/<str:muscle>/<str:equipment>/<str:difficulty>/', views.ExerciseFilter.as_view(), name='exercise-specify'),

    path('calculate-calories/<int:heigth>/<int:weigth>/<int:age>/<str:sex>/<str:activityLevel>/', views.calculate_calories, name='calculate-calories'),
    path('update-calories/<int:pk>/', views.update_calories, name='update-calories'),

    path('training-plans/', views.TrainingPlanCreateView.as_view(), name='training-plan-list-create'),
    path('training-plans/<str:user_name>/',views.TrainingPlanRetrieveUpdateDeletebyUserName.as_view(), name='training-plan-retrieve-update-delete'),

    

]