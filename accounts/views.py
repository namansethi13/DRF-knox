from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import permissions
from django.contrib.auth import login
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .models import UserDetails
from django.core.exceptions import PermissionDenied
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from .sendmail import send_mail
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_details = UserDetails.objects.create(user=user, bio='', is_email_verified=False)
        token = default_token_generator.make_token(user)
        send_mail(user, token)
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

#Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_details = user.user_details.get()
        if not user_details.is_email_verified:
             return Response(
                {"error": "Email is not verified."},
                status=status.HTTP_403_FORBIDDEN
            )
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def getuser(request):
    return Response({"user": request.user.username})