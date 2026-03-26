from django.contrib import admin

from .models import CityWorkerSignup, Gutter, HomeownerSignup


@admin.register(HomeownerSignup)
class HomeownerSignupAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'created_at')
    search_fields = ('full_name', 'email', 'street_address')
    readonly_fields = ('created_at',)


@admin.register(CityWorkerSignup)
class CityWorkerSignupAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'work_location', 'email', 'created_at')
    search_fields = ('full_name', 'email', 'work_location')
    readonly_fields = ('created_at',)


@admin.register(Gutter)
class GutterAdmin(admin.ModelAdmin):
    list_display = (
        'site_code',
        'location_description',
        'cleaning_priority',
        'needs_cleaning',
        'debris_level_percent',
        'last_sensor_read_at',
        'updated_at',
    )
    list_filter = ('needs_cleaning',)
    search_fields = ('site_code', 'location_description', 'notes')
    readonly_fields = ('updated_at',)
