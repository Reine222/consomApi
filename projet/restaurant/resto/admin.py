from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    list_search = ('nom')
    ordering = ('nom',)
    list_per_page = 5
    actions = ('active', 'desactive',)

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'Activer une Categorie')
    active.short_description = 'active Categorie'

    def desactive(self, queryset, request):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Categorie')
    desactive.short_description = 'desactive Categorie'



@admin.register(models.Plat)
class PlatAdmin(admin.ModelAdmin):
    list_display = ('categorie', 'nom', 'description', 'prix', 'date_add', 'date_upd', 'status', 'image',)
    list_filter = ('date_add', 'date_upd', 'status',)
    list_search = ('nom')
    ordering = ('nom',)
    list_per_page = 5
    readonly_fields = ['detail_image']
    actions = ('active', 'desactive',)

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'Activer une Plat')
    active.short_description = 'active Plat'

    def desactive(self, queryset, request):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Plat')
    desactive.short_description = 'desactive Plat'

    def view_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))

    def detail_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))




@admin.register(models.Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('nom', 'profession', 'description', 'fb', 'tweet', 'instagram', 'date_add', 'date_upd', 'status', 'image')
    list_filter = ('date_add', 'date_upd', 'status',)
    list_search = ('nom')
    ordering = ('nom',)
    list_per_page = 5
    actions = ('active', 'desactive',) 
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'Activer une Testimony')
    active.short_description = 'active Testimony'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Testimony')
    desactive.short_description = 'desactive Testimony'