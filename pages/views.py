from django.shortcuts import render
# Create your views here.
from .models import Contact,About



def index(request):
    return render(request,'pages/index.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        c = Contact(name=name, email=email, message=message)
        c.save()

        return render(request,'pages/contact.html')



     




    return render(request,'pages/contact.html')



def about(request):

    details= About.objects.get(id=1)

    context = {
        'details' : details,
    }





    return render(request,'pages/about.html',context)