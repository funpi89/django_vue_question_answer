from rest_framework import serializers
from users.models import CustomerUser

class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = ['username']