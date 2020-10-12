from django.db import models
# from django.contrib.auth.models import user
# import other model for foriegn keys
import django.utils.timezone

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    # author = models.FireignKey(User, on_delete=models.CASCADE)
