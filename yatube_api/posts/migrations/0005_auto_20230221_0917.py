# Generated by Django 3.2.16 on 2023-02-21 09:17

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_group'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follower',
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='no_selfsubscribe',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_follower'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(('user', django.db.models.expressions.F('following')), _negated=True), name='no_selfsubscribe'),
        ),
    ]