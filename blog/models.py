from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    apodo = models.CharField(max_length=200)
    descripcion = models.TextField()
    created_date = models.DateTimeField(
                default=timezone.now)
    published_date = models.DateTimeField(
                blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre