from django.shortcuts import render
import requests

def Home(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return render(request,"Home.html",{'data':response})