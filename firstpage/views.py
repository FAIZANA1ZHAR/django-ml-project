from django.shortcuts import render
import pandas as pd
from pymongo import MongoClient
from .models import TableForm 
from django.http import JsonResponse 
from django.http import HttpResponse
import json
from django.forms.models import model_to_dict
import numpy as np 
from django.core import serializers

# from django.utils import simplejson


client = MongoClient('localhost', 27017)
db = client['mpgDataBase']
collectionD = db['mpgTable']


import joblib

reloadModel = joblib.load('./models/ML_model.pkl')
number_of_rows = 0
prediction_score = 0 
# Create your views here.

def index(request):
    context = {'a':'HelloWorld'}

    
    
    return render (request, 'index2.html',context)
    
def predictMPG(request):
    if request.method == 'POST':
        temp2={}
        temp2['Account_length'] =  request.POST.get('Accountlength')
        temp2['Area_code'] =  request.POST.get('Areacode')
        temp2['Number_vmail_messages'] = request.POST.get('Numbervmailmessages')
        temp2['Total_day_minutes']=   request.POST.get('Totaldayminutes')
        temp2['Total_day_calls'] =  request.POST.get('Totaldaycalls')
        temp2['Total_day_charge'] =     request.POST.get('Totaldaycharge')
        temp2['Total_eve_minutes'] =   request.POST.get('Totaleveminutes')
        temp2['Total_eve_calls'] =   request.POST.get('Totalevecalls')
        temp2['Total_eve_charge'] =      request.POST.get('Totalevecharge')
        temp2['Total_night_minutes'] =    request.POST.get('Totalnightminutes')
        temp2['Total_night_calls'] =  request.POST.get('Totalnightcalls')
        temp2['Total_night_charge'] = request.POST.get('Totalnightcharge')
        temp2['Customer_service_calls'] =   request.POST.get('Customerservicecalls')
        temp2['Voice_mail_plan'] =    request.POST.get('Voicemailplan')
        temp2['International_plan'] =   request.POST.get('Internationalplan')
        temp2['international_voice_call_usage'] =    request.POST.get('internationalvoicecallusage')
    
    
    testData=pd.DataFrame({'x': temp2}).transpose()
    scoreval = reloadModel.predict(testData)[0]    
    print("prediction is done here")
    print(scoreval)
    if scoreval == True :
        newscoreval =1 
    else:
        newscoreval = 10    
    global prediction_score
    prediction_score =  newscoreval 
    context={'newscoreval':newscoreval,'temp2':temp2}
    
    return HttpResponse(prediction_score, content_type='text/plain')



def viewDatabase(request):
    countOfrow=collectionD.find().count()
    context={'countOfrow':countOfrow}
    return render(request,'viewDB.html',context)


def updateDataBase(request):   

    temp={}
    temp['Account length'] = request.POST.get('Accountlength')
    temp['Area code'] = request.POST.get('Areacode')
    temp['Number vmail messages'] = request.POST.get('Numbervmailmessages')
    temp['Total day minutes']=   request.POST.get('Totaldayminutes')
    temp['Total day calls'] =  request.POST.get('Totaldaycalls')
    temp['Total day charge'] =     request.POST.get('Totaldaycharge')
    temp['Total eve minutes'] =   request.POST.get('Totaleveminutes')
    temp['Total eve calls'] =   request.POST.get('Totalevecalls')
    temp['Total eve charge'] =      request.POST.get('Totalevecharge')
    temp['Total night minutes'] =    request.POST.get('Totalnightminutes')
    temp['Total night calls'] =  request.POST.get('Totalnightcalls')
    temp['Total night charge'] = request.POST.get('Totalnightcharge')
    temp['Customer service calls'] =   request.POST.get('Customerservicecalls')
    temp['Voice mail plan'] =    request.POST.get('Voicemailplan')
    temp['International plan'] =   request.POST.get('Internationalplan')
    temp['international voice call usage'] =    request.POST.get('internationalvoicecallusage')
    temp['mpg']=request.POST.get('mpgVal')
    collectionD.insert_one(temp)
    countOfrow=collectionD.find().count()
     
    global number_of_rows
    number_of_rows =  countOfrow 
    print (number_of_rows)

    
    context={'countOfrow':countOfrow}
    return render(request,'viewDB.html',context)





