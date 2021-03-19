from django.db import models

# Create your models here.
class Reg(models.Model):
	usname = models.CharField(max_length=120)
	psd = models.CharField(max_length=80)
