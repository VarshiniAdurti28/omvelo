from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
      
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class SubscriptionPlan(models.Model):
    subs_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.PositiveIntegerField()  
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subs_name
    

class User(AbstractBaseUser):
    Name = models.CharField(max_length=100, blank=False)
    ph_no=models.BigIntegerField()
    username = models.CharField(unique=True, max_length=150, blank=False)
    uid = models.AutoField(primary_key=True)
    objects = CustomUserManager()
    subscription_plan = models.ForeignKey(SubscriptionPlan, null=True, on_delete=models.SET_NULL)
    subscription_expiry = models.DateTimeField(null=False, blank=False)

    USERNAME_FIELD = 'username'

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username

    
class Bicycle(models.Model):
    # qr_code = models.CharField(max_length=100, unique=True)
    is_available = models.BooleanField(default=True)
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    last_unlocked_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Bicycle {self.id}"
    
class Ride(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bicycle = models.ForeignKey(Bicycle, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    start_location_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    start_location_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    end_location_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    end_location_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"Ride by {self.user.username} on {self.bicycle.id}"



