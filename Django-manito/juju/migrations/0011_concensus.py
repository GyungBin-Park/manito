# Generated by Django 3.1.3 on 2021-10-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juju', '0010_f_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='concensus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code_num', models.TextField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('target_prc', models.BigIntegerField(blank=True, db_column='TARGET_PRC', null=True)),
                ('recom_cd', models.FloatField(blank=True, db_column='RECOM_CD', null=True)),
                ('inst_nm', models.BigIntegerField(blank=True, db_column='INST_NM', null=True)),
                ('close', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'concensus',
                'managed': False,
            },
        ),
    ]
