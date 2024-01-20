from django.contrib import admin
from . import models 

# Register your models here.
# admin.site.register(models.BlogModel)
# admin.site.register(models.Category)
@admin.register(models.BlogModel)
class blog_model(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'content',
        'published',
        'description',
        'date',
    )

    empty_value_display = "vide"
    list_editable = ('slug','content','published')
    list_display_links=('date',)
    search_fields =('title','content')
    list_filter = ('published','date')