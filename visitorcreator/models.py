from __future__ import unicode_literals

from django.db import models as md
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# visitor class for models with usage of validators


class Visitor(md.Model):
    name = md.CharField(max_length=60)
    email = md.CharField(max_length=255, validators=[EmailValidator])
    photo = md.ImageField(blank=True)
    phone_number = PhoneNumberField()
    address = md.CharField(max_length=100)
    visitor_type = md.CharField(max_length=20, null=True)
    company_to_visit = md.CharField(max_length=60, null=True, blank=True)
    employee_to_visit = md.CharField(max_length=60, null=True, blank=True)
    mail_list_sub = md.BooleanField(default=False)
    description = md.TextField(blank=True)

