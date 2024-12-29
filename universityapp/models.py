from django.db import models
#from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=600)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Comment by {self.name} on {self.date}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=600)

    def __str__(self):
        return f"{self.name} {self.subject}"


    '''def set_password(self, password):
        # Hash the password and save it
        self.password = make_password(password)

    def check_password(self, password):
        # Check if the provided password matches the stored hashed password
        return check_password(password, self.password)'''