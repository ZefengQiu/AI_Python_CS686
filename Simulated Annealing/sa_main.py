#!/usr/bin/python

from city import City
from sa import Annealer

import  random
import matplotlib.pyplot as plt


def main():

    fo = open("randTSP/problem36.txt", "rw+")
    City.number_of_city = int(fo.readline())
    cities = []
    city_dict = {}


    for line in fo:
        city_info = line.split()
        cities.append(City(city_info[0], city_info[1], city_info[2]))
        city_dict[city_info[0]] = (city_info[1], city_info[2])

    acity = cities[0]
    fo.close()

    random.shuffle(cities)

    #creating a distance matrix
    dis_matrix = {}
    for c1 in cities:
        dis_matrix[c1.name] = {}
        for c2 in cities:
            if c2 == c1:
                dis_matrix[c1.name][c2.name] = 0.0
            else:
                dis_matrix[c1.name][c2.name] = c1.next_distance(c2)

    init_state = []
    for c in cities:
        init_state.append(c.name)

    tsp = Annealer(init_state, dis_matrix)
    state, energy = tsp.simulate_annealling()

    while state[0] != "A":
        state = state[1:] + state[:1]   #rotate A to start
    print energy , "--length of the rout travelled"

    #plot the travelling result
    names = []
    x = []
    y = []

    for city in state:
        names.append(city)
        x.append(city_dict[city][0])
        y.append(city_dict[city][1])

    x.append(acity.x)
    y.append(acity.y)
    fig, ax = plt.subplots()
    plt.figure(1)
    plt.plot(x, y)

    for i, txt in enumerate(names):
        ax.annotate(txt, (x[i], y[i]))

    #plot for the cost and temperature curve
    plt.figure(2)
    plt.plot(tsp.x_iteration, tsp.y_cost)

    plt.figure(3)
    plt.plot(tsp.x_iteration, tsp.y_tmp)

    plt.show()


if __name__ == "__main__":
    main()