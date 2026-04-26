#Module containing the Activity, CardioActivity and RunningActivity classes
class Activity:
    """Represents a fitness activity"""

    def __init__(self, type, duration, calories, date):
        """Initializes an activity with type, duration., calories and date"""
        self._type = type
        self._duration = duration
        self._calories = calories
        self._date = date

    @property
    def type(self):
        """Returns the activity type"""
        return self._type

    @type.setter
    def type(self, value):
        """Sets the activity type"""
        self._type = value

    @property
    def duration(self):
        """Returns the duration in minutes"""
        return self._duration

    @duration.setter
    def duration(self, value):
        """Sets the duration, raises ValueError if not a number"""
        if not isinstance(value, (float, int)):
            raise ValueError("Duration must be a number.")
        self._duration = value

    @property
    def calories(self):
        """Returns the calories burned"""
        return self._calories

    @calories.setter
    def calories(self, value):
        """Sets the calories, raises ValueError if not a number"""
        if not isinstance(value, (int, float)):
            raise ValueError("Calories must be a number.")
        self._calories = value

    @property
    def date(self):
        """Retyurns the date of the activity"""
        return self._date

    @date.setter
    def date(self, value):
        """Sets the date of the activity"""
        self._date = value

    def __add__(self, other):
        """Adds two activities together, combining duration and calories"""
        return Activity("Combined", self._duration + other.duration,
                        self._calories + other.calories, self._date)

    def summary(self):
        """Returns a formatted string summarizing the activity"""
        return (f"{self._type} on {self._date}: {self.duration} minutes,"
                f" {self._calories} calories burned.")

    def to_dict(self):
        """Converts the activity to a dictionary"""
        return {'Type': self._type, 'Duration': self._duration,
                'Calories': self._calories, 'Date': self._date}

    def __str__(self):
        """Returns the string representation of the activity"""
        return self.summary()


class CardioActivity(Activity):
    """Represents a cardio activity with distance and heart rate"""

    def __init__(self, type, duration, calories, date, distance, heartrate):
        """Initializes a cardio activity with distance and heart rate
           on top of the Activity class's attributes"""
        super().__init__(type, duration, calories, date)
        self._distance = distance
        self._heartrate = heartrate

    @property
    def distance(self):
        """Returns the distance in km"""
        return self._distance

    @distance.setter
    def distance(self, value):
        """Sets the distance, raises ValueError if not a number"""
        if not isinstance(value, (float, int)):
            raise ValueError("Distance must be a number.")
        self._distance = value

    @property
    def heartrate(self):
        """Returns the average heart rate"""
        return self._heartrate

    @heartrate.setter
    def heartrate(self, value):
        """Sets the heart rate, raises ValueError if not a number"""
        if not isinstance(value, (float, int)):
            raise ValueError("Heart rate must be a number.")
        self._heartrate = value

    def __add__(self, other):
        """Adds two cardio activities, combining distance
           and averaging heart rate"""
        avg_hr = (self._heartrate + other.heartrate) // 2
        return CardioActivity("Combined", self._duration + other.duration,
                              self._calories + other.calories, self._date,
                              self._distance + other.distance, avg_hr)

    def summary(self):
        """Returns a formatted string summarizing the cardio activity"""
        return (f"{self._type} on {self._date}: {self.duration} minutes, "
                f"{self._distance} distance passed,"
                f"{self._calories} calories burned,"
                f" {self._heartrate} average heart rate.")

    def to_dict(self):
        """Converts the cardio activity to a dictionary"""
        return {'Type': self._type, 'Duration': self._duration,
                'Calories': self._calories,
                'Date': self._date, 'Distance': self._distance,
                'Heart Rate': self._heartrate}

    def __str__(self):
        """Returns the string representation of the cardio activity"""
        return self.summary()


class RunningActivity(CardioActivity):
    """Represents a running activity with terrain type"""
    def __init__(self, type, duration, calories, date,
                 distance, heartrate, terrain):
        """Initializes a running activity with terrain
         on top of CardioActivity class's attributes"""
        super().__init__(type, duration, calories, date, distance, heartrate)
        self._terrain = terrain

    @property
    def terrain(self):
        """Returns the terrain type"""
        return self._terrain

    @terrain.setter
    def terrain(self, value):
        """Sets the terrain type"""
        self._terrain = value

    def __add__(self, other):
        """Adds two running activities, combining all attributes"""
        avg_hr = (self._heartrate + other.heartrate) // 2
        return RunningActivity("Combined", self._duration + other.duration,
                               self._calories + other.calories,
                               self._date, self._distance + other.distance,
                               avg_hr, self._terrain)

    def summary(self):
        """Returns a formatted string summarizing the running activity"""
        return (f"{self._type} on {self._date}: {self.duration} minutes,"
                f" {self._distance} distance passed,"
                f" {self._calories} calories burned,"
                f" {self._heartrate} average heart rate"
                f" on {self._terrain} terrain.")

    def to_dict(self):
        """Converts the running activity to a dictionary"""
        return {'Type': self._type, 'Duration': self._duration,
                'Calories': self._calories,
                'Date': self._date, 'Distance': self._distance,
                'Heart Rate': self._heartrate, 'Terrain': self._terrain}

    def __str__(self):
        """Returns the string representation of the running activity"""
        return self.summary()
