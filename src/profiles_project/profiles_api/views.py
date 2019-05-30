
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.views import View
from rest_framework.response import Response

# Create your views here.


class HelloApiView(APIView):
    """TEST Api View"""

    def get(self, request, format=None):
        """Returns a list of API View Features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'similar to django view',
            'bla bla bla'
        ]


        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

