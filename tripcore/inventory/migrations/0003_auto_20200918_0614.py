# Generated by Django 3.1.1 on 2020-09-18 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_fixture_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('led', 'LED'), ('conventional', 'Conventional'), ('mover', 'Mover')], default='conventional', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('led', 'LED'), ('conventional', 'Conventional'), ('mover', 'Mover')], default='conventional', max_length=20)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.source')),
            ],
        ),
        migrations.AddField(
            model_name='fixture',
            name='kind',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.kind'),
        ),
        migrations.AlterField(
            model_name='fixture',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.source'),
        ),
    ]
