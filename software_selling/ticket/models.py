from django.db import models

from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

"""
    Ticket Class
"""
class Ticket(models.Model):

    STATUS = (
        ("waiting","در انتظار"),
        ("checking","درحال بررسی"),
        ("close","بسته شد")
    )

    user        =   models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title       =   models.CharField(max_length=255,verbose_name="عنوان")
    slug        =   models.CharField(max_length=255,verbose_name="نامک")
    desc        =   models.TextField(verbose_name="توضیحات")
    track_id    =   models.CharField(max_length=64,verbose_name="کد پیگیری")
    status      =   models.CharField(max_length=20,choices=STATUS,default="waiting",verbose_name="وضعیت")
    created_at  =   models.DateField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    updated_at  =   models.DateField(auto_now=True,verbose_name="تاریخ ویرایش")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "تیکت"
        verbose_name_plural = "تیکت‌ها"



"""
    Ticket File
"""
class TicketFile(models.Model):
    Ticket      =   models.ForeignKey(Ticket,on_delete=models.CASCADE)
    image       =   models.ImageField(verbose_name="فایل پیوست")
    created_at  =   models.DateField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    updated_at  =   models.DateField(auto_now=True,verbose_name="تاریخ ویرایش")
