# Generated by Django 2.1.1 on 2018-09-26 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomVernaculaire', models.CharField(max_length=200)),
                ('nomScientifique', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Famille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ordre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifap.Classe')),
            ],
        ),
        migrations.AddField(
            model_name='famille',
            name='ordre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifap.Ordre'),
        ),
        migrations.AddField(
            model_name='animal',
            name='famille',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifap.Famille'),
        ),
    ]
