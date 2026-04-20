class Activity:
    def __init__(self, type, duration, calories, date):
        self._type = type
        self._duration = duration
        self._calories = calories
        self._date = date

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value,(float, int)):
            raise ValueError("Duration must be a number.")
        self._duration = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Calories must be a number.")
        self._calories = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    def summary(self):
        return f"{self._type} on {self._date}: {self.duration} minutes, {self._calories} calories burned."


    def to_dict(self):
        return {'Type': self._type, 'Duration': self._duration, 'Calories': self._calories, 'Date': self._date}

    def __str__(self):
        return self.summary()

class CardioActivity(Activity):
    def __init__(self, type, duration, calories, date, distance, heartrate):
        super().__init__(type, duration, calories, date)
        self._distance = distance
        self._heartrate = heartrate

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError("Distance must be a number.")
        self._distance = value

    @property
    def heartrate(self):
        return self._heartrate

    @heartrate.setter
    def heartrate(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError("Heart rate must be a number.")
        self._heartrate = value

    def summary(self):
        return (f"{self._type} on {self._date}: {self.duration} minutes, {self._distance} distance passed, "
                f"{self._calories} calories burned, {self._heartrate} average heart rate.")

    def to_dict(self):
        return {'Type': self._type, 'Duration': self._duration, 'Calories': self._calories,
                'Date': self._date, 'Distance': self._distance, 'Heart Rate': self._heartrate}

    def __str__(self):
        return self.summary()

class RunningActivity(CardioActivity):
    def __init__(self, type, duration, calories, date, distance, heartrate, terrain):
        super().__init__(type, duration, calories, date, distance, heartrate)
        self._terrain = terrain

    @property
    def terrain(self):
        return self._terrain

    @terrain.setter
    def terrain(self, value):
        self._terrain = value

    def summary(self):
        return (f"{self._type} on {self._date}: {self.duration} minutes, {self._distance} distance passed,"
                f" {self._calories} calories burned, {self._heartrate} average heart rate"
                f" on {self._terrain} terrain.")

    def to_dict(self):
        return {'Type': self._type, 'Duration': self._duration, 'Calories': self._calories,
                'Date': self._date, 'Distance': self._distance, 'Heart Rate': self._heartrate, 'Terrain': self._terrain}

    def __str__(self):
        return self.summary()

