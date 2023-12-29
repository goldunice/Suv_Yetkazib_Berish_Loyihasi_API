from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


class SuvlarAPIView(APIView):
    def get(self, request):
        suv = Suv.objects.all()
        serializer = SuvSerializer(suv, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SuvSerializer)
    def post(self, request):
        suv = request.data
        serializer = SuvSerializer(data=suv)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class SuvAPIView(APIView):
    def get(self, request, pk):
        suv = Suv.objects.get(id=pk)
        serializer = SuvSerializer(suv)
        return Response(serializer.data, status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SuvSerializer)
    def put(self, request, pk):
        suv = Suv.objects.get(id=pk)
        serializer = SuvSerializer(suv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors)


class MijozlarAPIView(APIView):
    def get(self, request):
        mijoz = Mijoz.objects.all()
        ismi = request.query_params('ismi')
        teli = request.query_params('teli')
        if ismi:
            mijoz = mijoz.filter(ism__startswith=ismi)
        if teli:
            mijoz = mijoz.filter(tel=teli)
        serializer = MijozSerializer(mijoz, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    @swagger_auto_schema(request_body=MijozSerializer)
    def post(self, request):
        mijoz = request.data
        serializer = MijozSerializer(data=mijoz)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class MijozAPIView(APIView):
    def get(self, request, pk):
        mijoz = Mijoz.objects.get(id=pk)
        serializer = MijozSerializer(mijoz)
        return Response(serializer.data, status.HTTP_200_OK)

    @swagger_auto_schema(request_body=MijozSerializer)
    def put(self, request, pk):
        mijoz = Mijoz.objects.get(id=pk)
        serializer = MijozSerializer(mijoz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors)


class BuyurtmalarAPIView(APIView):
    def get(self, request):
        buyurtma = Buyurtma.objects.all()
        serializer = BuyurtmaSerializer(buyurtma, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    @swagger_auto_schema(request_body=BuyurtmaSerializer)
    def post(self, request):
        buyurtma = request.data
        serializer = BuyurtmaSerializer(data=buyurtma)
        if serializer.is_valid():
            serializer.save(mijoz=request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class AdminlarAPIView(APIView):
    def get(self, request):
        admin = Admin.objects.all()
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminAPIView(APIView):
    def get(self, request, pk):
        admin = Admin.objects.get(id=pk)
        serializer = AdminSerializer(admin)
        return Response(serializer.data, status.HTTP_200_OK)


class HaydovchiAPIView(APIView):
    def get(self, request, pk):
        haydovchi = Haydovchi.objects.get(id=pk)
        serializer = HaydovchiSerializer(haydovchi)
        return Response(serializer.data, status.HTTP_200_OK)


class HaydovchilarAPIView(APIView):
    def get(self, request):
        haydovchi = Haydovchi.objects.all()
        serializer = HaydovchiSerializer(haydovchi, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
