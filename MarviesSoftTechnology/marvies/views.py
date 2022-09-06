from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def Index(request):
    if request.method=='POST':
        contact=ContactForm(request.POST)

        if contact.is_valid():
            contact.save()
    else:
        contact=ContactForm()     

    context={"contact":contact}   

    return render(request,"marvies/index.html",context)





    