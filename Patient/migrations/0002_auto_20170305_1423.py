# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='Q1',
            field=models.CharField(choices=[(0, 'The beach'), (0, 'An amusement park'), (1, 'The dinner table'), (0, 'I am not sure')], max_length=1, verbose_name='Where is the patient at the beginning of the story?'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='Q2',
            field=models.CharField(choices=[(1, 'Vision problems'), (0, 'Shortness of breath'), (0, 'Headache'), (0, 'Pain in her leg'), (0, 'I am not sure')], max_length=1, verbose_name="What is the patient's concern?"),
        ),
        migrations.AlterField(
            model_name='questions',
            name='Q3',
            field=models.CharField(choices=[(0, 'reading glasses'), (0, 'asthma medication'), (1, 'cataract surgery'), (0, 'a cast'), (0, 'no procedure'), (0, 'I am not sure')], max_length=1, verbose_name='What does the doctor suggest for the patient?'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='Q4',
            field=models.CharField(choices=[(0, 'nausea  and vomitting'), (1, 'infection, bleeding, loss of vision, double vision, after-cataract'), (0, 'no risk'), (0, 'I am not sure')], max_length=1, verbose_name='What are the risks of the surgery that the doctor explains to the patient?'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='Q5',
            field=models.CharField(choices=[(1, 'Yes, the minor risks of complications outweighs the risk of the cataract getting worse and requiring a more complicated surgery with more risks later on.'), (0, 'No, the minor risks of complications does not outweigh the minor risk of the cataract getting worse and requiring a more complicated surgery with more risks later on.'), (0, 'No, the doctor does not want his patient to receive the surgery'), (0, 'I am not sure')], max_length=1, verbose_name='Do the risks of receiving the cataract surgery outweigh the risks of not receiving the surgery?'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='Q6',
            field=models.CharField(choices=[(0, 'Her cataract will heal on its own'), (1, 'Her cataract may get worse'), (0, 'I am not sure')], max_length=1, verbose_name='If the patient does not receive the surgery...'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='Q7',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], max_length=1, verbose_name='In your opinion, should the patient receive the surgery?'),
        ),
    ]
