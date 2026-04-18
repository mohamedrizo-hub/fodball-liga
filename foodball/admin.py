from django.contrib import admin
from .models import (League, Team, Player, Match, Statistic,Coach, Stadium, Transfer, Referee, Sponsor,Training, Injury, Ticket)


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'season', 'total_teams')
    search_fields = ('name', 'country')
    list_filter = ('country', 'season')



@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'coach', 'league')
    search_fields = ('name', 'city')
    list_filter = ('league',)



@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'position', 'team')
    search_fields = ('name',)
    list_filter = ('position', 'team')



@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'home_score', 'away_score', 'date')
    list_filter = ('date',)
    search_fields = ('home_team__name', 'away_team__name')



@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('player', 'goals', 'assists', 'matches_played', 'rating')
    search_fields = ('player__name',)



@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'experience_years', 'trophies')
    search_fields = ('name',)
    list_filter = ('team',)



@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'capacity', 'team')
    search_fields = ('name', 'city')
    list_filter = ('city',)



@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('player', 'from_team', 'to_team', 'transfer_fee', 'date')
    search_fields = ('player__name',)
    list_filter = ('date',)



@admin.register(Referee)
class RefereeAdmin(admin.ModelAdmin):
    list_display = ('name', 'league', 'experience', 'rating')
    search_fields = ('name',)
    list_filter = ('league',)



@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'budget')
    search_fields = ('name',)
    list_filter = ('team',)



@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('team', 'coach', 'date', 'duration', 'intensity')
    list_filter = ('date', 'team')
    search_fields = ('team__name',)



@admin.register(Injury)
class InjuryAdmin(admin.ModelAdmin):
    list_display = ('player', 'injury_type', 'severity', 'date_injured')
    list_filter = ('severity',)
    search_fields = ('player__name',)



@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('match', 'seat_number', 'price', 'status')
    list_filter = ('status',)
    search_fields = ('seat_number', 'buyer_name')