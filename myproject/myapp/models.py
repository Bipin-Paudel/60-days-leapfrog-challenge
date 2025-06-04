from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
