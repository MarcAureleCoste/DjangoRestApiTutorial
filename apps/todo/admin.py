from django.contrib import admin
from .models import (
    Todo,
    TodoUser
)


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'finished')


@admin.register(TodoUser)
class TodoUserAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_useremail',)

    def get_username(self, obj):
        """Return the username of the 'user' model."""
        return obj.d_user.username
    get_username.short_description = 'Username'

    def get_useremail(self, obj):
        """Return the mail of the 'user' model."""
        return obj.d_user.email
    get_useremail.short_description = 'User email'
