from django.contrib import admin

from .models import Birthday


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )
    list_editable = (
        'last_name',
        'birthday',
    )


admin.site.register(Birthday, BirthdayAdmin)
