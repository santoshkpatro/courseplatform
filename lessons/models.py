from django.db import models
from courses.models import Course
from modules.models import Module


class Lesson(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = ("published", "Published")
        DRAFT = ("draft", "Draft")
        PROCESSING = ("processing", "Processing")
        ARCHIVED = ("archived", "Archived")

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="course_lessons"
    )
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name="module_lessons"
    )
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    is_preview_available = models.BooleanField(default=False)
    video_src = models.CharField(max_length=300, blank=True, null=True)
    status = models.CharField(
        max_length=10, default=Status.DRAFT, choices=Status.choices
    )
    order = models.IntegerField(blank=True)

    class Meta:
        db_table = "lessons"
