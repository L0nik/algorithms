def solve(stations, states_needed):

    result = set()

    while states_needed:
        best_station = None
        states_covered = set()

        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                states_covered = covered
                best_station = station

        states_needed -= states_covered
        result.add(best_station)
        
    return result


states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "са"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

result = solve(stations, states_needed)
print(result)