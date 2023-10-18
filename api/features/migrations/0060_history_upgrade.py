# Generated by Django 3.2.20 on 2023-10-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0059_fix_feature_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalfeature',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical feature', 'verbose_name_plural': 'historical features'},
        ),
        migrations.AlterModelOptions(
            name='historicalfeaturesegment',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical feature segment', 'verbose_name_plural': 'historical feature segments'},
        ),
        migrations.AlterModelOptions(
            name='historicalfeaturestate',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical feature state', 'verbose_name_plural': 'historical feature states'},
        ),
        migrations.AlterModelOptions(
            name='historicalfeaturestatevalue',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical feature state value', 'verbose_name_plural': 'historical feature state values'},
        ),
        migrations.AlterField(
            model_name='historicalfeature',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfeaturesegment',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfeaturestate',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalfeaturestatevalue',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
