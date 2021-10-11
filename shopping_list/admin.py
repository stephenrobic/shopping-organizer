from django.contrib import admin
from .models import List, Item, Friends, FriendRequest


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_filter = ['name', 'price', 'checked_off']
    list_display = ['name', 'price', 'checked_off']
    search_fields = ['name', 'price', 'checked_off']
    readonly_fields = ['name', 'price', 'checked_off']

    class Meta:
        model = Item


class ListAdmin(admin.ModelAdmin):
    list_filter = ['user', 'name', 'created_on', 'updated_on', 'budget']
    list_display = ['user', 'name', 'created_on', 'updated_on', 'budget']
    search_fields = ['user', 'name', 'created_on', 'updated_on', 'budget']
    readonly_fields = ['user', 'created_on', 'updated_on']

    class Meta:
        model = List


class FriendsAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user']
    search_fields = ['user']
    readonly_fields = ['user']

    class Meta:
        model = Friends


class FriendRequestAdmin(admin.ModelAdmin):
    list_filter = ['sender', 'receiver']
    list_display = ['sender', 'receiver']
    search_fields = ['sender', 'receiver']

    class Meta:
        model = FriendRequest


admin.site.register(Item, ItemAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(Friends, FriendsAdmin)
admin.site.register(FriendRequest, FriendRequestAdmin)
