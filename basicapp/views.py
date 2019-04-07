from django.shortcuts import render
from basicapp.forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def base(request):
    return render(request,'basicapp/base.html')
def index(request):
     return render(request,'basicapp/index.html')
def register(request):
      registered = False
      if request.method =='POST':
           user_form = UserForm(data=request.POST)
           if user_form.is_valid():
               user =user_form.save()
               user.set_password(user.password)
               user.save()
               registered =True
           else :
            print("user_form:errors")
      else :
           user_form = UserForm()
      return render(request,'basicapp/register.html',
                       {'user_form':user_form,'registered':registered})
def quiz(request):
     return render(request,'basicapp/quiz.html')
