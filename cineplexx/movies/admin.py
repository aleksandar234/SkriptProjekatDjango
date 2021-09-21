from django.contrib import admin
from .models import Question,Choice

admin.site.site_header = "Cineplexx"
admin.site.site_title = "Cineplexx Usce"
admin.site.index_title = "Welcome to Cineplexx"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [("Aleksandar",{'fields': ["question_text",]}),]
    inlines = [ChoiceInline]

# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin)
