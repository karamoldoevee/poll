from django.contrib import admin
from webapp.models import Poll, Choice

class ChoiceAdmin(admin.TabularInline):
    model = Choice
    fields = ['choice_text']
    extra = 0

class PollAdmin(admin.ModelAdmin):
    list_display = ['pk', 'question', 'created_at']
    list_filter = ['question']
    list_display_links = ['pk', 'question']
    search_fields = ['question']
    exclude = []
    readonly_fields = ['created_at']
    inlines = [ChoiceAdmin]

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
