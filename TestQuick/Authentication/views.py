
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import permissions, status
from .serializers import UserSerializer


class CRUDUser(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                return Response(token.key, status=status.HTTP_201_CREATED)
            return Response(token.key, status=status.HTTP_304_NOT_MODIFIED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
