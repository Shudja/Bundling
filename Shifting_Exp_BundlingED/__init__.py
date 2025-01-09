from otree.api import *
import numpy as np
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Shifting_Exp_BundlingED'
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

    first_choice=models.IntegerField()
    second_choice=models.IntegerField()

    green1TDrawn=models.IntegerField()
    green1BDrawn=models.IntegerField()

    green2TDrawn=models.IntegerField()
    green2BDrawn=models.IntegerField()

    bandit_payoff=models.IntegerField()

    Question1Correct1=models.IntegerField(initial=-1000)
    Question1Correct2=models.IntegerField(initial=-1000)

    Question2Correct1=models.IntegerField(initial=-1000)
    Question2Correct2=models.IntegerField(initial=-1000)

    Question3Correct1=models.IntegerField(initial=-1000)
    Question3Correct2=models.IntegerField(initial=-1000)

    Return=models.IntegerField(initial=0)



def creating_session(subsession: Subsession):

    if subsession.round_number == 1:

        #organizing urn locations
        for player in subsession.get_players():
            #payment choice
            player.participant.random_sheet = np.random.choice([i for i in range(1, 11)])
            player.random_round=int(player.participant.random_sheet)
            urnAs = [
                [90, 10],  # Adding uncertainty, compare to Base
                [90, 30],  # Reducing spread, what happens
                [70, 10],
                [100, 40],  # First Stage revealing, compare to Base, compare to prediction
                [60, 0],
                [100, 20],  # Base
                [80, 0],  # Compare to adding uncertainty one
                [70, 0],
                [100, 30],
                [100, 0],
            ]

            urnBs = [
                [80, 20],  # Adding uncertainty, compare to Base
                [80, 40],  # Reducing spread, what happens
                [60, 20],
                [90, 50],  # First Stage revealing, compare to Base, compare to prediction
                [50, 10],
                [90, 30],  # Base
                [70, 10],  # Compare to adding uncertainty one
                [60, 10],
                [90, 40],
                [75, 25],
            ]

            urnCs = [
                [70, 30],  # Adding uncertainty, compare to Base
                [70, 50],  # Reducing spread, what happens
                [50, 30],
                [80, 60],  # First Stage revealing, compare to Base, compare to prediction
                [40, 20],
                [80, 40],  # Base
                [60, 20],  # Compare to adding uncertainty one
                [50, 20],
                [80, 50],
                [65, 35],
            ]

            urnDs = [
                [60, 40],  # Adding uncertainty, compare to Base
                [60, 60],  # Reducing spread, what happens
                [40, 40],
                [70, 70],  # First Stage revealing, compare to Base, compare to prediction
                [30, 30],
                [70, 50],  # Base
                [50, 30],  # Compare to adding uncertainty one
                [40, 30],
                [70, 60],
                [50, 50],
            ]
            #randomizing urns
            # seeds=np.array([2,3,4,5,6,7,8,9])
            # np.random.shuffle(seeds)

            seeds=np.array([1,2,3,4,5,6,7,8,9,10])
            np.random.shuffle(seeds)

            part2_urns_randomized=[]

            # part2_urns_randomized.append([urnAs[0], urnBs[0], urnCs[0], urnDs[0]])

            for i in range(len(seeds)):
                part2_urns_randomized.append([urnAs[seeds[i]-1], urnBs[seeds[i]-1], urnCs[seeds[i]-1], urnDs[seeds[i]-1]])

            # part2_urns_randomized.append([urnAs[9], urnBs[9], urnCs[9], urnDs[9]])


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
                if (random.random() <= 0.5):
                    storage.append(1)
                else:
                    storage.append(0)
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
    form_model = 'player'
    form_fields = ['Question1Correct1']


    def is_displayed(player):
        return player.round_number == 1

class Instructions2F(Page):
    form_model = 'player'
    form_fields = ['Question1Correct2']


    def is_displayed(player):
        return (player.round_number == 1) & (player.Question1Correct1 == 0)

    def before_next_page(player, timeout_happened):
        if (player.Question1Correct1==0)& (player.Question1Correct2==0):
            player.Return=1


