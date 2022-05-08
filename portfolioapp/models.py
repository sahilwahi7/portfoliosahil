from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class About(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


class Resume(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


class Projects(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content
