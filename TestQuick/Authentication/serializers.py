from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import CustomUser
from django.core import exceptions
import django.contrib.auth.password_validation as validators


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(min_length=8, write_only=True)

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        if attrs['password'] != password2:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        user = CustomUser(**attrs)
        password = attrs.get('password')
        errors = dict()
        try:
            validators.validate_password(password=password, user=user)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)
        return super(UserSerializer, self).validate(attrs)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'], validated_data['email'],
                                              validated_data['password'])
        return user

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'password2')
