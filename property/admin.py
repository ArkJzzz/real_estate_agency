from django.contrib import admin

from property.models import Flat
from property.models import Complaint
from property.models import Owner

class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner_deprecated']
    readonly_fields = ['created_at']
    list_display = [
            'town',
            'address',
            'price',
            'new_building',
            'construction_year',
            'owners_phonenumber',
            'owner_pure_phone',
        ]
    list_editable = ['new_building']
    list_filter = [
            'new_building',
            'rooms_number',
            'has_balcony',
            'floor',
        ]
    raw_id_fields = [
            'liked_by',
        ]


admin.site.register(Flat, FlatAdmin)


class ComplaintAdmin(admin.ModelAdmin):
    list_display = [
            'user',
            'flat',
            'text',
        ]
    list_editable = [
            'text',
        ]
    raw_id_fields = [
            'user',
            'flat',
        ]

admin.site.register(Complaint, ComplaintAdmin)


class OwnerAdmin(admin.ModelAdmin):
    list_display = [
            'name',
            'phonenumber',
            'pure_phone',
        ]    
    raw_id_fields = [
            'flats',
        ]

admin.site.register(Owner, OwnerAdmin)