class Instructions3(Page):
    form_model = 'player'
    form_fields = ['Question2Correct1']

    def is_displayed(player):
        return (player.round_number == 1) & (player.Return==0)


class Instructions3F(Page):
    form_model = 'player'
    form_fields = ['Question2Correct2']

    def is_displayed(player):
        return (player.round_number == 1) & (player.Question2Correct1 == 0) & (player.Return==0)

    def before_next_page(player, timeout_happened):
        if (player.Question2Correct1==0)& (player.Question2Correct2==0):
            player.Return=1

class Instructions4(Page):
    form_model = 'player'
    form_fields = ['Question3Correct1']

    def is_displayed(player):
        return (player.round_number == 1) & (player.Return==0)

class Instructions4F(Page):
    form_model = 'player'
    form_fields = ['Question3Correct2']

    def is_displayed(player):
        return (player.round_number == 1) & (player.Question3Correct1 == 0) & (player.Return==0)

    def before_next_page(player, timeout_happened):
        if (player.Question3Correct1==0)& (player.Question3Correct2==0):
            player.Return=1

class PleaseReturn(Page):
    def is_displayed(player):
        return (player.round_number == 1) & (player.Return==1)


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
    form_fields = ['first_choice']

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
        state=player.participant.part2_states[player.round_number-1][player.first_choice-1]
        if state==1:
            prob=player.participant.part2_urns[player.round_number-1][player.first_choice-1][0]
        else:
            prob=player.participant.part2_urns[player.round_number-1][player.first_choice-1][1]
        probability=prob*.01

        if x<=probability:
            player.green1TDrawn=1
        else:
            player.green1TDrawn=0

        y=random.random()
        probabilityS=0
        if player.first_choice==1:
            probabilityS=player.safe1*.01
        elif player.first_choice==2:
            probabilityS=player.safe2*.01
        elif player.first_choice==3:
            probabilityS=player.safe3*.01
        elif player.first_choice==4:
            probabilityS=player.safe4*.01

        if y<=probabilityS:
            player.green1BDrawn=1
        else:
            player.green1BDrawn=0


class InitialFeedback(Page):
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
            first_choice=player.first_choice,
            safe1=player.safe1,
            safe2=player.safe2,
            safe3=player.safe3,
            safe4=player.safe4,
            green1BDrawn=player.green1BDrawn,
        )


class SituationSecond(Page):
    form_model = 'player'
    form_fields = ['second_choice']

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
            first_choice=player.first_choice,
            safe1=player.safe1,
            safe2=player.safe2,
            safe3=player.safe3,
            safe4=player.safe4,
            green1BDrawn=player.green1BDrawn,
        )

    def before_next_page(player, timeout_happened):
        x=random.random()
        state=player.participant.part2_states[player.round_number-1][player.second_choice-1]
        if state==1:
            prob=player.participant.part2_urns[player.round_number-1][player.second_choice-1][0]
        else:
            prob=player.participant.part2_urns[player.round_number-1][player.second_choice-1][1]
        probability=prob*.01

        if x<=probability:
            player.green2TDrawn=1
        else:
            player.green2TDrawn=0

        y=random.random()
        probabilityS=0
        if player.second_choice==1:
            probabilityS=player.safe1*.01
        elif player.second_choice==2:
            probabilityS=player.safe2*.01
        elif player.second_choice==3:
            probabilityS=player.safe3*.01
        elif player.second_choice==4:
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
            first_choice=player.first_choice,
            green2TDrawn=player.green2TDrawn,
            green2BDrawn=player.green2BDrawn,
            second_choice=player.second_choice,
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

page_sequence = [Consent_Form, Instructions1, Instructions2, Instructions2F, Instructions3, Instructions3F,
                 Instructions4, Instructions4F, PleaseReturn,  Example, Starting_Situation, SituationFirst,
                 InitialFeedback, SituationSecond, SituationResults, Experiment_Results]
