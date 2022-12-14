from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display= ('title', 'slug')
    search_fields= ['title']
    prepopulated_fields= {"slug": ("title",)} 

    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)




