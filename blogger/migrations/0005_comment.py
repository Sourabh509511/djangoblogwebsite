# Generated by Django 3.1 on 2020-08-10 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogger', '0004_auto_20200809_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_text', models.TextField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogger.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogger.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
