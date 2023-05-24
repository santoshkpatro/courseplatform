from django.db import models
from accounts.models import User
from courses.models import Course


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_reviews")
    body = models.TextField()
    is_clean = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "reviews"

    def __str__(self) -> str:
        return self.body