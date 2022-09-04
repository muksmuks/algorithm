"""
Suppose you’re starting a radio show. You want to
reach listeners in all 50 states. You have to decide what
stations to play on to reach all those listeners. It costs
money to be on each station, so you’re trying to minimize the
number of stations you play on. You have a list of stations.
"""


#This is special kind of greedy algorithm which creates approximate solutions
# Hence called approximation algorithm

states_needed = set(["mt", "wa", "or", "id", "nv", "ut","ca", "az"])

stations = {}
stations["kfive"] = set(["ca", "az"])
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])


final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        # Entire block below finds the best station
        # ie one which covers most of the remaining states/areas
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
