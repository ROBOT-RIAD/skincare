from django.db import models

# Create your models here.


class TempInfoCollect(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    contact_number = models.CharField(max_length=20)
    skin_type = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True, blank=True)

    def __str__(self):
        return self.full_name
