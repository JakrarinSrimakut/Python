from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    # add in autor later

    #Migration-whenever Article class update migrate
    #py -3 manage.py makemigrations
    #py -3 manage.py migrate

    #ORM
    #py -3 manage.py shell
    #interact with DB

# Return the title of object when calling object in DB table
    def __str__(self):
        return self.title

# Character limit for body
    def snippit(self):
        return self.body[:50] + '...'