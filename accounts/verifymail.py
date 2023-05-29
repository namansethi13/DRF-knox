from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def verify_mail(request, token):
    if token is None:
        return HttpResponseBadRequest('Token is missing.')
    try:
        user = User.objects.get(id=default_token_generator.check_token(user, token))
    except User.DoesNotExist:
        return HttpResponseBadRequest('Invalid token.')
    user.userdetails.is_email_verified = True
    user.userdetails.save()

    return Response("Email verification successful.")