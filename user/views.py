from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import SignInSerializer, SignUpSerializer


class SignUpAPIView(APIView):

    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignInAPIView(APIView):

    permission_classes = [AllowAny]
    serializer_class = SignInSerializer

    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer)

        return Response(serializer.signin(data=request.data), status=status.HTTP_200_OK)


class SignOutAPIView(APIView):
    def post(self, request):
        Refresh_token = request.data['refresh']
        token = RefreshToken(Refresh_token)
        token.blacklist()

        return Response({"detail": "로그아웃 되었습니다."}, status=status.HTTP_200_OK)
