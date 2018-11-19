from django.contrib import admin

from .models import Section, Reading, Question


class ReadingAdmin(admin.ModelAdmin):
    list_display = ('heading', 'marked')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'marked')


admin.site.register(Section)
admin.site.register(Reading, ReadingAdmin)
admin.site.register(Question, QuestionAdmin)
