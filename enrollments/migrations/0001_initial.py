# Generated by Django 4.2.1 on 2023-05-24 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('enrolled_on', models.DateTimeField(blank=True, null=True)),
                ('enrolled_valid', models.DateTimeField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_enrollments', to='courses.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_enrollments', to='accounts.user')),
            ],
            options={
                'db_table': 'enrollments',
                'unique_together': {('course', 'user')},
            },
        ),
    ]
