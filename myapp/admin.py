from django.contrib import admin
from .models  import About,Portfolio,BlogPost,Contact

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)

admin.site.register(About, AboutAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'website', 'completed_date', 'image')
    search_fields = ('title', 'client')
    list_filter = ('completed_date',)
    ordering = ('-completed_date',)

admin.site.register(Portfolio, PortfolioAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')
    search_fields = ('title', 'author', 'content')

admin.site.register(BlogPost, BlogPostAdmin)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["first_name", "email"]

