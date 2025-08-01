# Generated by Django 4.2.23 on 2025-07-27 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Primary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_building', models.CharField(choices=[('EM', 'Empty'), ('GH', 'Great Hall'), ('MK', 'Market'), ('MN', 'Monastery'), ('LP', 'Longphort')], default='EM', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Secondary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secondary_building', models.CharField(choices=[('EM', 'Empty'), ('BA', 'Benedictine Abbey'), ('FM', 'Farm'), ('OR', 'Orchard'), ('PA', 'Pasture'), ('HN', 'Hunting'), ('FI', 'Fishing'), ('WD', 'Wood'), ('GD', 'Gold'), ('TN', 'Tin'), ('IN', 'Iron'), ('SL', 'Silver'), ('CP', 'Copper'), ('LD', 'Lead'), ('CL', 'Cloth'), ('SA', 'Salt'), ('BP', 'Beach Port'), ('PT', 'Pottery')], default='EM', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='province_plans', to=settings.AUTH_USER_MODEL)),
                ('primary_building', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='primary_building_of', to='planner.primary')),
                ('secondary_building_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary_building_1_of', to='planner.secondary')),
                ('secondary_building_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary_building_2_of', to='planner.secondary')),
                ('secondary_building_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary_building_3_of', to='planner.secondary')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
