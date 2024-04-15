from django.contrib import admin
from .models import MonthlyIssues, Page
# Register your models here.

class PageAdmin(admin.StackedInline):
    model = Page

class MonthlyIssueAdmin(admin.ModelAdmin):
    # list_display = ("title", "volume", "issue",)
    # prepopulated_fields = {"slug": ("volume", "issue", "title")}
    inlines = [PageAdmin]

    class Meta:
        model = MonthlyIssues


admin.site.register(Page)
admin.site.register(MonthlyIssues, MonthlyIssueAdmin)

