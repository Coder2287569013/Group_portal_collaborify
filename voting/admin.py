from django.contrib import admin
from .models import Voting, Choice, Vote

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'creator', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    inlines = [ChoiceInline]

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('voting', 'choice', 'user', 'created_at')
    list_filter = ('created_at',)
