from rest_framework import serializers

from profiles_api import models
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView and can also handle validations"""
    name=serializers.CharField(max_length=10)

    """It tells us which fields are we expecting in the request body"""

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model=models.UserProfile
        """List down the fields that you want to get managed through the serializer"""
        """List of all the fields that we want to make accessible through our API or you want to create new models with our serializer"""
        fields=('id','name','email','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{
                    'input_type':'password'
                }
            }
        }

    def create(self,validated_data):
        """Create and return a new user"""
        user=models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)