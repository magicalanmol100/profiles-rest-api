from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of API View features"""
        features=[
            "Uses HTTP methods as functions(get,post,put,patch,delete)",
            "Is similar to a traditional Django View",
            "Gives you more control over your application logic",
            "Is mapped manually to URLs"
        ]
        return Response({'message':'Hello!','features':features})
    
    def post(self,request):
        """Create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            #To retrieve any field that you defined inside a serializer
            message=f"Hello {name}"
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            #errors will give you a dictionary of errors based on the validation rules that were applied by the serializer,
            #so that person who uses the API knows what went wrong
    
    def put(self,request,pk=None):
        """Handles updating an object. pk is the id of the object to be updated with put request"""
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        """Handles partial updating of an object"""
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        """Handles deleting an object"""
        return Response({'method':'DELETE'})
