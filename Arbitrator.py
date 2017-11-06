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
            return self.stochastic_choice()
        else:
            return self.deterministic_choice()

    #Velger ein tilfeldig behaviour
    def stochastic_choice(self):
        sum = 0
        behaviour_dict = {}

        #Går gjennom alle behaviours og lager ei dictionary med intervall
        for behave in self.bbcon.active_behaviors:
            behaviour_dict[behave] = [sum, sum+behave.priority]
            sum += behave.priority

        #Plukker eit random tall innafor intervallet
        rand = random.uniform(0, sum)
        winner = None

        #Finn riktig vinner
        for key, value in behaviour_dict.items():
            if value[1] < rand:
                winner = key
        return winner

    #Velger den med størst prioritet
    def deterministic_choice(self):
        max = self.bbcon.active_behaviors[0].priority
        winner = self.bbcon.active_behaviors[0]
        for behave in self.bbcon.active_behaviors:
            if behave.priority > max:
                max = behave.priority
                winner = behave
        return winner
