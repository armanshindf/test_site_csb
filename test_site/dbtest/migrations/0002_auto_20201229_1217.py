# Generated by Django 3.1.4 on 2020-12-29 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbtest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='name',
        ),
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbtest.categories')),
            ],
        ),
    ]
