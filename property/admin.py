from django.contrib import admin

from property.models import Flat


class FlatAdmin(admin.ModelAdmin):
	search_fields = ['town', 'address', 'owner']
	readonly_fields = ['created_at']
	list_display = [
			'town',
			'address',
			'price',
			'new_building',
			'construction_year',
		]
	list_editable = ['new_building']


admin.site.register(Flat, FlatAdmin)
