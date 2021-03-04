from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from .signals import create_user_profile, save_user_profile



class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = _('profile')
    
    def ready(self):
        post_save.connect(create_profile, sender=User)
        post_save.connect(save_profile, sender=User)