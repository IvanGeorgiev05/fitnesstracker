# Module for reading and writing activity data to JSON files.
import json
import configparser
from activity import Activity, CardioActivity, RunningActivity

config = configparser.ConfigParser()
config.read("config.ini")

filename = config["SETTINGS"]["filename"]


def write_json(activity):
    """Writes an activity to the JSON file"""
    try:
        data = read_json()
        data.append(activity.to_dict())

        with open(filename, "w") as file:
            json.dump(data, file, indent=2)

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open(filename, "w") as file:
            json.dump([activity.to_dict()], file, indent=2)


def read_json():
    """Reads and returns data from the JSON file"""
    with open(filename, "r") as file:
        data = json.load(file)

    return data


def dict_to_obj(data):
    """Converts a list of dictionaries to activity objects"""
    objects = []

    for i in data:
        if "Terrain" in i:
            obj = RunningActivity(i["Type"], i["Duration"],
                                  i["Calories"], i["Date"], i["Distance"],
                                  i["Heart Rate"], i["Terrain"])
            objects.append(obj)
        elif "Distance" in i:
            obj = CardioActivity(i["Type"], i["Duration"],
                                 i["Calories"], i["Date"], i["Distance"],
                                 i["Heart Rate"])
            objects.append(obj)
        else:
            obj = Activity(i["Type"], i["Duration"], i["Calories"], i["Date"])
            objects.append(obj)

    return objects
