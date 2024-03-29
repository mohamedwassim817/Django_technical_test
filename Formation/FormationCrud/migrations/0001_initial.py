# Generated by Django 3.2.4 on 2021-06-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('web', 'Web'), ('mobile', 'Mobile'), ('cloud', 'Cloud')], default='web', max_length=10)),
                ('etat', models.CharField(choices=[('active', 'Active'), ('non', 'Non')], default='active', max_length=10)),
            ],
        ),
    ]
