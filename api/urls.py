from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('get_stu/',views.StudentAPI.as_view()),
    path('get_stu/<str:id>/',views.StudentAPI.as_view()),
    path('add_stu/',views.StudentAPI.as_view()),
    path('del_stu/',views.StudentAPI.as_view()),
    path('patch_stu/',views.StudentAPI.as_view()),
]