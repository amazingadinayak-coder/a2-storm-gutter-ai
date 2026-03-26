from django.db import models


class HomeownerSignup(models.Model):
    full_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} ({self.email})"


class CityWorkerSignup(models.Model):
    full_name = models.CharField(max_length=200)
    work_location = models.CharField(
        max_length=500,
        help_text="Primary work area or reporting location.",
    )
    available_days = models.CharField(
        max_length=200,
        help_text="Days you are typically available (e.g. Mon–Fri).",
    )
    available_hours = models.CharField(
        max_length=200,
        help_text="Hours (e.g. 8:00 AM – 4:00 PM).",
    )
    email = models.EmailField()
    phone = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} — {self.work_location}"


class Gutter(models.Model):
    """Gutter site + sensor snapshot; city staff maintain records in Django admin."""

    site_code = models.CharField(
        max_length=64,
        unique=True,
        help_text="Sensor or asset ID (unique).",
    )
    location_description = models.CharField(max_length=500)
    cleaning_priority = models.PositiveSmallIntegerField(
        default=1,
        help_text="Higher number = higher priority to clean next.",
    )
    debris_level_percent = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text="Estimated fullness / debris from sensor (0–100).",
    )
    sensor_water_level_cm = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text="Optional water depth reading (cm).",
    )
    needs_cleaning = models.BooleanField(default=True)
    last_sensor_read_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-cleaning_priority', '-needs_cleaning', 'site_code']

    def __str__(self):
        return f"{self.site_code} — {self.location_description[:40]}"
