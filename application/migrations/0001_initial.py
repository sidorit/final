# Generated by Django 3.2.5 on 2021-07-25 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='사용자명')),
                ('one_introduction', models.CharField(max_length=100, verbose_name='한 줄 소개')),
                ('motive', models.TextField(verbose_name='지원동기')),
                ('make_site', models.TextField(verbose_name='만들고 싶은 사이트')),
                ('why', models.TextField(verbose_name='이유')),
                ('project_experience', models.TextField(verbose_name='경험')),
                ('conflict', models.TextField(verbose_name='갈등')),
                ('solution', models.TextField(verbose_name='해결방법')),
                ('state', models.TextField(blank=True, default='지원 완료', verbose_name='합불상태')),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '지원서',
                'verbose_name_plural': '지원서',
                'db_table': 'User_Application_table',
            },
        ),
    ]
