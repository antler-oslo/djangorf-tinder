from django.db import models


class AppUser(models.Model):

    email = models.EmailField()
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    picture = models.ImageField()
    gender = models.CharField(max_length=30,
                choices=[
                    ('female','Female'),
                    ('male','Male'),
                    ('nonbinary','Non-binary'),
                    ('other','Other')
                    ])
    localisation = models.CharField(max_length=200)

    def __str__(self):
        return self.email
