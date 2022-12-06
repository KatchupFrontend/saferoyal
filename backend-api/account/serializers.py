from rest_framework.serializers import ModelSerializer
from properties_app.models import Customer
from hashlib import sha256


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id','fullname','email','password','phone_number',]
        extra_kwargs = {
            'password': {
                'write_only':True
            }
        }

    def create(self, validated_data):
        email = validated_data.get('email')
        fullname = validated_data.get('fullname')
        password = sha256(validated_data.get('password').encode())
        phone_number = validated_data.get('phone_number')
        hashed_password = password.hexdigest()
        # Create user
        return Customer.objects.create(email = email, fullname = fullname, password = hashed_password, phone_number = phone_number)
