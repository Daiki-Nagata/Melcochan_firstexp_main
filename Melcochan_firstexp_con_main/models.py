from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


class Constants(BaseConstants):
    name_in_url = 'Melcochan_firstexp_con_main'
    players_per_group = None
    num_rounds = 2

    instructions_template = 'Melcochan_firstexp_con_main/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    adv = models.IntegerField(
        label='',
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )

    quality = models.IntegerField(
        label='',
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )

