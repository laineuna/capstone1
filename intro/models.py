# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

# </standard imports>

author = 'Curtis Kephart'

doc = """
Section: instructions. 
An implementation of Niederle Vesterlund real effort task in oTree.
"""


def check_and_ok(user_total, reference_ints):
    ok = (user_total == sum(reference_ints))
    return ok


class Constants(BaseConstants):
    name_in_url = 'intro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    subject_netid = models.CharField(
        doc='netid',
        verbose_name='Please enter your <b>NYU</b> net ID <font color="gray"><br>for example, abc123</font>',
    )
