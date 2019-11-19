from django.contrib import admin
from .models import Notice,User_details
# Register your models here.


class NoticeAdmin(admin.ModelAdmin):
	list_display=('subject', 'description')

admin.site.register(Notice,NoticeAdmin)
admin.site.register(User_details)