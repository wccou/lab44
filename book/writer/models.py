from django.db import models
from django.contrib import admin

# Create your models here.
class Author(models.Model):
	AuthorID = models.CharField(max_length = 150)
	Name = models.CharField(max_length = 150)
	Age = models.CharField(max_length = 150)
	Country = models.CharField(max_length = 150)

class Authors(admin.ModelAdmin):
	list_display = ('AuthorID','Name','Age','Country')
    
admin.site.register(Author,Authors)	
# admin.site.register(Author)