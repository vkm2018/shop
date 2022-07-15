from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.account.serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializers

User = get_user_model()


class RegisterApiView(APIView):
    def post(self, request):
        data = request.data
        serializers = RegisterSerializer(data=data)

        if serializers.is_valid(raise_exception=True):
            serializers.save()
            message = 'Вы успешно зарегистрировались.' \
                      f'Вам отправлено письмо с активацией'
            return Response(message, status=201)


class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activate_code= activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msq': 'Успешно'}, status=200)
        except User.DoesNotExist:
            return  Response({'msq': 'Неверный код!'}, status=400)


class LoginApiView(ObtainAuthToken):
    serializer_class = LoginSerializer

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializers = ChangePasswordSerializers(data=request.data, context={'request': request})
        serializers.is_valid(raise_exception=True)
        serializers.set_new_password()
        return Response('Пароль  успешно обновлен')






