from dataclasses import dataclass
from typing import List
from conf.station import stations


@dataclass
class Route:
    # route: pattern represent the direction for town to town
    route: List[str]
    # latest_town: It's lastest current town for this route
    latest_town: str
    # distance: a summary number of distance for route
    distance: int = 0
    # stops: a number of stop points not include start point
    stops: int = 0

    def __init__(self, *args, **kwargs) -> None:
        self.route = kwargs["route"] if "route" in kwargs else args[0]
        self.update_route_info()
        if "distance" in kwargs:
            self.distance = kwargs["distance"]
        if "stops" in kwargs:
            self.stops = kwargs["stops"]

    def compute_distance(self, route: List[str]) -> int:
        distance = 0
        try:
            for index, town in enumerate(route):
                if index != len(route) - 1:
                    distance += stations[town]["destinations"][route[index + 1]][
                        "distance"
                    ]

            return distance
        except KeyError:
            return 0

    def update_route_info(self):
        self.latest_town = self.route[-1]
        self.stops = len(self.route) - 1
        self.distance = self.compute_distance(self.route)

    def to_directed_graph(self) -> str:
        return "-".join(self.route)
