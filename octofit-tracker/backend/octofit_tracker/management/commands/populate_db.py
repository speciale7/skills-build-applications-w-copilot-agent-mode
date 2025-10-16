from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from pymongo import MongoClient

# Sample data for users, teams, activities, leaderboard, and workouts
USERS = [
    {"username": "superman", "email": "superman@dc.com", "team": "team dc"},
    {"username": "batman", "email": "batman@dc.com", "team": "team dc"},
    {"username": "wonderwoman", "email": "wonderwoman@dc.com", "team": "team dc"},
    {"username": "ironman", "email": "ironman@marvel.com", "team": "team marvel"},
    {"username": "spiderman", "email": "spiderman@marvel.com", "team": "team marvel"},
    {"username": "captainmarvel", "email": "captainmarvel@marvel.com", "team": "team marvel"},
]

TEAMS = [
    {"name": "team dc", "members": ["superman", "batman", "wonderwoman"]},
    {"name": "team marvel", "members": ["ironman", "spiderman", "captainmarvel"]},
]

ACTIVITIES = [
    {"user": "superman", "activity": "flight", "duration": 60},
    {"user": "batman", "activity": "martial arts", "duration": 45},
    {"user": "ironman", "activity": "flying suit", "duration": 50},
]

LEADERBOARD = [
    {"team": "team dc", "points": 300},
    {"team": "team marvel", "points": 350},
]

WORKOUTS = [
    {"name": "strength training", "level": "advanced"},
    {"name": "cardio blast", "level": "intermediate"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
