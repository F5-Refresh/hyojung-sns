# Generated by Django 3.2.14 on 2022-07-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='이메일')),
                ('password', models.CharField(max_length=150, verbose_name='비밀번호')),
                ('nickname', models.CharField(max_length=10, verbose_name='닉네임')),
                ('is_active', models.BooleanField(default=True, verbose_name='계정 활성화 여부')),
                ('is_admin', models.BooleanField(default=False, verbose_name='admin 권한')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]