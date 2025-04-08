import logging
from django.core.management.base import BaseCommand
from octofit_tracker_app.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from django.db import connection

# Configure logging
logging.basicConfig(level=logging.INFO)

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Add detailed logging for debugging
        logging.info("Starting database population...")

        # Check database connection
        try:
            connection.ensure_connection()
            logging.info("Database connection successful.")
        except Exception as e:
            logging.error(f"Database connection failed: {e}")

        # Log deletion of existing data
        logging.info("Deleting existing data...")
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Log user creation
        logging.info("Creating users...")
        users = [
            User(email='thundergod@mhigh.edu', name='Thor'),
            User(email='metalgeek@mhigh.edu', name='Tony Stark'),
            User(email='zerocool@mhigh.edu', name='Steve Rogers'),
            User(email='crashoverride@mhigh.edu', name='Natasha Romanoff'),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner'),
        ]
        User.objects.bulk_create(users)
        logging.info(f"Users created: {[user.email for user in users]}")
        logging.info(f"User count after creation: {User.objects.count()}")

        # Create teams
        logging.info("Creating teams...")
        teams = [
            Team(name='Blue Team', members=[]),
            Team(name='Gold Team', members=[]),
        ]
        Team.objects.bulk_create(teams)
        logging.info(f"Teams created: {[team.name for team in teams]}")
        logging.info(f"Team count after creation: {Team.objects.count()}")

        # Create activities
        logging.info("Creating activities...")
        activities = [
            Activity(user=users[0], type='Cycling', duration=60),
            Activity(user=users[1], type='Crossfit', duration=120),
            Activity(user=users[2], type='Running', duration=90),
            Activity(user=users[3], type='Strength', duration=30),
            Activity(user=users[4], type='Swimming', duration=75),
        ]
        Activity.objects.bulk_create(activities)
        logging.info(f"Activities created: {[activity.type for activity in activities]}")
        logging.info(f"Activity count after creation: {Activity.objects.count()}")

        # Create leaderboard entries
        logging.info("Creating leaderboard entries...")
        leaderboard_entries = [
            Leaderboard(user=users[0], points=100),
            Leaderboard(user=users[1], points=90),
            Leaderboard(user=users[2], points=95),
            Leaderboard(user=users[3], points=85),
            Leaderboard(user=users[4], points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)
        logging.info(f"Leaderboard entries created: {[entry.user.email for entry in leaderboard_entries]}")
        logging.info(f"Leaderboard count after creation: {Leaderboard.objects.count()}")

        # Create workouts
        logging.info("Creating workouts...")
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)
        logging.info(f"Workouts created: {[workout.name for workout in workouts]}")
        logging.info(f"Workout count after creation: {Workout.objects.count()}")

        logging.info("Database population completed successfully.")
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
