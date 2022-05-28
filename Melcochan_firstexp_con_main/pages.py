from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class Instraction(Page):
    pass

class Maintask(Page):
    form_model = 'player'
    form_fields = ['adv', 'quality']
    @staticmethod
    def error_message(values):
        print('values is', values)
        if values['adv'] + values['quality'] != 10:
            return '合計で10になるように投資してください'

class Result(Page):
    pass

page_sequence = [Introduction, Maintask, Result]
