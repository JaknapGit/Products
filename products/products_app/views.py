from .serializer import ProductSerial, Product
from rest_framework.views import APIView
from django.http import request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class ProductView(APIView):
    def get(self, request):
        product_obj = Product.objects.all()
        serializer = ProductSerial(product_obj, many=True)
        return Response(data= serializer.data)
    
    def post(self, request):
        serialized = ProductSerial(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response('Data saved successfully...')
        return Response(data= {'Bad server request'})
