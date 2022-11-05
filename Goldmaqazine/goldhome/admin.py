from django.contrib import admin

from .models import Gold,Category,Tag,Contact,Carusel
from django.utils.safestring import mark_safe




class GoldAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category','post_title','probe','weight','price','get_photo','creded_at','creded_up','public')
    search_fields = ('title',)
    list_display_links = ('id','title')
    list_editable = ('public',)
    list_filter = ('public','category','title')



    def get_photo(self, object):
        return  mark_safe(f"<img src = '{object.image.url}' width=40>")

    get_photo.short_description = 'Sekiller'

admin.site.register(Gold,GoldAdmin)




class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','post_title')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Category,CategoryAdmin)




class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Tag,TagAdmin)




class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','message','date_at')
    search_fields = ('name','email')
    list_display_links = ('id','name')

admin.site.register(Contact,ContactAdmin)




class CaruselAdmin(admin.ModelAdmin):
    list_display = ('id','name','content','get_photo','price','creded_at','public')
    search_fields = ('name',)
    list_display_links = ('id','name')
    list_editable = ('public',)



    def get_photo(self, object):
        return  mark_safe(f"<img src = '{object.image.url}' width=70>")

    get_photo.short_description = 'Carusel_Sekilleri'

admin.site.register(Carusel,CaruselAdmin)