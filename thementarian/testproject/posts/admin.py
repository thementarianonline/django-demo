from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth import get_permission_codename

from .models import Posts

# @admin.action(description="Mark selected stories as published")
# def make_published(modeladmin, request, queryset):
#     queryset.update(status="p")
# make_published.allowed_permissions = ('change',)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ("title", "categories", "datetime", "author", "status",)
    prepopulated_fields = {"slug": ("title",)}
    actions = ["make_published", "make_draft"]

    @admin.action(permissions=["publish"])
    def make_published(self, request, queryset):
        queryset.update(status="p")

    @admin.action(permissions=["draft"])
    def make_draft(self, request, queryset):
        queryset.update(status="d")

    def has_draft_permission(self, request):
        """Does the user have the draft permission?"""
        opts = self.opts
        codename = get_permission_codename("draft", opts)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename))

    def has_publish_permission(self, request):
        """Does the user have the publish permission?"""
        opts = self.opts
        codename = get_permission_codename("publish", opts)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename))

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['status'].disabled = True
        return form



admin.site.register(Posts, PostAdmin)# Register your models here.
