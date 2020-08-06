from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	#to display the column for admin
	list_display=['user','caption','created_on','updated_on']
	
	#for readonly fields for admin
	readonly_fields=['created_on','updated_on']
	#to use the same name as that of title
	prepopulated_fields = {"slug":("user",)}
	class meta:
		model = Post


class CommentAdmin(admin.ModelAdmin):
	list_display = ['author','text','created_on','updated_on']

	readonly_fields=['created_on','updated_on']
	class meta:
		model = Comment

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
