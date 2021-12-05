from railroad import search_routes
from route import Route


def test_distance_of_the_route_A_B_C_should_equal_9():
    route = Route(["A", "B", "C"])
    assert route.distance == 9


def test_distance_of_the_route_A_D_should_equal_5():
    route = Route(["A", "D"])
    assert route.distance == 5


def test_distance_of_the_route_A_D_C_should_equal_13():
    route = Route(["A", "D", "C"])
    assert route.distance == 13


def test_distance_of_the_route_A_E_B_C_D_should_equal_22():
    route = Route(["A", "E", "B", "C", "D"])
    assert route.distance == 22


def test_distance_of_the_route_A_E_D_should_equal_0():
    route = Route(["A", "E", "D"])
    assert route.distance == 0


def test_number_of_trips_C_to_C_with_maximum_3_stops_should_have_2_routes():
    routes = search_routes(start="C", end="C")
    actual_3_stops_maximum = [route for route in routes if route.stops <= 3]
    print(actual_3_stops_maximum)
    assert len(actual_3_stops_maximum) == 2
    assert actual_3_stops_maximum == [
        Route(route=["C", "E", "B", "C"], distance=9, stops=3),
        Route(route=["C", "D", "C"], distance=16, stops=2),
    ]


def test_number_of_trips_A_to_C_with_exactly_4_stops_should_have_3_routes():
    routes = search_routes(
        start="A",
        end="C",
        filters=[lambda route: route.stops == 4],
    )
    actual_4_stops = [route for route in routes if route.stops == 4]
    assert len(actual_4_stops) == 3
    assert actual_4_stops == [
        Route(route=["A", "D", "E", "B", "C"], distance=18, stops=4),
        Route(route=["A", "B", "C", "D", "C"], distance=25, stops=4),
        Route(route=["A", "D", "C", "D", "C"], distance=29, stops=4),
    ]


def test_shortest_distance_for_A_to_C_should_equal_9():
    routes = search_routes(start="A", end="C")
    assert routes[0].distance == 9


def test_shortest_distance_for_B_to_B_should_equal_9():
    routes = search_routes(start="B", end="B")
    assert routes[0].distance == 9


def test_number_of_routes_with_distance_less_than_30_should_equal_7():
    routes = search_routes(start="C", end="C", loopable=True)
    assert len(routes) == 7


def test_search_routes_A_to_C_should_return_correctly_routes():
    routes = search_routes(start="A", end="C")
    assert routes == [
        Route(["A", "B", "C"]),
        Route(["A", "D", "C"]),
        Route(["A", "E", "B", "C"]),
        Route(["A", "D", "E", "B", "C"]),
    ]


def test_search_routes_with_not_existence_destination_should_return_NO_SUCH_ROUTE():
    routes = search_routes(start="B", end="A")
    assert routes == []
