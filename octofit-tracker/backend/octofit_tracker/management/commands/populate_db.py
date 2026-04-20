from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Teams
        teams = [
            {"name": "Team Marvel"},
            {"name": "Team DC"}
        ]
        team_ids = db.teams.insert_many(teams).inserted_ids

        # Users
        users = [
            {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "Team Marvel"},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Team Marvel"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "Team DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "Team DC"}
        ]
        db.users.insert_many(users)
        db.users.create_index([("email", 1)], unique=True)

        # Activities
        activities = [
            {"user": "Spider-Man", "activity": "Running", "duration": 30},
            {"user": "Iron Man", "activity": "Cycling", "duration": 45},
            {"user": "Wonder Woman", "activity": "Swimming", "duration": 60},
            {"user": "Batman", "activity": "Yoga", "duration": 40}
        ]
        db.activities.insert_many(activities)

        # Workouts
        workouts = [
            {"user": "Spider-Man", "workout": "Push-ups", "reps": 50},
            {"user": "Iron Man", "workout": "Sit-ups", "reps": 40},
            {"user": "Wonder Woman", "workout": "Squats", "reps": 60},
            {"user": "Batman", "workout": "Pull-ups", "reps": 30}
        ]
        db.workouts.insert_many(workouts)

        # Leaderboard
        leaderboard = [
            {"user": "Spider-Man", "points": 120},
            {"user": "Iron Man", "points": 110},
            {"user": "Wonder Woman", "points": 130},
            {"user": "Batman", "points": 100}
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
