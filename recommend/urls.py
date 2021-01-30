from django.urls import path

from . import views

app_name = 'recommend'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/<str:kind>/', views.resultJob, name='result'),
    path('result1/', views.fir_result, name='result1'),
    path('infojob/', views.wanna_job, name='infojob'),
    path('result2/', views.sec_result, name='result2')

]
