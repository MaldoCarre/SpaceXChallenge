
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import CarInfoSerializer, ResponseCardSerializer
from rest_framework.views import APIView
from rest_framework import status
from .actions import checktasck
# Create your views here.


"""
creating the api view.
"""
class CardCreation(APIView):
    def post (self,request):
        serializer = CarInfoSerializer(data=request.data)
        serializer.is_valid(True)
        data_for_card = serializer.data
        try:
            res_data =checktasck(data_for_card)
            return Response(status=status.HTTP_200_OK, data=res_data)
        except Exception:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
