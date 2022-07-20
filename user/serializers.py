from django.contrib.auth.hashers import check_password
from rest_framework import exceptions, serializers
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ('email', 'password', 'nickname')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        email = validated_data['email']
        nickname = validated_data['nickname']

        user = User.objects.create_user(email=email, nickname=nickname)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserInfoSerializer(serializers.Serializer):

    user = serializers.CharField()
    refresh = serializers.CharField()
    access = serializers.CharField()


class SignInSerializer(TokenObtainPairSerializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, max_length=255)

    def signin(self, data):

        user = User.objects.filter(email=data['email']).first()
        if not user or not check_password(data['password'], user.password):
            raise_exception = exceptions.APIException(detail="fail signin")
            raise_exception.status_code = status.HTTP_400_BAD_REQUEST

        refresh = super().get_token(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        data = {
            'user': str(user),
            'refresh': refresh_token,
            'access': access_token,
            'message': '로그인에 성공했습니다.',
        }

        serializer = UserInfoSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return serializer.data
