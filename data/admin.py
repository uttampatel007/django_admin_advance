from django.contrib import admin

from .models import Article, Author


#Exaample of adding action in Django-Admin

class ArticleAdmin(admin.ModelAdmin):
	list_display = [
		'title',
		'status',
		'first_word_of_title',
		'colored_name',
		]

	# list_display_links = None	(fields to highlight link for description page)
	# list_editable = ('title',) 
	# (fields to change on list view itself, list_display_links should be there)
	
	actions = ['make_published']
	list_filter = ('status',)
	
	#fields = () fields needs to be displayed
	#exclude = () fields needs to be excluded
	#ordering
	"""
	formfield_overrides = {
		models.TextField: {'widget': RichTextEditorWidget},
	}
	"""
	def make_published(self, request, queryset):
		queryset.update(status='p')
	
	make_published.short_description = "Mark selected stories as published"

#stackedInline stackes in line 
#tabularinline tables the field
class ArticleInline(admin.StackedInline):
    model = Article


class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        ArticleInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)

