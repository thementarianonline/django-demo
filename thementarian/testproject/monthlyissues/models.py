from django.db import models

# Create your models here.
class MonthlyIssues(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to="thumbnail")
    volume = models.IntegerField(null=True)
    issue_no = models.IntegerField(null=True)
    date = models.DateField(null=True)
    slug = models.SlugField(default="", null=False)
 
    def __str__(self):
        return f"{self.title}"

class Page(models.Model):
    monthlyissue = models.ForeignKey(MonthlyIssues, on_delete=models.CASCADE, related_name='Pages')
    page = models.ImageField(upload_to ='file')




# Create your models here.
