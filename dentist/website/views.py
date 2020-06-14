from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'index.html', {})
def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send an email
        send_mail(
            'Message From'+ message_name, #subject
            message, #message
            message_email, #from email
            ['1@gmail.com','2@gmail.com'], #To email
        )

        return render(request, 'contact.html', {'message_name':message_name})

    else:
        return render(request,'contact.html', {})
def pricing(request):
    return render(request,'pricing.html', {})
def about(request):
    return render(request,'about.html', {})
def service(request):
    return render(request,'service.html', {})

def appointment(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_scheldule = request.POST['your-scheldule']
        your_time = request.POST['your-time']
        your_message = request.POST['your-message']

        # #send an email
        # send_mail(
        #     'Message From'+ message_name, #subject
        #     message, #message
        #     message_email, #from email
        #     ['1@gmail.com','2@gmail.com'], #To email
        # )

        return render(request, 'appointment.html', {'your_scheldule': your_scheldule})

    else:
        return render(request,'index.html', {})