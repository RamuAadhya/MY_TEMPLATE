from django.contrib import admin
from .models import Contact,About

# Register your models here.



class ContactAdmin(admin.ModelAdmin):
    list_display = ('email','name','is_active','created_at')
    list_filter = ('is_active','created_at')








admin.site.register(Contact,ContactAdmin)



admin.site.register(About)