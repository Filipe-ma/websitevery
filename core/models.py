from django.db import models

class Header(models.Model):
    header_logo = models.ImageField(upload_to='media/')
    social_media_links = models.ManyToManyField('SocialMediaLink')
    footer_content = models.TextField()

    def __str__(self):
        return "header"

class SocialMediaLink(models.Model):
    image = models.ImageField(upload_to='media/')
    url = models.URLField()

    def __str__(self):
        return self.url

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/')
    title2 = models.CharField(max_length=100)
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()

    def __str__(self):
        return self.title

class Section1(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='section1_images/')
    button = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Section2(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.title

class Section3(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='section3_images/')
    button = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Section4(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='section4_images/')
    title2 = models.CharField(max_length=100)
    description2 = models.TextField()
    button = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Section5(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='section5_images/')
    button = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Section6(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='service_images/')
    description1 = models.TextField()

    def __str__(self):
        return self.title

class Description(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Body(models.Model):
    title = models.CharField(max_length=100)
    description1 = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
