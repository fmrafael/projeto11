from django.contrib import admin
from django.forms import Textarea
from django.db import models

# Register your models here.
from .models import Post, TableAffiliate

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created","updated")
    list_filter = ("status",)
    prepopulated_fields = {"slug":("title",)}

@admin.register(TableAffiliate)
class TableAffiliateAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    list_display = ("name_affiliate","author")
  