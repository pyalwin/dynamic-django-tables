# Generated by Django 3.0.3 on 2020-06-24 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usertables', '0002_auto_20200624_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='0098-1231-1233',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age of user', models.IntegerField(blank=True, null=True)),
                ('Name', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='0098-1231-1232',
        ),
    ]
