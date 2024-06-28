from django.http import request, response
from django.shortcuts import render
import pickle


# def hrdetails():
#     result=None
#     if request.method=="POST":
#         num=int(request.POST.get('num')) 
#         num1=int(request.POST.get('num1'))
#         num2=int(request.POST.get('num2')) 
#         num3=int(request.POST.get('num3')) 
#         num4=int(request.POST.get('num4')) 
#         num5=int(request.POST.get('num5')) 
#         num6=int(request.POST.get('num6')) 
#         num7=int(request.POST.get('num7')) 
#         num8=int(request.POST.get('num8')) 
#         model=pickle.load(open('E:/Django_apps/HR_department/model.pkl', 'rb'))
#         condition=model.predict([[num,num1,num2,num3,num4,num5,num6,num7,num8]])

#         if condition==0:
#             result="Employee organization not left"
#         else:
#             result="Employee organization left"

#     return render(request,'index.html',{'result': result})    
    


        
from django.shortcuts import render
import pickle

def hrdetails(request):
    result = "None"
    if request.method == "POST":
        try:
            num = float(request.POST.get('num', 0))
            num1 = float(request.POST.get('num1', 0))
            num2 = int(request.POST.get('num2', 0))
            num3 = int(request.POST.get('num3', 0))
            num4 = int(request.POST.get('num4', 0))
            num5 = int(request.POST.get('num5', 0))
            num6 = int(request.POST.get('num6', 0))
            num7 = int(request.POST.get('num7', 0))
            num8 = int(request.POST.get('num8', 0))
            
            model = pickle.load(open('model.pkl', 'rb'))
            condition = model.predict([[num, num1, num2, num3, num4, num5, num6, num7, num8]])

            if condition == 0:
                result = "Employee has not left the organization"
            else:
                result = "Employee has left the organization"
        except (TypeError, ValueError) as e:
            result = "Invalid input: please ensure all fields are filled correctly."
    
    return render(request,'index.html',{'result': result})    
