from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model


class EmailAuthBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        usermodel = get_user_model()

        try:
            user = usermodel.objects.get(email=username)
            if user.check_password(password):
                return user
            return None

        except (usermodel.DoesNotExist, usermodel.MultipleObjectsReturned):
            return None


    def get_user(self, user_id):
        usermodel = get_user_model()
        try:
            user = usermodel.objects.get(pk=user_id)
            return user
        except (usermodel.DoesNotExist, usermodel.MultipleObjectsReturned):
            return None
