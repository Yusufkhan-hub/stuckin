from django.contrib.auth.models import BaseUserManager
from django.db import reset_queries
from django.utils import timezone
from datetime import date, datetime

class CustomUsersManager(BaseUserManager):
    use_for_related_fields = True
    
    def _create_user(self,username,password,is_staff,is_superuser,**extra_fields):
        
        now = (datetime.now())
        if not username:
            raise ValueError("The given username must be set")
        user = self.model(username=username,
                          is_staff=is_staff,is_active=True,
                          is_superuser=is_superuser,last_login=now
                          ,date_joined=now,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_user(self,username,password=None,**extra_fields):
        return self._create_user(username,password,True,True,**extra_fields)
    def create_superuser(self,username,password,**extra_fields):
        return self._create_user(username,password,True,True,**extra_fields)
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field:username})
        
        
        