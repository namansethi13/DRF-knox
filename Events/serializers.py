from rest_framework import serializers
from Events.models import Events
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields ='__all__'
        