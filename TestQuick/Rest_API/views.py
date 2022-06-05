from multiprocessing.connection import Client
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404, HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from .models import Clients, Bills, Products
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import BillsSerializer, ClientsSerializer, RelationBillsSerializer, RelationClientsSerializer, RelationProductsSerializer
# Create your views here.


class CRUDClients(APIView):
    """
    Create,Retrieve,Update or Delete an objects Clients
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Clients.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = ClientsSerializer(data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            data = Clients.objects.all()
            serializer = RelationClientsSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def post(self, request, format=None):
        serializer = RelationClientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = RelationClientsSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CRUDBills(APIView):
    """
    Create,Retrieve,Update or Delete an objects Clients
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Bills.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = RelationBillsSerializer(data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            data = Bills.objects.all()
            serializer = RelationBillsSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def post(self, request, format=None):
        serializer = BillsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = RelationBillsSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CRUDProducts(APIView):
    """
    Create,Retrieve,Update or Delete an objects Clients
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = RelationProductsSerializer(data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            data = Products.objects.all()
            serializer = RelationProductsSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def post(self, request, format=None):
        serializer = RelationProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = RelationProductsSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
