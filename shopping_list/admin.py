from django.contrib import admin
from .models import List, Item


# Register your models here.
class ListAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'updated_on',)


admin.site.register(List, ListAdmin)
admin.site.register(Item)

