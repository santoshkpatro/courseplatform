from django.db import models
from accounts.models import User
from categories.models import Category


class Course(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = ("published", "Published")
        DRAFT = ("draft", "Draft")
        ARCHIVED = ("archived", "Archived")

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="category_courses"
    )
    title = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
    instructor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="instructor_courses"
    )
    total_enrollments = models.IntegerField(default=0)
    total_enrollments_allowed = models.IntegerField(blank=True, null=True)
    status = models.CharField(
        max_length=10, default=Status.DRAFT, choices=Status.choices
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "courses"

    def __str__(self) -> str:
        return self.title

    @property
    def is_free(self):
        if self.price == 0:
            return True
        else:
            return False
