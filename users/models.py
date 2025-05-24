from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DJangoUserManager

class UserManager(DJangoUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다.')
        
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    phone = models.CharField(verbose_name='전화번호', max_length=13)
    birth_year = models.PositiveIntegerField(verbose_name='출생년도', null=True, blank=True)
    birth_month = models.PositiveIntegerField(verbose_name='출생월', null=True, blank=True)
    birth_day = models.PositiveIntegerField(verbose_name='출생일', null=True, blank=True)
    
    GENDER_CHOICES = [
        ('M', '남자'),
        ('F', '여자'),
    ]
    gender = models.CharField(verbose_name='성별', max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    point = models.IntegerField(verbose_name='포인트', default=0)
    address = models.CharField(verbose_name='주소', max_length=60)

    objects = UserManager()

