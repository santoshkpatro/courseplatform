from django.db import models

from courses.models import Course


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_modules")
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "modules"

    def __str__(self) -> str:
        return self.title
