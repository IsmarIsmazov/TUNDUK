from django.core.mail import send_mail

from .models import CustomUser
from .tokens import confirmation_code, recovery_code
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

CustomUser = get_user_model()


class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None


def send_email_confirmation(email):
    subject = 'Подтверждение регистрации'
    message = f"""      Здравствуйте! Ваш адрес электронной почты был указан для входа на приложение Meyman. 
    Пожалуйста, введите этот код на странице авторизации:<<< {confirmation_code} >>> 
    Если это не вы или вы не регистрировались на сайте, то просто проигнорируйте это письмо"""
    email_from = 'abdykadyrovsyimyk0708@gmail.com'
    send_mail(subject, message, email_from, [email])
    user_obj = CustomUser.objects.get(email=email)
    user_obj.verify_code = confirmation_code
    user_obj.save()


def send_email_reset_password(email):
    subject = "Восстановление пароля"
    message = f"Код для восстановления пароля: <<< {recovery_code} >>> Код действителен в течении 5 минут"
    email_from = 'abdykadyrovsyimyk0708@gmail.com'
    send_mail(subject, message, email_from, [email])
