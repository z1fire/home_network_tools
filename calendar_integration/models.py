from django.db import models
from django.utils import timezone

class CalendarEvent(models.Model):
    REPEAT_CHOICES = [
        ('NONE', 'No Repeat'),
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly'),
        ('YEARLY', 'Yearly'),
        ('CUSTOM', 'Custom'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True)
    repeat = models.CharField(max_length=10, choices=REPEAT_CHOICES, default='NONE')
    repeat_until = models.DateField(null=True, blank=True)  # End date for recurring events
    custom_repeat_interval = models.PositiveIntegerField(null=True, blank=True, help_text="Interval for custom recurrence in days.")
    custom_repeat_unit = models.CharField(max_length=10, choices=[('days', 'Days'), ('weeks', 'Weeks')], null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_occurrences(self):
        """
        Generates all occurrences of a recurring event up to the specified 'repeat_until' date.
        """
        occurrences = []
        if self.repeat == 'NONE':
            occurrences.append(self)
        else:
            current_start = self.start_time
            current_end = self.end_time
            while current_start.date() <= (self.repeat_until or timezone.now().date()):
                occurrences.append({
                    'title': self.title,
                    'start_time': current_start,
                    'end_time': current_end,
                    'description': self.description,
                    'location': self.location,
                })

                # Increment to the next occurrence based on repeat pattern
                if self.repeat == 'DAILY':
                    current_start += timezone.timedelta(days=1)
                    current_end += timezone.timedelta(days=1)
                elif self.repeat == 'WEEKLY':
                    current_start += timezone.timedelta(weeks=1)
                    current_end += timezone.timedelta(weeks=1)
                elif self.repeat == 'MONTHLY':
                    # Handle monthly increment
                    current_start = current_start.replace(month=current_start.month % 12 + 1, year=current_start.year + (current_start.month // 12))
                    current_end = current_end.replace(month=current_end.month % 12 + 1, year=current_end.year + (current_end.month // 12))
                elif self.repeat == 'YEARLY':
                    # Handle yearly increment
                    current_start = current_start.replace(year=current_start.year + 1)
                    current_end = current_end.replace(year=current_end.year + 1)
                elif self.repeat == 'CUSTOM':
                    # Handle custom increments
                    if self.custom_repeat_unit == 'days':
                        current_start += timezone.timedelta(days=self.custom_repeat_interval)
                        current_end += timezone.timedelta(days=self.custom_repeat_interval)
                    elif self.custom_repeat_unit == 'weeks':
                        current_start += timezone.timedelta(weeks=self.custom_repeat_interval)
                        current_end += timezone.timedelta(weeks=self.custom_repeat_interval)

        return occurrences
