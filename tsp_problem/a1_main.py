#!/usr/bin/python

from city import City
from ai import AI
import matplotlib.pyplot as plt


def run_instance(instance_num):

    #change the number after randTSP to switch to different number of cities graph

    fo = open("randTSP/15/instance_%s.txt"%instance_num, "rw+")
    # fo = open("randTSP/problem36.txt", "rw+")

    number_of_city = int(fo.readline())
    cities = []

    #prepare data for a star algorithm
    for line in fo:
        city_info = line.split()
        cities.append(City(city_info[0], city_info[1], city_info[2]))

    fo.close()

    # performing A* Search Algorithm, starting from the first node -- city A
    astar = AI(cities)

    result = astar.perfroming_AI()

    #plot the result
    fig, ax = plt.subplots()
    x = []
    y = []
    names = []

    for r in result:
        print r.name
        x.append(r.x)
        y.append(r.y)
        names.append(r.name)

    ttl = str(AI.node_expand) + " nodes have expended"
    print "result is ----------> ",AI.node_expand, "<----------"

    plt.title(ttl)
    plt.plot(x, y)

    for i, txt in enumerate(names):
        ax.annotate(txt, (x[i], y[i]))

    plt.show()



def main():

    #change the instance number in here
    run_instance(2)


if __name__ == "__main__":
    main()



