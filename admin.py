from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Post
from .models import Question

admin.site.register(Book)
admin.site.register(Post)
admin.site.register(Question)