class NationalPark:
    _all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) < 3:
            raise Exception("Name must be at least 3 characters")
        self._name = name
        NationalPark._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise Exception("Cannot change national park name")
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) < 3:
            raise Exception("Name must be at least 3 characters")
        self._name = value

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        return list(set(trip.visitor for trip in self.trips()))

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        if not self.trips():
            return None
        visitor_counts = {}
        for trip in self.trips():
            visitor = trip.visitor
            visitor_counts[visitor] = visitor_counts.get(visitor, 0) + 1
        return max(visitor_counts.items(), key=lambda x: x[1])[0] if visitor_counts else None

    @classmethod
    def most_visited(cls):
        if not cls._all:
            return None
        park_visits = {park: park.total_visits() for park in cls._all}
        return max(park_visits.items(), key=lambda x: x[1])[0] if any(park_visits.values()) else None


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(visitor, Visitor):
            raise Exception("Visitor must be a Visitor instance")
        if not isinstance(national_park, NationalPark):
            raise Exception("NationalPark must be a NationalPark instance")
        self._visitor = visitor
        self._national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str):
            raise Exception("Start date must be a string")
        if len(value) < 7:
            raise Exception("Start date must be at least 7 characters")
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str):
            raise Exception("End date must be a string")
        if len(value) < 7:
            raise Exception("End date must be at least 7 characters")
        self._end_date = value

    @property
    def visitor(self):
        return self._visitor

    @property
    def national_park(self):
        return self._national_park


class Visitor:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if not 1 <= len(name) <= 15:
            raise Exception("Name must be between 1 and 15 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise Exception("Name must be between 1 and 15 characters")
        self._name = value

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self):
        return list(set(trip.national_park for trip in self.trips()))

    def total_visits_at_park(self, park):
        if not isinstance(park, NationalPark):
            raise Exception("Must be a NationalPark instance")
        return len([trip for trip in self.trips() if trip.national_park == park])