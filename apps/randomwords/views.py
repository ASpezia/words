from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    if "count" in request.session:
        request.session["count"] +=1
    if "count" not in request.session:
         request.session["count"] =1
    context= {
    "randomwords": get_random_string(length=20),}
    return render(request, "randomwords/index.html", context)
    
def reset(request):
    del request.session['count']
    return redirect ("/")
