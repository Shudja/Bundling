from otree.api import *
import numpy as np
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Shifting_Exp_ChoiceD'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10

    ETA=15
    COMPLETION_FEE = 2.50
    EXCHANGE_RATE = 0.03
    NUM_BALLS=100
    BET_PAY=100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    urnA_H=models.IntegerField()
    urnB_H=models.IntegerField()
    urnC_H=models.IntegerField()
    urnD_H=models.IntegerField()

    urnA_L=models.IntegerField()
    urnB_L=models.IntegerField()
    urnC_L=models.IntegerField()
    urnD_L=models.IntegerField()

    state1=models.IntegerField()
    state2=models.IntegerField()
    state3=models.IntegerField()
    state4=models.IntegerField()

    safe1=models.IntegerField()
    safe2=models.IntegerField()
    safe3=models.IntegerField()
    safe4=models.IntegerField()

    first_choice1=models.IntegerField()
    first_choice2=models.IntegerField()

    second_choice1=models.IntegerField()
    second_choice2=models.IntegerField()

    green1TDrawn=models.IntegerField()
    green1BDrawn=models.IntegerField()

    green2TDrawn=models.IntegerField()
    green2BDrawn=models.IntegerField()

    bandit_payoff=models.IntegerField()


def creating_session(subsession: Subsession):

    if subsession.round_number == 1:

        #organizing urn locations
        for player in subsession.get_players():
            #payment choice
            player.participant.random_sheet = np.random.choice([i for i in range(1, 11)])
            player.random_round=int(player.participant.random_sheet)

            urnAs = [
                [90, 10],  # Adding uncertainty, compare to Base
                [85, 15],  # Reducing spread, what happens
                [95, 5],
                [60, 0],  # First Stage revealing, compare to Base, compare to prediction
                [55, 5],
                [90, 30],  # Base
                [95, 25],  # Compare to adding uncertainty one
                [85, 35],
                [80, 0],
                [100, 20],
            ]

            urnBs = [
                [80, 20],  # Adding uncertainty, compare to Base
                [70, 30],  # Reducing spread, what happens
                [85, 15],
                [50, 10],  # First Stage revealing, compare to Base, compare to prediction
                [45, 15],
                [80, 40],  # Base
                [85, 35],  # Compare to adding uncertainty one
                [75, 45],
                [70, 10],
                [90, 30],
            ]

            urnCs = [
                [60, 40],  # Adding uncertainty, compare to Base
                [75, 25],  # Reducing spread, what happens
                [65, 35],
                [40, 20],  # First Stage revealing, compare to Base, compare to prediction
                [45, 15],
                [70, 50],  # Base
                [75, 45],  # Compare to adding uncertainty one
                [65, 55],
                [50, 30],
                [70, 50],
            ]

            urnDs = [
                [50, 50],  # Adding uncertainty, compare to Base
                [50, 50],  # Reducing spread, what happens
                [50, 50],
                [30, 30],  # First Stage revealing, compare to Base, compare to prediction
                [30, 30],
                [60, 60],  # Base
                [60, 60],  # Compare to adding uncertainty one
                [60, 60],
                [40, 40],
                [60, 60],
            ]


            #randomizing urns
            seeds=np.array([1,2,3,4,5,6,7,8,9,10])
            np.random.shuffle(seeds)

            part2_urns_randomized=[]

            for i in range(len(seeds)):
                part2_urns_randomized.append([urnAs[seeds[i]-1], urnBs[seeds[i]-1], urnCs[seeds[i]-1], urnDs[seeds[i]-1]])

            player.participant.part2_urns=part2_urns_randomized


            #choosing states
            states=[]
            for sitNum in range(1,11):
                storage=[]
                if (random.random() <= 0.5):
                    storage.append(1)
                else:
                    storage.append(0)
                if (random.random() <= 0.5):
                    storage.append(1)
                else:
                    storage.append(0)
                if (random.random() <= 0.5):
                        storage.append(1)
                else:
                    storage.append(0)
                storage.append(1)
                states.append([storage[0],storage[1],storage[2],storage[3]])

            player.participant.part2_states = states



# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

class Consent_Form(Page):
    def is_displayed(self):
        return self.round_number == 1

class Instructions1(Page):
    def is_displayed(self):
        return self.round_number == 1

class Instructions2(Page):
    def is_displayed(self):
        return self.round_number == 1

class Instructions3(Page):
    def is_displayed(self):
        return self.round_number == 1

class Example(Page):
    def is_displayed(self):
        return self.round_number == 1

class Starting_Situation(Page):

    def vars_for_template(player):
        return dict(
            round_number=player.round_number,
        )

    def before_next_page(player, timeout_happened):

        safes=[[54,53,52,51],[54,53,52,51],[54,53,52,51],[54,53,52,51],[54,53,52,51],[54,53,52,51],[54,53,52,51]
               ,[54,53,52,51],[54,53,52,51],[54,53,52,51]]

        player.urnA_H = player.participant.part2_urns[player.round_number-1][0][0]
        player.urnB_H = player.participant.part2_urns[player.round_number-1][1][0]
        player.urnC_H = player.participant.part2_urns[player.round_number-1][2][0]
        player.urnD_H = player.participant.part2_urns[player.round_number-1][3][0]

        player.urnA_L = player.participant.part2_urns[player.round_number-1][0][1]
        player.urnB_L = player.participant.part2_urns[player.round_number-1][1][1]
        player.urnC_L = player.participant.part2_urns[player.round_number-1][2][1]
        player.urnD_L = player.participant.part2_urns[player.round_number-1][3][1]

        player.state1=player.participant.part2_states[player.round_number-1][0]
        player.state2=player.participant.part2_states[player.round_number-1][1]
        player.state3=player.participant.part2_states[player.round_number-1][2]
        player.state4=player.participant.part2_states[player.round_number-1][3]

        player.safe1=safes[player.round_number-1][0]
        player.safe2=safes[player.round_number-1][1]
        player.safe3=safes[player.round_number-1][2]
        player.safe4=safes[player.round_number-1][3]


