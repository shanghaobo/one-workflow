# Generated by Django 3.0.2 on 2020-04-28 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0010_customfield_field_attribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transition',
            name='dest_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dest_state', to='workflows.State', verbose_name='目的状态'),
        ),
        migrations.AlterField(
            model_name='transition',
            name='source_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='source_state', to='workflows.State', verbose_name='源状态'),
        ),
    ]