from django.contrib import admin
from .models import User,Comment,Contact
# Register your models here.
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Contact)