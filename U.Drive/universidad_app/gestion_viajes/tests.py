from django.test import TestCase
from .models import Trip, Contact

class TripModelTest(TestCase):
    def setUp(self):
        self.trip = Trip.objects.create(
            driver_name="Juan Pérez",
            destination="Ciudad de México",
            date="2023-10-01",
            seats_available=3
        )

    def test_trip_creation(self):
        self.assertEqual(self.trip.driver_name, "Juan Pérez")
        self.assertEqual(self.trip.destination, "Ciudad de México")
        self.assertEqual(self.trip.seats_available, 3)

class ContactModelTest(TestCase):
    def setUp(self):
        self.trip = Trip.objects.create(
            driver_name="Juan Pérez",
            destination="Ciudad de México",
            date="2023-10-01",
            seats_available=3
        )
        self.contact = Contact.objects.create(
            trip=self.trip,
            phone_number="555-1234"
        )

    def test_contact_creation(self):
        self.assertEqual(self.contact.phone_number, "555-1234")
        self.assertEqual(self.contact.trip, self.trip)