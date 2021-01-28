from django.shortcuts import render
import pandas as pd
import os
# Create your views here.
def index (request):
    return render(request,'index.html')
def fir_result(request):
    return render(request,'result1.html')
def wanna_job(request):
    return render(request,'infojob.html')
def sec_result(requese):
    return render(requese,'result2.html')
def readCsv(address):
    df=pd.read_csv(address)
    return df
# address 파라미터 적어줄때  => r'절대주소'