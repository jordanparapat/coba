from django.shortcuts import render
import requests

def button(request):

   return render(request,'home.html')
      
def output(request):
    data=request.get("https://reqres.in/api/users")
    print(data.text)
    data=data.text
    return render(request,'home.html',{'data':data})