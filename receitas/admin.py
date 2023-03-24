from django.contrib import admin

from .models import Category, Receita


class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Receita)
class Receitas(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
