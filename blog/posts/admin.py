from django.contrib import admin
from .models import Post

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__" , "updated" , "timestamp"]
	list_filter = ["updated" , "timestamp"]
	#Fields that can be edited in the admin page
	#list_editable = []
	search_fields = ["title" , "content"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)