from rest_framework import serializers
from .models import User, Product
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)
    confirm_password = serializers.CharField(write_only = True)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")

        return data
    
    def validate_email(self, value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError("Email address is already is use")
        return value 
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password']
        )

        return user
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError("An email address is required for login")
        
        if password is None:
            raise serializers.ValidationError("An password is required for login")
        
        user = authenticate(username = email, password=password)

        if user is None:
            raise serializers.ValidationError(
                "Invalid Email or Password"
            )
        
        if not user.is_active:
            raise serializers.ValidationError(
                "User is inactive"
            )
        # user_id = getattr(user, 'id', None)

        # if user_id is None:
        #     raise serializers.ValidationError("User object does not have an 'id' attribute")
        
        # return{
        #     "email" : user.email,
        #     "user_id": user.id 
        # }
        
        data['user'] = user
        return data
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'price','image']