from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'joined_date')

# also we can create like this 
# admin.site.register(Member)
