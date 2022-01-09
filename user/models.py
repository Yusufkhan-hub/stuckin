from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db.models import base
# Create your models here.
from .managers import CustomUsersManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from datetime import date, datetime


class CustomUsers(AbstractBaseUser,PermissionsMixin):
    
    
    id=models.CharField(max_length=50,primary_key=True)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=200,unique=True)
    email = models.EmailField(max_length=254,unique=True)
    is_staff = models.BooleanField(_("staff status"),default=False)
    is_active = models.BooleanField(_("active"),default=True)
    date_joined = models.DateTimeField(default=datetime.now())
    
    objects  = CustomUsersManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS  = ['email']
    
    class Meta:
        db_table = 'custome_user'
        managed = True
        
    # def get_absolute_url(self):
    #     return "account_configuration/%s/" % urlquote(self.email) 
    
    def get_full_name(self):
        return self.username
    
