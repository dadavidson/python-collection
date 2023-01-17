def number(bus_stops):
    in_bus = []
    out_bus = []
    for p in range(len(bus_stops)):
        in_bus.append(bus_stops[p][0])
        out_bus.append(bus_stops[p][1])
    
    return (abs(sum(in_bus) - sum(out_bus)))


print(number([[10,0],[3,5],[5,8]]))