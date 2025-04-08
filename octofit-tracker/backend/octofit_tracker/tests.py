from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Test Team", members=[])
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(user="test@example.com", type="running", duration=30)
        self.assertEqual(activity.type, "running")

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(user="test@example.com", points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Test Workout", description="Test Description")
        self.assertEqual(workout.name, "Test Workout")
