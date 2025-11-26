from dataclasses import dataclass
from datetime import date
from typing import List

class ParalympicEvent:
    """ Represents a Paralympic event

     Attributes:
         name: A string representing the name of the event
         sport: An integer representing the sport that the event belongs to
         classification: An integer representing the event classification
         athletes: A list of strings representing the athletes that compete in the event

     Methods:
         describe() Prints a description of the event
         register_athlete() Adds an athlete to the list of athletes

     """

    def __init__(self, name, sport, classification):
        self.name = name
        self.sport = sport
        self.classification = classification
        self.athletes = []  # Empty list to hold athlete names

    def describe(self):
        """ Describes the event """
        print(f"{self.name} is a {self.sport} event for classification {self.classification}.")
        print("Athletes competing:", ", ".join(self.athletes))

    def register_athlete(self, athlete_name):
        """ Register the athlete with the event

        Args:
            athlete_name: A string representing the name of the athlete
        """
        self.athletes.append(athlete_name)


@dataclass
class Medal:
    type: str
    design: str
    date_designed: date


class Athlete:
    def __init__(self, first_name: str, last_name: str, team_code: str, disability_class: str, medals: List[Medal]):
        self.first_name = first_name
        self.last_name = last_name
        self.team_code = team_code
        self.disability_class = disability_class
        self.medals = medals  # Composition: Athlete has Medals

    def introduce(self):
        print(f"{self.first_name} {self.last_name} represents {self.team_code} in class {self.disability_class}. Has medals: {self.medals}")

# Subclass
class Runner(Athlete):
    def __init__(self, first_name, last_name, team_code, disability_class, distance):
        super().__init__(first_name, last_name, team_code, disability_class)
        self.distance = distance  # e.g., 100m, 400m

    def race_info(self):
        print(f"{self.first_name} is running the {self.distance} race.")

#1
event = ParalympicEvent(
    name="Men's individual BC1",
    sport="Boccia",
    classification="BC1",
)

# event.describe()  # Should print the event description, "Athletes competing" will be empty
# event.register_athlete("Sungjoon Jung")  # should register the athlete
# event.describe()  # Should print the event again, "Athletes competing" should include Sungjoon Jung

# athlete1 = Athlete(
#     first_name="Sungjoon Jung",
#     last_name="Jung",
#     team_code="South Korea",
#     disability_class="BC1"
# )
# athlete1.introduce()

#2
# Example usage
# runner1 = Runner("Li", "Na", "CHN", "T12", "100m")
# runner1.introduce()  # Inherited method
# runner1.race_info()  # Subclass-specific method

# Create medals
medal1 = Medal("gold", "Paris 2024 design", date(2023, 7, 1))
medal2 = Medal("silver", "Tokyo 2020 design", date(2019, 8, 25))

# Create an athlete with medals
athlete = Athlete(
    first_name="Wei",
    last_name="Wang",
    team_code="CHN",
    disability_class="T54",
    medals=[medal1, medal2]
)

athlete.introduce()