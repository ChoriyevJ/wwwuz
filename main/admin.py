from django.contrib import admin

from main.models import Category, Site, Statistic


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    pass


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'test_date', 'visitors_number', 'views_number')
    list_editable = ['test_date']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('statistic_type', 'site', 'title', 'visitors_number', 'from_date')


