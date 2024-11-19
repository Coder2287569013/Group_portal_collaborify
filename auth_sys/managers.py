from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **o_fields):
        if not email:
            raise ValueError("Email problem")
        email = self.normalize_email(email)
        user = self.model(email=email, **o_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **o_fields):
        o_fields.setdefault("is_staff", True)
        o_fields.setdefault("is_superuser", True)
        o_fields.setdefault("is_active", True)

        if o_fields.get("is_staff") is not True or o_fields.get("is_superuser") is not True:
            raise ValueError("Missing role")

        return self.create_user(email, password, **o_fields)
