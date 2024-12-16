from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    friends = models.ManyToManyField(User, related_name='friends', blank=True)

    def __str__(self):
        return str(self.user)