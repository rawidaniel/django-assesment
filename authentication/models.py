from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    ADMIN = 'Admin'
    COACH = 'Coach'
    AGENT = 'Agent'
    FOOTBALLPLAYER = 'Footballplayer'
    USER_ROLE = [
       (ADMIN, ADMIN),
       (COACH, COACH),
       (AGENT,AGENT ),
       (FOOTBALLPLAYER, FOOTBALLPLAYER)
   ]
    role = models.CharField(max_length=20,
                           choices=USER_ROLE)