from django.contrib import admin
from .models import Post

# to make the model visible on the admin page410
admin.site.register(Post)
