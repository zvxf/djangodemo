from django.contrib import admin
from blog.models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'desc', 'read_count',)
    list_display_links = ('title', 'desc',)
    list_editable = ('read_count',)
    fieldsets = (
        (None, {
            'fields': ('title', 'user', 'desc', 'body', 'read_count', 'category', 'tag')
        }),

    )


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Advert)
