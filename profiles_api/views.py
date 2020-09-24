from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,format=None):
        """Returns a list of API View features"""
        features=[
            "Uses HTTP methods as functions(get,post,put,patch,delete)",
            "Is similar to a traditional Django View",
            "Gives you more control over your application logic",
            "Is mapped manually to URLs"
        ]
        return Response({'message':'Hello!','features':features})