from django.core.mail import send_mail as sm


def send_mail(user, token):
    verification_link = f"http://127.0.0.0/api/account/verify_token/{token}"
    subject = "Email Verification"
    message = f"Please click the following link to verify your email: {verification_link}"
    from_email = "computerspgi@gmail.com"
    recipient_list = [user.email]
    sm(subject, message, from_email, recipient_list, auth_password="" )