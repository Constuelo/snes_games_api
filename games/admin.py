# games/admin.py
from django.contrib import admin
from . models import Game, Publisher, Developer
from django.utils.html import mark_safe

# @admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    readonly_fields = ["image_tag",]
    def image_tag(self, obj):
        return mark_safe('<img src="{url}" width="{width}" />'.format(
            url = obj.image.url,
            width = obj.image.width,
            )
        )

# class GameAdmin(admin.ModelAdmin):
#     fields = ( 'image_tag','title','description','image','externalURL', )
#     readonly_fields = ('image_tag',)


admin.site.register(Game, GameAdmin)
admin.site.register(Publisher)
admin.site.register(Developer)
