# Generated by Django 3.0.2 on 2020-04-27 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0008_state_create_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transition',
            name='attribute_type',
            field=models.CharField(choices=[(0, '草稿中'), (1, '进行中'), (2, '被退回'), (3, '被撤销'), (4, '已完成'), (5, '已关闭')], default=0, max_length=1, verbose_name='属性类型'),
        ),
    ]