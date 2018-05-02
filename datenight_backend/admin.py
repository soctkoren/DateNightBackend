from django.contrib import admin
from .models import Comment, DateTag, Date, DestinationNode, FavoriteComment, FavoriteDate, FavoriteNode, FeaturedDate, Image, Node, Tag, TravelNode, UserDate
# Register your models here.

admin.site.register(Comment)
admin.site.register(DateTag)
admin.site.register(Date)
admin.site.register(DestinationNode)
admin.site.register(FavoriteComment)
admin.site.register(FavoriteDate)
admin.site.register(FavoriteNode)
admin.site.register(FeaturedDate)
admin.site.register(Image)
admin.site.register(Node)
admin.site.register(Tag)
admin.site.register(TravelNode)
admin.site.register(UserDate)
