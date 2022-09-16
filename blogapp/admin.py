from django.contrib import admin
from blogapp.models import Post,CommentModel
# Register your models here.

class CommentModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'post', 'username', 'comment', 'comment_date']
admin.site.register(CommentModel,CommentModelAdmin)


admin.site.register(Post)

