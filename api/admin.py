from django.contrib import admin
from api.models import Event, User
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets+ (
        (                      
            'Location', # you can also use None 
            {
                'fields': (
                    'location',
                ),
            },
        ),
    )


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date', 'sport', 'role', 'coach_user')
admin.site.register(Event, EventAdmin)
