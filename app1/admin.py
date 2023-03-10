from django.contrib import admin
from .models import CensorVoc


@admin.action(description='Сделать первую букву заглавной')
def word_upper(modeladmin, request, queryset):
    for obj in queryset:
        word = obj.word.title()
        obj.word = word
        obj.save()


def word_lower(modeladmin, request, queryset):
    for obj in queryset:
        word = obj.word.lower()
        obj.word = word
        obj.save()
word_lower.short_description = 'Сделать все буквы строчными'


class CensorVocAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'len_word')
    list_filter = ('word', )
    actions = [word_upper, word_lower]


admin.site.register(CensorVoc, CensorVocAdmin)
# admin.site.unregister(CensorVoc)

