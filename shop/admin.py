from django.contrib import admin
from shop.models import Category, Krasofkalar 

# Register your models here.

class KrasofkaAdmin(admin.ModelAdmin):
    list_display = ('name', 'old_price', 'price','image','category')
    list_display_links = ('name',)
    search_fields = ('name', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Krasofkalar,KrasofkaAdmin)