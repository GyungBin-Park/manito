# Generated by Django 3.1.3 on 2021-10-02 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juju', '0005_delete_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='stock_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code_num', models.CharField(max_length=50)),
                ('code_name', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
            ],
        ),
    ]
