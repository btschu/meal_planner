from django.db import models
import re

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 1:
            errors["first_name"] = "Please enter a FIRST NAME"
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Please enter a LAST NAME"
        if len(postData['email']) >= 1:
            errors["email"] = "That EMAIL ADDRESS is already registered"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please enter a valid EMAIL ADDRESS"
        if len(postData['password']) < 8:
            errors["password"] = "Your PASSWORD must be at least 8 characters long"
        if not any(char.isdigit() for char in postData['password']):
            errors["password"] = "Your PASSWORD must contain at least one number"
        if not any(char.isupper() for char in postData['password']):
            errors["password"] = "Your PASSWORD must contain at least one uppercase letter"
        if postData['password'] != postData['confirm']:
            errors["password"] = "Your PASSWORDS do not match"
        return errors

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address or password!"
        if (len(postData['password']) < 8):
            errors['password'] = "Invalid email address or password!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
