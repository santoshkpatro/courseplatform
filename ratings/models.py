from django.db import models
from accounts.models import User
from courses.models import Course


class Rating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_ratings")
    rating = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ratings"
        unique_together = ["course", "user"]

    def __str__(self) -> str:
        return str(self.id)