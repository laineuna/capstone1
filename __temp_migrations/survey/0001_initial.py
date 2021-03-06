# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-04 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_group', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('q_rank', otree.db.models.StringField(choices=[['1', '1 (you solved the most questions right)'], ['2', '2'], ['3', '3'], ['4', '4 (you solved the least questions right)']], max_length=10000, null=True, verbose_name='')),
                ('q_riskaversion', otree.db.models.StringField(choices=[('8 AED for certain', '8 AED for certain'), ('12 AED or 6 AED with a 50% chance', '12 AED or 6 AED with a 50% chance'), ('16 AED or 4 AED with a 50% chance', '16 AED or 4 AED with a 50% chance'), ('20 AED or 2 AED with a 50% chance', '20 AED or 2 AED with a 50% chance'), ('24 AED or 0 AED with a 50% chance', '24 AED or 0 AED with a 50% chance')], max_length=10000, null=True, verbose_name='')),
                ('q_riskpreference', otree.db.models.StringField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=10000, null=True, verbose_name='')),
                ('q_mathplacement', otree.db.models.StringField(choices=[('Mathematical Functions', 'Mathematical Functions'), ('Introduction to Vector Mathematics', 'Introduction to Vector Mathematics'), ('Calculus', 'Calculus'), ('Multivariable Calculus', 'Multivariable Calculus')], max_length=10000, null=True, verbose_name='')),
                ('q_mathlevel', otree.db.models.StringField(choices=[('Pre-Calculus', 'Pre-Calculus'), ('Calculus', 'Calculus'), ('Mutivariable calculus', 'Mutivariable calculus'), ('Beyond multivariable calculus', 'Beyond multivariable calculus')], max_length=10000, null=True, verbose_name='')),
                ('q_GPA_highschool', otree.db.models.FloatField(null=True, verbose_name='What was your final GPA in high school?')),
                ('q_GPA_highschool_max', otree.db.models.FloatField(null=True, verbose_name='')),
                ('q_majordeclarationYN', otree.db.models.StringField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10000, null=True, verbose_name='')),
                ('q_expectedstudytrack_AH', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Arts and Humanities')),
                ('q_expectedstudytrack_EG', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Engineering')),
                ('q_expectedstudytrack_MD', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Multidisciplinary (Arab Crossroads or Interactive Media)')),
                ('q_expectedstudytrack_SC', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Science')),
                ('q_expectedstudytrack_SS', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Social Science')),
                ('q_declaredstudytrack_AH', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Arts and Humanities')),
                ('q_declaredstudytrack_EG', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Engineering')),
                ('q_declaredstudytrack_MD', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Multidisciplinary (Arab Crossroads or Interactive Media)')),
                ('q_declaredstudytrack_SC', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Science')),
                ('q_declaredstudytrack_SS', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Social Science')),
                ('q_gpastudytrack', otree.db.models.StringField(choices=[('Arts and Humanities', 'Arts and Humanities'), ('Engineering', 'Engineering'), ('Multidisciplinary Track (Interactive Media, Arab Crossroads', 'Multidisciplinary Track (Interactive Media, Arab Crossroads'), ('Science', 'Science'), ('Social Science', 'Social Science')], max_length=10000, null=True, verbose_name='')),
                ('q_profitablestudytrack', otree.db.models.StringField(choices=[('Arts and Humanities', 'Arts and Humanities'), ('Engineering', 'Engineering'), ('Multidisciplinary Track (Interactive Media, Arab Crossroads', 'Multidisciplinary Track (Interactive Media, Arab Crossroads'), ('Science', 'Science'), ('Social Science', 'Social Science')], max_length=10000, null=True, verbose_name='')),
                ('q_mathlevelnyuad', otree.db.models.StringField(choices=[('...in the top 25%?', '...in the top 25%?'), ('...in the top 25-50%?', '...in the top 25-50%?'), ('...in the top 50-75%?', '...in the top 50-75%?'), ('...in the bottom 25%?', '...in the bottom 25%?')], max_length=10000, null=True, verbose_name='')),
                ('q_passinggrade', otree.db.models.StringField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=10000, null=True, verbose_name='')),
                ('q_wealth', otree.db.models.StringField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10000, null=True, verbose_name='')),
                ('task_1_score', otree.db.models.PositiveIntegerField(null=True)),
                ('task_2_score', otree.db.models.PositiveIntegerField(null=True)),
                ('op_scores', otree.db.models.StringField(max_length=10000, null=True)),
                ('op_top_score', otree.db.models.PositiveIntegerField(null=True)),
                ('task_2_final_score', otree.db.models.PositiveIntegerField(null=True)),
                ('payment_method_selection', otree.db.models.StringField(max_length=10000, null=True)),
                ('task_3_score', otree.db.models.PositiveIntegerField(null=True)),
                ('task_3_final_score', otree.db.models.PositiveIntegerField(null=True)),
                ('task_4_payment', otree.db.models.StringField(max_length=10000, null=True)),
                ('final_task_earnings', otree.db.models.FloatField(null=True)),
                ('risk_aversion_payment', otree.db.models.PositiveIntegerField(null=True)),
                ('showup_Fee', otree.db.models.FloatField(null=True)),
                ('final_earnings', otree.db.models.FloatField(null=True)),
                ('q_CT_publicsector', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], null=True, verbose_name='I would rather work in public than private sector.')),
                ('q_CT_familyimportance', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], null=True, verbose_name='Family is more important than work.')),
                ('q_CT_wagevshours', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], null=True, verbose_name='I would work for higher wage even if there is less flexibility in working hours.')),
                ('q_CT_incomecontribution', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], null=True, verbose_name='Having a job is the best way for a woman to be an independent person.')),
                ('q_CT_jobwomenindependence', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], null=True, verbose_name='When a mother works for pay outside the home, the children suffer.')),
                ('q_CT_workingmother', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], null=True, verbose_name='A working mother can establish just as warm and secure a relationship with her children as a mother who does not work')),
                ('q_CT_fatherSuited', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], null=True, verbose_name='In general, fathers are as fit to look after children as mothers')),
                ('q_CT_preschoolWork', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], null=True, verbose_name='A pre-school child is likely to suffer if his or her mother works')),
                ('q_gpastudytrack_AH', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']], null=True, verbose_name='Arts and Humanities')),
                ('q_gpastudytrack_EG', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']], null=True, verbose_name='Engineering')),
                ('q_gpastudytrack_MD', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']], null=True, verbose_name='Multidisciplinary (Arab Crossroads or Interactive Media)')),
                ('q_gpastudytrack_SC', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']], null=True, verbose_name='Science')),
                ('q_gpastudytrack_SS', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']], null=True, verbose_name='Social Science')),
                ('q_profitablestudytrack_AH', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']], null=True, verbose_name='Arts and Humanities')),
                ('q_profitablestudytrack_EG', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']], null=True, verbose_name='Engineering')),
                ('q_profitablestudytrack_MD', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']], null=True, verbose_name='Multidisciplinary (Arab Crossroads or Interactive Media)')),
                ('q_profitablestudytrack_SC', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']], null=True, verbose_name='Science')),
                ('q_profitablestudytrack_SS', otree.db.models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']], null=True, verbose_name='Social Science')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_player', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Subsession'),
        ),
    ]
