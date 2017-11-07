import random

#Returnerer ein vinner basert på aktive behaviours i bbcon
class Arbitrator():

    #Stoch --> boolean som bestemmer kva ein skal ta hensyn til når ein skal velge mellom behaviours
    def __init__(self, bbcon, stoch):
        self.bbcon = bbcon
        self.stoch = stoch

    #Velger om ein skal velge med hensyn til vekt eller stokastisk
    def choose_action(self):
        if self.stoch:
            return self.stochastic()
        else:
            return self.deterministic()


    #Velger den med størst prioritet
    def deterministic(self):
        maximum = self.bbcon.active_behaviors[0].priority
        winner = self.bbcon.active_behaviors[0]
        for behave in self.bbcon.active_behaviors:
            if behave.priority > maximum:
                maximum = behave.priority
                winner = behave
        return winner

    # Velger ein tilfeldig behaviour
    def stochastic(self):
        sum = 0
        behaviour_dict = {}

        #B1: [0, 0.8), B2: [0.8, 1.3) osv
        for behave in self.bbcon.active_behaviors:
            behaviour_dict[behave] = [sum, sum + behave.priority]
            sum += behave.priority

        rand = random.uniform(0, sum)
        winner = None

        # Finn riktig vinner
        for key, value in behaviour_dict.items():
            if value[1] < rand:
                winner = key
        return winner
