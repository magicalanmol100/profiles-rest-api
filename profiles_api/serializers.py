from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView and can also handle validations"""
    name=serializers.CharField(max_length=10)

    """It tells us which fields are we expecting in the request body"""