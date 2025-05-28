from django.test import TestCase
from .models import User, Trip

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            phone_number='1234567890'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('testpassword'))

class TripModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.trip = Trip.objects.create(
            driver=self.user,
            destination='City Center',
            departure_time='2023-10-01 10:00:00'
        )

    def test_trip_creation(self):
        self.assertEqual(self.trip.driver, self.user)
        self.assertEqual(self.trip.destination, 'City Center')

    def test_trip_user_relationship(self):
        self.trip.users.add(self.user)
        self.assertIn(self.user, self.trip.users.all())