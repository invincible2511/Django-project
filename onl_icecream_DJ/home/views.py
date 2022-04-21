from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable":"LOL"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This is Homepage")

def about(request):
   # return HttpResponse("This is about page.")
   return render(request, 'about.html')

def services(request):
   # return HttpResponse("This is services page.")
   return render(request, 'services.html')

def contact(request):
   # return HttpResponse("This is contact page.")
   if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      desc = request.POST.get('desc')
     
      if len(name)<2 or len(email)<5 or len(phone)<10 or len(desc)<2:
         messages.error(request, "Please fill the form correctly.") 
      else:
         contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
         contact.save()
         messages.success(request, 'Your message has been sent!')
   return render(request, 'contact.html')

