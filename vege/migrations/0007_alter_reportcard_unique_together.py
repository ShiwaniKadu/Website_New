# Generated by Django 4.2 on 2024-01-18 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0006_reportcard'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reportcard',
            unique_together={('student_rank', 'date_of_report_card_generation')},
        ),
    ]
