from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class hrusers(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField(max_length=10, unique=True, validators=[
        RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    #                              message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    # phone = models.IntegerField(max_length=10)
    address=models.CharField(max_length=1000)
    reg_type=models.CharField(max_length=1000)
    profile_pic=models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class hrlistings(models.Model):
    user_id=models.CharField(max_length=10)
    name=models.CharField(max_length=10)
    photo=models.EmailField(max_length=50)
    phone=models.IntegerField(max_length=10, unique=True, validators=[
        RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    about=models.CharField(max_length=256)
    address=models.CharField(max_length=256)
    verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class hrbookmark(models.Model):
    listing_id=models.ForeignKey(hrlistings, on_delete=models.DO_NOTHING)
    user_id=models.ForeignKey(hrusers, on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.listing_id
