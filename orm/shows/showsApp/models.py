from django.db import models
from datetime import datetime
class showManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData["title"]) < 2:
            errors["title"] = "Title should be at least 2 characters"

        if len(postData["network"]) < 3:
            errors["network"] = "show network should be at least 3 characters"

        if len(postData["desc"]) < 10:
            errors["desc"] = "Description should be at least 10 characters"

        if postData:
            errors["desc"] = "Description should be at least 10 characters"

        if len(postData["desc"]) < 10:
            errors["desc"] = "Description should be at least 10 characters"

        return errors

# Create your models here.
class show(models.Model):
    title=models.CharField(max_length=255,default="title")
    network = models.CharField(max_length=255,default="network")
    release_date=models.DateField()
    desc = models.TextField(default="nth")
    objects = showManager()
    def __str__(self):
        return f"<User object: {self.title+self.network} ({self.id})>"

    #d = datetime.date(2020, 10, 19)

    #d.strftime('%B %d ,%Y')
