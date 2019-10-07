from django.contrib import admin
from . import models

admin.site.register(models.Users)
admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.Place)
admin.site.register(models.Restaurant)
admin.site.register(models.Waiter)
admin.site.register(models.Publication)
admin.site.register(models.Article)
