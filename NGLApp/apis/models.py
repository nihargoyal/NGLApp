from django.db import models

class App(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=250)
    points = models.PositiveIntegerField()

class UserTask(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/', blank=True, null=True)
    points = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)