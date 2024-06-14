from django.contrib.auth import logout

from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, response
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from .serializers import SignUpSerializer, LoginSerializer, VerifySerializer, \
    PasswordResetSearchUserSerializer, PasswordResetCodeSerializer, PasswordResetNewPasswordSerializer, \
    CustomUserSerializer, ChangePasswordSerializer
from .utils import login_user, VerifyService, RegisterService, ResetPasswordSendEmail, PasswordResetCode, \
    PasswordResetNewPassword


class CustomUserView(APIView):

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        return RegisterService.create_user(self.serializer_class(data=request.data), request)


class VerifyOTP(APIView):
    serializer_class = VerifySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        return VerifyService.verify_code(serializer)


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return login_user(serializer)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetRequestAPIView(generics.CreateAPIView):
    serializer_class = PasswordResetSearchUserSerializer

    def post(self, request, *args, **kwargs):
        reset_password_service = ResetPasswordSendEmail()
        return reset_password_service.password_reset_email(self, request)


class PasswordResetCodeAPIView(generics.CreateAPIView):
    serializer_class = PasswordResetCodeSerializer

    def post(self, request, *args, **kwargs):
        reset_password_code = PasswordResetCode()
        return reset_password_code.password_reset_code(self, request)


class PasswordResetNewPasswordAPIView(generics.CreateAPIView):
    serializer_class = PasswordResetNewPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            code = kwargs["code"]
            password = serializer.validated_data["password"]
            success, message = PasswordResetNewPassword.password_reset_new_password(code, password)
            if success:
                return response.Response(data={"detail": message}, status=status.HTTP_200_OK)
            else:
                return response.Response(data={"detail": message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserTypeView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        new_user_type = request.data.get('user_type')

        if new_user_type is not None:
            user.user_type = new_user_type
            user.save()
            return Response({'message': 'User type updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data.get('old_password')
            new_password = serializer.validated_data.get('new_password')
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                return Response({'message': 'Пароль успешно изменен.'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Неверный старый пароль.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout Successful"}, status=status.HTTP_200_OK)
