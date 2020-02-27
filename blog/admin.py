from django.contrib import admin

# Register your models here.

from blog.models import Goods, UrlList, OAuthUser, Category

from django.contrib import admin

# class OAuthUserAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(OAuthUser, OAuthUserAdmin)
admin.site.register(Goods)
admin.site.register(UrlList)
admin.site.register(Category)
