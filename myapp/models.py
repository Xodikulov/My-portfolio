from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title
    


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='portfolio/')
    client = models.CharField(max_length=100)
    website = models.URLField()
    completed_date = models.DateField()

    def __str__(self):
        return self.title
    

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    author = models.CharField(max_length=255)
    excerpt = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    read_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    description = models.TextField()  

    def __str__(self):
        return self.first_name

    

