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

    def create(self, validated_data):
        email = validated_data.get('email')
        username = validated_data.get('username')
        first_name = validated_data.get('firstName')
        last_name = validated_data.get('lastName')
        password = validated_data.get('password')
        # Create user
        return User.objects.create_user(username=username,email=email,password=password,first_name = first_name,last_name=last_name)
