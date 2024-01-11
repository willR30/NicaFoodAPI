from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Food_image(models.Model):
    image_url = models.TextField(null=True)

    def __str__(self):
        return self.image_url


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    image_url = models.ManyToManyField(Food_image)
    department=models.ManyToManyField(Department)

    def __str__(self):
        return self.name
