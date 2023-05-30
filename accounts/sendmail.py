from django.core.mail import send_mail as sm
from django.core.mail import EmailMessage, get_connection
from django.conf import settings


def send_mail(user, token):
    verification_link = f"http://127.0.0.0/api/account/verify_token/{token}"
    subject = "Email Verification"
    message = f"Please click the following link to verify your email: {verification_link}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    # # if request.method == "POST": 
    # with get_connection(  
    #           host=settings.EMAIL_HOST, 
    #     port=settings.EMAIL_PORT,  
    #    username=settings.EMAIL_HOST_USER,  
    #    password=settings.EMAIL_HOST_PASSWORD,  
    #     use_tls=settings.EMAIL_USE_TLS 
    #     ) as connection:
    #     EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  

    sm(subject, message, from_email, recipient_list,fail_silently=False)

    # def send_emails(request):  
    # :  
    #         recipient_list = request.POST.get("email").split()  
    #         subject = request.POST.get("subject")  
    #         email_from = settings.EMAIL_HOST_USER  
    #         message = request.POST.get("message")  
    #         print(type(recipient_list)) 
  
    # return render(request, 'send_emails.html')