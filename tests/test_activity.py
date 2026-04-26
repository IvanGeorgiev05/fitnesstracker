# Unit tests for the Activity, CardioActivity, and RunningActivity classes.
from unittest import TestCase, main
from activity import Activity, CardioActivity, RunningActivity


class TestActivity(TestCase):

    def setUp(self):
        self.activity = Activity("gym", 90, 400, "10.04.2026")

    def test_creation(self):
        self.assertEqual(self.activity.type, "gym")
        self.assertEqual(self.activity.duration, 90)
        self.assertEqual(self.activity.calories, 400)
        self.assertEqual(self.activity.date, "10.04.2026")

    def test_duration_setter_invalid(self):
        with self.assertRaises(ValueError):
            self.activity.duration = "sixty"

    def test_to_dict(self):
        expected = {
            "Type": "gym",
            "Duration": 90,
            "Calories": 400,
            "Date": "10.04.2026"
        }
        self.assertEqual(self.activity.to_dict(), expected)

    def test_add(self):
        other = Activity("yoga", 60, 200, "11.04.2026")
        combined = self.activity + other
        self.assertEqual(combined.duration, 150)
        self.assertEqual(combined.calories, 600)


class TestCardioActivity(TestCase):

    def setUp(self):
        self.cardio = CardioActivity("bike", 45, 300, "11.04.2026", 12.5, 140)

    def test_creation(self):
        self.assertEqual(self.cardio.type, "bike")
        self.assertEqual(self.cardio.distance, 12.5)
        self.assertEqual(self.cardio.heartrate, 140)

    def test_inheritance(self):
        self.assertIsInstance(self.cardio, Activity)

    def test_add(self):
        other = CardioActivity("swim", 30, 250, "12.04.2026", 7.5, 160)
        combined = self.cardio + other
        self.assertEqual(combined.duration, 75)
        self.assertEqual(combined.calories, 550)
        self.assertEqual(combined.distance, 20.0)
        self.assertEqual(combined.heartrate, 150)


class TestRunningActivity(TestCase):

    def setUp(self):
        self.running = RunningActivity("Running", 60, 500, "12.04.2026", 8.0, 160, "trail")

    def test_creation(self):
        self.assertEqual(self.running.terrain, "trail")
        self.assertEqual(self.running.distance, 8.0)

    def test_inheritance(self):
        self.assertIsInstance(self.running, CardioActivity)
        self.assertIsInstance(self.running, Activity)

    def test_add(self):
        other = RunningActivity("Running", 45, 350, "13.04.2026", 6.0, 150, "road")
        combined = self.running + other
        self.assertEqual(combined.duration, 105)
        self.assertEqual(combined.calories, 850)
        self.assertEqual(combined.distance, 14.0)


if __name__ == '__main__':
    main()