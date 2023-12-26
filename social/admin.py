from django.contrib import admin
from .models import  SocialMediaPlatform


# Register your models here.
@admin.register(SocialMediaPlatform)
class SocialMediaPlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_url')


from .models import SocialMediaProfile

@admin.register(SocialMediaProfile)
class SocialMediaProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'platform', 'handle', 'followers_count', 'is_verified')
    list_filter = ('platform', 'is_verified')
    search_fields = ('handle', 'user__username')


from .models import ExternalUser

@admin.register(ExternalUser)
class ExternalUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'external_id')
    search_fields = ('username',)


from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'profile', 'posted_at', 'likes_count')
    list_filter = ('profile', 'posted_at')
    search_fields = ('title', 'profile__user__username')


from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'external_user', 'created_at', 'likes_count')
    list_filter = ('post', 'created_at')
    search_fields = ('post__title', 'external_user__username')


from .models import Reply

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('comment', 'external_user', 'created_at')
    list_filter = ('comment', 'created_at')
    search_fields = ('comment__content', 'external_user__username')

from .models import Hashtag
@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name',)

from .models import SocialLink
@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'platform', 'url')
    list_filter = ('platform',)
    search_fields = ('handle', 'user__username')