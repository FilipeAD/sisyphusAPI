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

    path('calories/<int:weigth>&<int:heigth>&<str:sex>&<str:activityLevel>&<int:age>/', views.Calories.as_view(), name='calculateCalories')

]