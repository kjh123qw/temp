from django.shortcuts import render
import pandas as pd
from recommend.models import test
import os

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

test_df=readCsv(r'C:\Users\네리\Desktop\sba_re\4조\job_data_list_final.csv')
print(test_df.columns)
#col=index,jobId,company,title,job,skill,region,experience,intro
#task,require,prefer,jobUrl
test_df=test_df.fillna('')

print(type(test_df['jobId'][0]))

#test => titleId,company,title,job,skill
def create():
    for i in range(len(test_df)):
        test.objects.create(titleId=test_df['jobId'][i], company=test_df['company'][i], title=test_df['title'][i], job=test_df['job'][i], skill=test_df['skill'][i])
print(len(test_df))
#model.objects.all()