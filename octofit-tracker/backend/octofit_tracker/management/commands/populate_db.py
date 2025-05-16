from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Test data for users
        users = [
            {"email": "john.doe@example.com", "name": "John Doe", "age": 16},
            {"email": "jane.smith@example.com", "name": "Jane Smith", "age": 17},
        ]
        db.users.insert_many(users)

        # Test data for teams
        teams = [
            {"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]},
        ]
        db.teams.insert_many(teams)

        # Test data for activities
        activities = [
            {"user": "john.doe@example.com", "type": "running", "duration": 30},
            {"user": "jane.smith@example.com", "type": "cycling", "duration": 45},
        ]
        db.activity.insert_many(activities)

        # Test data for leaderboard
        leaderboard = [
            {"user": "john.doe@example.com", "points": 100},
            {"user": "jane.smith@example.com", "points": 120},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Test data for workouts
        workouts = [
            {"name": "Morning Run", "description": "A 5km run to start the day"},
            {"name": "Evening Yoga", "description": "Relaxing yoga session"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
