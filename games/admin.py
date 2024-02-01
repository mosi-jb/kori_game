from django.contrib import admin

from games.models import Category, Game

# Register your models here.


admin.site.register(Category)


@admin.register(Game)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    prepopulated_fields = {"slug": ("title",)}
