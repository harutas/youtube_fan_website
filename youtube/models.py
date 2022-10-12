from django.db import models

# Create your models here.
class Youtube(models.Model):
  genre_name = models.CharField(max_length=70)
  img_url = models.CharField(max_length=255)
  genre_description = models.TextField(max_length=255)

  def __str__(self):
    return self.genre_name


class Notable(models.Model):
  name = models.CharField(max_length=70)
  img_url = models.CharField(max_length=255)
  description = models.TextField(max_length=255)
  youtube = models.ForeignKey(Youtube, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
  
  
class Link(models.Model):
  title = models.CharField(max_length=70, null=True)
  link = models.URLField()
  youtube = models.ForeignKey(Youtube, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title