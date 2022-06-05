from fileinput import filename
from importlib.resources import path
import json
import os
import pandas as pd
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404, HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Clients, Bills, Products
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import BillsSerializer, ClientsSerializer, RelationBillsSerializer, RelationClientsSerializer, RelationProductsSerializer
from pathlib import Path
# Create your views here.


class CSV(APIView):
    """_
    Handle class for Upload and download CSV
    """

    def get(self, request):
        query = 'SELECT * FROM Rest_API_clients'
        data = Clients.objects.raw(query)
        info_dataframe = []
        for client in data:
            total_bills = Bills.objects.filter(client_id=client.id).count()
            items = {}
            items["document"] = client.document
            items["full_name"] = f"{client.first_name} {client.last_name}"
            items["total_bills"] = total_bills
            info_dataframe.append(items)

        df = pd.DataFrame(info_dataframe)
        compression_opts = dict(method='zip', archive_name='BillsByClient.csv')
        df.to_csv('Bills.zip', index=False, compression=compression_opts)
        path_file = os.getcwdb()
        return Response({"path_file": path_file}, status=status.HTTP_201_CREATED)

    def post(self, request):
        for file in request.FILES:
            file_csv = request.FILES[file]

        df = pd.read_csv(file_csv)
        data_json = df.to_json(orient='records')
        data = json.loads(data_json)
        serializer = RelationClientsSerializer(data=data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CRUDClients(APIView):
    """
    Create,Retrieve,Update or Delete an objects Clients
    """
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

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
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

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
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

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
