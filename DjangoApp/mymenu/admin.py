from django.contrib import admin
from .models import MenuItems, OtherMenuItems


class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')
    list_filter = ('name', 'parent', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(MenuItems, MenuItemsAdmin)


class OtherMenuItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')
    list_filter = ('name', 'parent', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(OtherMenuItems, OtherMenuItemsAdmin)