class SituationFirst(Page):
    form_model = 'player'
    form_fields = ['first_choice1','first_choice2']

    def vars_for_template(player):
        return dict(
            urnA_H=player.urnA_H,
            urnB_H=player.urnB_H,
            urnC_H=player.urnC_H,
            urnD_H=player.urnD_H,
            urnA_L=player.urnA_L,
            urnB_L=player.urnB_L,
            urnC_L=player.urnC_L,
            urnD_L=player.urnD_L,
            round_number=player.round_number,
            safe1=player.safe1,
            safe2=player.safe2,
            safe3=player.safe3,
            safe4=player.safe4,
        )


    def before_next_page(player, timeout_happened):
        x=random.random()
        state=player.participant.part2_states[player.round_number-1][player.first_choice1-1]
        if state==1:
            prob=player.participant.part2_urns[player.round_number-1][player.first_choice1-1][0]
        else:
            prob=player.participant.part2_urns[player.round_number-1][player.first_choice1-1][1]
        probability=prob*.01

        if x<=probability:
            player.green1TDrawn=1
        else:
            player.green1TDrawn=0

        y=random.random()
        probabilityS=0
        if player.first_choice2==5:
            probabilityS=player.safe1*.01
        elif player.first_choice2==6:
            probabilityS=player.safe2*.01
        elif player.first_choice2==7:
            probabilityS=player.safe3*.01
        elif player.first_choice2==8:
            probabilityS=player.safe4*.01

        if y<=probabilityS:
            player.green1BDrawn=1
        else:
            player.green1BDrawn=0

class SituationSecond(Page):
    form_model = 'player'
    form_fields = ['second_choice1', 'second_choice2']

    def vars_for_template(player):
        return dict(
            urnA_H=player.urnA_H,
            urnB_H=player.urnB_H,
            urnC_H=player.urnC_H,
            urnD_H=player.urnD_H,
            urnA_L=player.urnA_L,
            urnB_L=player.urnB_L,
            urnC_L=player.urnC_L,
            urnD_L=player.urnD_L,
            round_number=player.round_number,
            green1TDrawn=player.green1TDrawn,
            first_choice1=player.first_choice1,
            first_choice2=player.first_choice2,
            safe1=player.safe1,
            safe2=player.safe2,
            safe3=player.safe3,
            safe4=player.safe4,
            green1BDrawn=player.green1BDrawn,
        )

    def before_next_page(player, timeout_happened):
        x=random.random()
        state=player.participant.part2_states[player.round_number-1][player.second_choice1-1]
        if state==1:
            prob=player.participant.part2_urns[player.round_number-1][player.second_choice1-1][0]
        else:
            prob=player.participant.part2_urns[player.round_number-1][player.second_choice1-1][1]
        probability=prob*.01

        if x<=probability:
            player.green2TDrawn=1
        else:
            player.green2TDrawn=0

        y=random.random()
        probabilityS=0
        if player.second_choice2==5:
            probabilityS=player.safe1*.01
        elif player.second_choice2==6:
            probabilityS=player.safe2*.01
        elif player.second_choice2==7:
            probabilityS=player.safe3*.01
        elif player.second_choice2==8:
            probabilityS=player.safe4*.01

        if y<=probabilityS:
            player.green2BDrawn=1
        else:
            player.green2BDrawn=0



        player.bandit_payoff=0 + player.green1TDrawn*100 + player.green1BDrawn*100 + player.green2TDrawn*100+ player.green2BDrawn*100;


class SituationResults(Page):
    def vars_for_template(player):
        return dict(
            urnA_H=player.urnA_H,
            urnB_H=player.urnB_H,
            urnC_H=player.urnC_H,
            urnD_H=player.urnD_H,
            urnA_L=player.urnA_L,
            urnB_L=player.urnB_L,
            urnC_L=player.urnC_L,
            urnD_L=player.urnD_L,
            round_number=player.round_number,
            green1TDrawn=player.green1TDrawn,
            green1BDrawn=player.green1BDrawn,
            first_choice1=player.first_choice1,
            first_choice2=player.first_choice2,

            green2TDrawn=player.green2TDrawn,
            green2BDrawn=player.green2BDrawn,
            second_choice1=player.second_choice1,
            second_choice2=player.second_choice2,

            bandit_payoff=player.bandit_payoff,
            safe1=player.safe1,
            safe2=player.safe2,
            safe3=player.safe3,
            safe4=player.safe4,
        )

    def before_next_page(player, timeout_happened):
        if player.round_number==player.participant.random_sheet:
            player.participant.Payoff1=(player.bandit_payoff)*0.03
            player.payoff=player.participant.Payoff1


class Experiment_Results(Page):
    def is_displayed(self):
        return self.round_number == 10

page_sequence = [Consent_Form, Instructions1, Instructions2, Instructions3, Example, Starting_Situation, SituationFirst, SituationSecond,
                 SituationResults, Experiment_Results]
