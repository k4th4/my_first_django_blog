from django.contrib import admin
from .models import Post
from .models import TextEntry

admin.site.register(Post)
admin.site.register(TextEntry)