from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
# Create your views here.
def contact_view(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")

        if not subject:
            subject = "Mavzu ko'rsatilmagan"

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request,"Sizning arizangiz muvaffaqiyatli jo'natildi!")

        return redirect('contact')
    return render(request,"contact.html")
