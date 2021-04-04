from django.contrib import admin
from .models import List

class ListAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'URL', 'published')
	list_display_links = ('title', 'content')
	search_fields = ('title', 'content', )

admin.site.register (List, ListAdmin)
