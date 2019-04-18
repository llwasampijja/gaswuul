from rest_framework import status
from django.contrib.auth import login
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth.password_validation import ValidationError
from .serializers import UserSerializer, LoginSerializer


class SignUp(APIView):
    """
    post:
    Register a user.
    """

    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
            except ValidationError as errors:
                return Response(
                        data={"status": 400,
                              "errors": [errors]
                              },
                        status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(
                data={
                    "status": status.HTTP_201_CREATED,
                    "data": [
                        {
                            "username": user.username,
                            "email": user.email,
                            "is_admin": user.is_superuser,
                        }
                    ],
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            data={"status": 400, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

class Login(APIView):
    """
    post:
    login a user.
    """

    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            data={"Username": serializer.data['username'],
                  "Email": serializer.data['email'],
                  "token": serializer.data['token']},
            status=status.HTTP_200_OK

        )