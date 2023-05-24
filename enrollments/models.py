from django.db import models
from accounts.models import User
from courses.models import Course


class Enrollment(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="course_enrollments"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_enrollments"
    )
    is_active = models.BooleanField(default=True)
    enrolled_on = models.DateTimeField(blank=True, null=True)
    enrolled_valid = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "enrollments"
        unique_together = ["course", "user"]

    def __str__(self) -> str:
        return str(self.id)
