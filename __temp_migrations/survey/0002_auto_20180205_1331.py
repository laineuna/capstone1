# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-05 09:31
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='q_GPA_highschool',
            field=otree.db.models.FloatField(null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='q_mathplacement',
            field=otree.db.models.StringField(choices=[('Mathematical Functions', 'Mathematical Functions'), ('Introduction to Vector Mathematics', 'Introduction to Vector Mathematics'), ('Trigonometry and Differential Equations', 'Trigonometry and Differential Equations'), ('Calculus', 'Calculus'), ('Multivariable Calculus', 'Multivariable Calculus')], max_length=10000, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='q_riskaversion',
            field=otree.db.models.StringField(choices=[('8 AED for certain', '8 AED for certain'), ('12 AED with a 50% chance or 6 AED with a 50% chance', '12 AED with a 50% chance or 6 AED with a 50% chance'), ('16 AED with a 50% chance or 4 AED with a 50% chance', '16 AED with a 50% chance or 4 AED with a 50% chance'), ('20 AED with a 50% chance or 2 AED with a 50% chance', '20 AED with a 50% chance or 2 AED with a 50% chance'), ('24 AED with a 50% chance or 0 AED with a 50% chance', '24 AED with a 50% chance or 0 AED with a 50% chance')], max_length=10000, null=True, verbose_name=''),
        ),
    ]
