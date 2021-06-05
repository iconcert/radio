from django.contrib import admin
from .models import List
from .models import Services

class ListAdmin(admin.ModelAdmin):
	list_display = ('title', 'ganre', 'URL', 'published')
	list_display_links = ('title', 'ganre')
	search_fields = ('title', 'ganre', )

class ServicesAdmin(admin.ModelAdmin):
	list_display = ('title', 'typeservices', 'content', 'price', 'published')
	list_display_links = ('title', 'typeservices')
	search_fields = ('title', 'typeservices', )

admin.site.register (List, ListAdmin)
admin.site.register (Services, ServicesAdmin)
