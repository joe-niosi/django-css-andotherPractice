from django.contrib import admin
from firstApp.models import User, Message


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)
class MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Message, MessageAdmin)