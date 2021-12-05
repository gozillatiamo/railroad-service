from typing import Callable, List
from route import Route
from itertools import chain
from conf.station import stations


def search_routes(
    start: str,
    end: str,
    maximum_distance: int = 29,
    filters: List[Callable[[Route], bool]] = None,
    loopable: bool = False,
):
    """
    start: A town of start point.
    end: A town of end point.
    maximum_distance: A limitation of distance for each route to prevent infinity loop in case
                      some of town have two ways destination, Example: D -> C, C -> D that can
                      make a route to be C-D-C-D-C-D in case of C to D or any case that has C and D
                      as a passage way to expected destination.
    filters: functions that will be conditions for filter possible routes, default filters will apply
             latest_town should be 'end' town condition.
    loopable: This flag used for allow routes result can has a end destination as a one of passage way
              example: in case C to C it can be C-E-B-C-D-C or C-D-C-E-B-C
              but the default is disable to make running time provide only routes that exclude end-destination
              as a passage-way.
    """

    if filters is None:
        filters = []

    # append the default condition (latest_town == end).
    filters.append(lambda route: route.latest_town == end)
    routes = []
    uncomplete = [Route(route=[start])]

    # Run until uncomplete is nothing.
    while len(uncomplete) != 0:
        # find next possible node
        updated_next_town = list(chain(*map(next_town, uncomplete)))
        # filter found routes with conditions.
        updated_next_town = [
            {"route": route, "completed": all(map(lambda fn: fn(route), filters))}
            for route in updated_next_town
        ]

        # completed should less than or equal maximum distance to prevent infinity loop.
        completed = [
            route["route"]
            for route in updated_next_town
            if route["completed"] and route["route"].distance <= maximum_distance
        ]

        uncomplete = [
            route["route"]
            for route in updated_next_town
            if not route["completed"] and route["route"].distance < maximum_distance
        ]

        # If loopable is allow the uncomplete will includes all of commpleted
        # to make it can found other possible route that has end-destination as a passage way.
        if loopable:
            uncomplete += completed

        routes += completed

    # sort by distance as a ascending.
    routes.sort(key=lambda route: route.distance)
    return routes


def next_town(route: Route) -> List[Route]:
    # find next possible destination
    possible_town = stations[route.latest_town]["destinations"]
    # It's can found other route that can reach the same end-destination
    return [Route(route=[*route.route, town]) for town in possible_town]


# This is for user input only
def user_input():
    print("Please provide your trip infomant.")
    start = None
    end = None

    try:

        while start not in stations:
            start = input("Please enter your start town(A,B,C,D,E): ").upper()
            if start not in stations:
                print(
                    "Incorrect town station, Please enter only one of [A, B, C, D, E]."
                )

        while end not in stations or end == start:
            end = input("Please enter your end town(A,B,C,D,E): ").upper()
            if end not in stations:
                print(
                    "Incorrect town station, Please enter only one of [A, B, C, D, E]."
                )
            elif end == start:
                print(
                    f"Your destination can't be start town, Your start town is {start}."
                )

        print(
            f"Your trip will start from {start} town and your destination is {end} town."
        )
        return start, end
    except KeyboardInterrupt:
        print("Exit.")
        return None, None


def display_route_information(routes: List[Route]):
    print(f"{len(routes)} Routes found.")

    print("======================================")
    print("Routes Information:")
    print("======================================")

    print("The Shortest Route:")
    print(f"Route Trip: {routes[0].to_directed_graph()}")
    print(f"Route Distance: {routes[0].distance}")
    print("======================================")

    if len(routes) > 1:
        print("Optional Routes:")
        print("======================================")
    for route in routes[1:]:
        print(f"Route Trip: {route.to_directed_graph()}")
        print(f"Route Distance: {route.distance}")
        print("---------------------------------------")


def main():
    print("======================================")
    print("Local Railroad Information Service")
    print("======================================")
    start, end = user_input()
    if start != None and end != None:
        routes = search_routes(start=start, end=end)
        if len(routes) == 0:
            print("NO SUCH ROUTE")
        else:
            display_route_information(routes)


if __name__ == "__main__":
    main()
