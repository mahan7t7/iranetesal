from django.db import models

# Create your models here.
from django.db import models
import uuid
from django.contrib import messages
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):

    def create(self, user, password):
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, phone, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not (email and phone):
            raise ValueError('Users must have an email address and phone number')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user_complete(self,  first_name, last_name, company_name, phone, email, password=None):
        
        
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
            email=self.normalize_email(email),
            phone=phone,
        )
        
        user.set_password(password)
        try:
            user.save(using=self._db)
        except:
            print("cant")
        
        return user    


    def create_staffuser(self, username, email, phone, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            email,
            phone,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            email,
            phone,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):
    username          = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email             = models.EmailField(verbose_name='email', max_length=60, unique=True)
    phone             = PhoneNumberField(verbose_name='phone', unique=True)
    first_name        = models.CharField(verbose_name='first name', max_length=60)
    company_name      = models.CharField(verbose_name='company name', max_length=60, null=True)
    last_name         = models.CharField(verbose_name='last name', max_length=60)
    date_joined       = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login        = models.DateTimeField(verbose_name='last login', auto_now=True)
    active            = models.BooleanField(default=True)
    vip               = models.BooleanField(default=False)
    staff             = models.BooleanField(default=False) # a admin user; non super-user
    admin             = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that's built in.

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone'] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    @property
    def is_vip(self):
        "can User buy with cheque?"
        return self.vip