from django.db import models

STATUS_CHOICES = {
    "d": "Draft",
    "p": "Published",
    "w": "Withdrawn",
}   

CATEGORIES_CHOICES = {
    "school": "School",
    "national": "National",
    "international": "International",
    "opinion": "Opinion",
    "feature": "Feature",
}

class Posts(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    categories = models.CharField(max_length=15, choices=CATEGORIES_CHOICES, default='school')
    datetime = models.DateField(null=True)
    slug = models.SlugField(default="", null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    description = models.TextField(null=True, blank=True)
    content = models.TextField(null=True)

    def __str__(self):
        return f"{self.title}"

# Create your models here.
