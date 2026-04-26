# Unit tests for the file handler functions.
import os
from unittest import TestCase, main
from activity import Activity, CardioActivity, RunningActivity
from file_handler import write_json, read_json, dict_to_obj


class TestFileHandler(TestCase):

    def setUp(self):
        self.backup = None
        if os.path.exists("data.json"):
            with open("data.json", "r") as f:
                self.backup = f.read()

    def tearDown(self):
        if self.backup is not None:
            with open("data.json", "w") as f:
                f.write(self.backup)
        elif os.path.exists("data.json"):
            os.remove("data.json")

    def test_write_and_read(self):
        if os.path.exists("data.json"):
            os.remove("data.json")

        activity = Activity("gym", 90, 400, "10.04.2026")
        write_json(activity)
        data = read_json()

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["Type"], "gym")

    def test_dict_to_obj(self):
        data = [
            {"Type": "gym", "Duration": 90, "Calories": 400, "Date": "10.04.2026"},
            {"Type": "bike", "Duration": 45, "Calories": 300,
             "Date": "11.04.2026", "Distance": 12.5, "Heart Rate": 140}
        ]
        objects = dict_to_obj(data)

        self.assertEqual(len(objects), 2)
        self.assertIsInstance(objects[0], Activity)
        self.assertIsInstance(objects[1], CardioActivity)


if __name__ == '__main__':
    main()