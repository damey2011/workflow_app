from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from rest_framework.authtoken.models import Token

# from process.models import FormResponseFile


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser, BaseModel):
    email = models.EmailField(
        'email address',
        max_length=150,
        unique=True,
        blank=False,
        help_text="Required. Enter a valid email address",
        error_messages={
            'unique': "A user with that email already exists.",
        })
    first_name = models.CharField('first name', max_length=30)
    last_name = models.CharField('last name', max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=11, validators=[RegexValidator(regex='^\d{11}$')])
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=6, null=True)
    is_email_verified = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=128, null=True)
    reset_password_key = models.CharField(max_length=128, null=True)
    is_reset_password_key_used = models.BooleanField(default=False)
    key_expires = models.DateTimeField(null=True)
    reset_passsword_key_expires = models.DateTimeField(null=True)
    profile_pic = models.ImageField(null=True, blank=False)
    # organization = models.ManyToManyField(Organization, related_name="users_in_org", blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=False,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True,
                                 **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
