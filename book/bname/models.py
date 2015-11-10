from django.db import models
from django.contrib import admin
class Book(models.Model):
	ISBN = models.CharField(max_length = 150)
	test =  models.CharField(max_length = 150)
	B2 =  models.CharField(max_length = 150)
	Title = models.CharField(max_length = 150)
	AuthorID = models.CharField(max_length = 150)
	Publisher = models.CharField(max_length = 150)
	PublishDate = models.CharField(max_length = 150)
	Price = models.CharField(max_length = 150)

	
class BooksAdmin(admin.ModelAdmin):
	list_display = ('Title','ISBN','AuthorID','Publisher','Price')
    
admin.site.register(Book,BooksAdmin)

# admin.site.register(Book)
