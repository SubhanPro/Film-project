from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=150, help_text="Please enter your name")
    surname = models.CharField(max_length=150, help_text="Please enter your surname")
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=30)
    message = models.TextField()

    class Meta:
        verbose_name = "Contact"

    def __str__(self):
        return self.name + " " + self.surname