def sentdata(request):
    data="hi i am here"
    temp = request.POST.get('Datareturn',None)
    print(temp)
    return HttpResponse(temp, content_type='text/plain')






def tableCrud(request):
    # temp2 = {}
    # temp2['Account_length'] = 5
    # temp2['Area_code'] =2
    # temp2['Number_vmail_messages'] = 3
    # temp2['Total_day_minutes']=  1
    # temp2['Total_day_calls'] =  1
    # temp4 = serializers.serialize("json", temp2)    
    # return JsonResponse(temp4 , safe=False)
    if request.method == "POST":

        temp2={}
        temp2['Account_length'] =   request.POST.get('Accountlength')
        temp2['Area_code'] = request.POST.get('Areacode')
        temp2['Number_vmail_messages'] = request.POST.get('Numbervmailmessages')
        temp2['Total_day_minutes']=   request.POST.get('Totaldayminutes')
        temp2['Total_day_calls'] =  request.POST.get('Totaldaycalls')
        temp2['Total_day_charge'] =     request.POST.get('Totaldaycharge')
        temp2['Total_eve_minutes'] =    request.POST.get('Totaleveminutes')
        temp2['Total_eve_calls'] =   request.POST.get('Totalevecalls')
        temp2['Total_eve_charge'] =     request.POST.get('Totalevecharge')
        temp2['Total_night_minutes'] =  request.POST.get('Totaleveminutes')
        temp2['Total_night_calls'] =  request.POST.get('Totalnightcalls')
        temp2['Total_night_charge'] = request.POST.get('Totalnightcharge')
        temp2['Customer_service_calls'] =  request.POST.get('Customerservicecalls')
        temp2['Voice_mail_plan'] =    request.POST.get('Voicemailplan')
        temp2['International_plan'] =  request.POST.get('Internationalplan')
        temp2['international_voice_call_usage'] =    request.POST.get('internationalvoicecallusage')
        print(temp2['international_voice_call_usage'])
       
        testData=pd.DataFrame({'x': temp2}).transpose()
        scoreval = reloadModel.predict(testData)[0]    
        print (scoreval)
        if scoreval == True :
            newscoreval =1
        else:
            newscoreval = 10 

           
        temp3={}
        temp3['Account_length'] =   request.POST.get('Accountlength')
        temp3['Area_code'] = request.POST.get('Areacode')
        temp3['Number_vmail_messages'] = request.POST.get('Numbervmailmessages')
        temp3['Total_day_minutes']=   request.POST.get('Totaldayminutes')
        temp3['Total_day_calls'] =  request.POST.get('Totaldaycalls')
        temp3['Total_day_charge'] =     request.POST.get('Totaldaycharge')
        temp3['Total_eve_minutes'] =    request.POST.get('Totaleveminutes')
        temp3['Total_eve_calls'] =   request.POST.get('Totalevecalls')
        temp3['Total_eve_charge'] =     request.POST.get('Totalevecharge')
        temp3['Total_night_minutes'] =  request.POST.get('Totaleveminutes')
        temp3['Total_night_calls'] =  request.POST.get('Totalnightcalls')
        temp3['Total_night_charge'] = request.POST.get('Totalnightcharge')
        temp3['Customer_service_calls'] =  request.POST.get('Customerservicecalls')
        temp3['Voice_mail_plan'] =    request.POST.get('Voicemailplan')
        temp3['International_plan'] =  request.POST.get('Internationalplan')
        temp3['international_voice_call_usage'] =    request.POST.get('internationalvoicecallusage')
        temp3['scoreval'] =    newscoreval
        temp4 = serializers.serialize("json", temp3)

    
        return JsonResponse(temp4 , safe=False)  





    
def update1(request):   

    temp={}
    temp['Account length'] = 4
    temp['Area code'] =3
    temp['Number vmail messages'] = 3
    temp['Total day minutes']=   2
    temp['Total day calls'] =  1
    temp =dict(temp)
    
    temp4 = serializers.serialize("json", temp)    
    return JsonResponse(temp , safe=False)
