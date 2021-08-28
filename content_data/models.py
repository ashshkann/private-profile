from django.db import models
from django.db.models.base import Model
from django.db.models.expressions import F

# Create your models here.

class home(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, verbose_name='عنوان')
    logo = models.ImageField(null=False, blank=False, upload_to='media/', verbose_name='لوگو')    
    logo_name = models.CharField(max_length=30, null=False, blank=False, verbose_name='نام در نوبار')
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='اسم')
    job_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='نام شغل')
    url_content = models.URLField(null=False, blank=False, verbose_name='آدرس وب')
    text_button = models.CharField(max_length=30, null=False, blank=False, verbose_name='متن دکمه')
    image_content = models.ImageField(null=False, blank=False, upload_to='media/', verbose_name='عکس')

    class Meta:
        verbose_name = 'صفحه ی خانه'
        verbose_name_plural = 'صفحه ی خانه'

    def __str__(self):
        return self.name


class about(models.Model):
    text_title = models.CharField(max_length=50, null=False, blank=False, verbose_name='عنوان توضیحات')
    content_text = models.TextField(null=False, blank=False, verbose_name='توضیحات')
    image_content = models.ImageField(null=False, blank=False, upload_to='media/', verbose_name='عکس')

    class Meta:
        verbose_name = 'توضیحات'
        verbose_name_plural = 'توضیحات'

    def __str__(self):
        return self.text_title

class contact(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    text = models.TextField(verbose_name='متن پیام')
    is_read = models.BooleanField(verbose_name='خوانده شده / نشده')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس های کاربران'

    def __str__(self):
        return self.full_name

class work(models.Model):
    image_1 = models.ImageField(null=False, blank=False, upload_to='media/', verbose_name="عکس نمونه ۱")
    image_2 = models.ImageField(null=False, blank=False, upload_to='media/', verbose_name="عکس نمونه ۲")
    image_3 = models.ImageField(null=False, blank=False, upload_to='media/', verbose_name="عکس نمونه ۳")
    image_4 = models.ImageField(null=False, blank=False, upload_to='media/', verbose_name="عکس نمونه ۴")
    image_5 = models.ImageField(null=False, blank=False, upload_to='media/', verbose_name="عکس نمونه ۵")
    image_6 = models.ImageField(null=False, blank=False, upload_to='media/', verbose_name="عکس نمونه ۶")

    class Meta:
        verbose_name = 'عکس'
        verbose_name_plural = 'عکس ها'




class footer(models.Model):
    text_footer = models.CharField(null=False, blank=False, max_length=150, default=None, verbose_name='متن آخر صفحه')
    url_field_tel = models.URLField(null=False, blank=False, default=None, verbose_name='آدرس وب تلگرام')
    url_field_insta = models.URLField(null=False, blank=False, default=None, verbose_name='آدرس وب اینستاگرام')
    url_field_google = models.URLField(null=False, blank=False, default=None, verbose_name='آدرس وب گوگل درایو')
    text_copyright = models.CharField(null=False, blank=False, max_length=150, default=None, verbose_name='متن کپی رایت')

    class Meta:
        verbose_name = 'آخر صفحه'
        verbose_name_plural = 'آخر صفحه'

    def __str__(self):
        return self.text_footer