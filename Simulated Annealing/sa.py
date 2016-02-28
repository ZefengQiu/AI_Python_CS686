#!/usr/bin/python
import math
import random


class Annealer:

    Tmax = 200.0          #max temperature
    Tmin = 2.0              #min temperature, Tmin need > 0
    steps = 500000.00          #number of iterations, float number
    updates = 1000          #number of updates

    #for ploting
    y_cost = []
    y_tmp = []
    x_iteration = []

    def __init__(self, initial_state,  distance_matrix):
        self.distance_matrix = distance_matrix
        self.state = self.copy_state(initial_state)


    def random_neighbor(self):
        """randomly switch neighbour"""
        a = random.randint(0, len(self.state) - 1)
        b = random.randint(0, len(self.state) - 1)
        self.state[a], self.state[b] = self.state[b], self.state[a]


    def energy(self):
        """Calculates cost, which is the length of the route."""
        e = 0
        for i in range(len(self.state)):
            e += self.distance_matrix[self.state[i-1]][self.state[i]]
        return e


    def copy_state(self, state):
        return state[:]


    def report(self, T, E, step):
        self.y_cost.append(E)
        self.y_tmp.append(T)
        self.x_iteration.append(step)
        print "temperature: ", T, "     Energy: ",E


    def acception_pro_function(self, dE, T):

        return math.exp(dE / T)


    def simulate_annealling(self):

        step = 0

        #shedule 1, 1/t, which t is time

        #schedule 2
        # factor = (self.Tmin - self.Tmax)/self.Tmax

        #schedule 3
        factor = -math.log(self.Tmax / self.Tmin)

        # initial state
        T = self.Tmax
        E = self.energy()

        pre_state = self.copy_state(self.state)
        pre_energy = E
        best_state = self.copy_state(self.state)
        best_energy = E

        if self.updates > 0:
            updateWavelength = self.steps / self.updates
            self.report(T, E, step)

        # Attempt moves to new states
        while step < self.steps :
            step += 1
            #schedule 1
            # alpha = 3/float(step)

            #schedule 2
            # alpha = factor*step/self.steps + 1

            #schedule 3
            alpha =  math.exp(factor * step / self.steps)
            T = self.Tmax * alpha

            #random neighboring solution
            self.random_neighbor()

            #calculating the new solution cost
            E = self.energy()
            dE = pre_energy - E

            probobility = self.acception_pro_function(dE, T)

            if dE < 0.0 and probobility < random.random():
                # new state is worse ,restore previous state
                self.state = self.copy_state(pre_state)
                E = pre_energy
            else:
                # new state is better than the old one, accept and update the information
                pre_state = self.copy_state(self.state)
                pre_energy = E
                if E < best_energy:
                    best_state = self.copy_state(self.state)
                    best_energy = E

            if self.updates > 1:
                if step // updateWavelength > (step - 1) // updateWavelength:
                    self.report(T, E, step)



        print('\n')
        self.state = self.copy_state(best_state)
        print "final step is ", step
        return best_state, best_energy










