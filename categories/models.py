from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "categories"

    def __str__(self) -> str:
        return self.title