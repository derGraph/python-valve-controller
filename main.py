import matplotlib.pyplot as plt

# waterlevel at start (m)
water_level = 1
# size of the tank (m2)
tank = 4
# waterflow in the tank at the beginning (m3)
flow_in = 1
# set level (m)
set_level = 1
# waterflow out of the tank at the beginning (m3)
valve = 1
# P and I gains
p = 2
i = 4
# variable for calc
error = 0
time = 0
graph_list = []
plt.ion()
# Animation loop to 20
while time < 20:
    # at 8 the flow is changed to 1.4
    if time == 8:
        flow_in = 1.4

    # calculate valve position
    valve += (water_level - set_level) * p - (error - (water_level - set_level)) * i
    error = water_level - set_level

    # calculate new water level
    water_level = water_level + (flow_in - valve) / tank
    graph_list.append(water_level)

    # draw the graph
    plt.clf()
    plt.plot(graph_list)
    plt.title("Change of flow from 1.0 to 1.4 at 8")
    plt.ylabel("water level (m)")
    plt.xlabel("time")
    plt.pause(0.0000001)

    # increment time variable
    time += 1
# show the final graph
plt.show(block=True)
