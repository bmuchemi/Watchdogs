from django.contrib import admin
from .models import Neighbourhood,Buisness,Post,Profile

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Buisness)
admin.site.register(Post)
admin.site.register(Profile)