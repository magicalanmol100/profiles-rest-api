from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """Return a hello message"""

        a_viewset=[
            'Uses actions (list, create, update, partial update, retrieve, destroy',
            'Automatically mapped to URLs using Routers',
            'Provides more functionality with less code'
        ]
        return Response({"message":"Hello","a_viewset":a_viewset})
    
    def create(self,request):
        """Create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f"Hello {name}"
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        """Handle getting an object by its id"""
        return Response({'method':'GET'})
    
    def update(self,request,pk=None):
        """Handles updating an object by its id"""
        return Response({'method':'PUT'})
    
    def partial_update(self,request,pk=None):
        """Handles partially updating an object"""
        return Response({'method':'PATCH'})
    
    def destroy(self,request,pk=None):
        """Handles removing an object"""
        return Response({'method':'DELETE'})
    

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updaing profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email')
    #It will allow us to search for a specific profile through email name and password
    #This is how you add search filtering to a viewset in django rest framework