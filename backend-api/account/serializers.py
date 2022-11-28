from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','email','password']
        extra_kwargs = {
            'password': {
                'write_only':True
            }
        }