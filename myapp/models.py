from django.db import models

# Create your models here.
class Blog(models.Model):

    objects = models.Manager() # solution for "class has no objects member error"

    writer = models.CharField(null=True, max_length = 50)
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    category = models.CharField(null=True, max_length = 50, help_text='friend, family') 


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]