# Generated by Django 4.2.6 on 2023-10-27 13:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Имя')),
                ('phone', models.CharField(max_length=11, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.CharField(choices=[('morning', 'Morning'), ('evening', 'Evening')], max_length=10)),
                ('extra_note', models.TextField(blank=True, null=True, verbose_name='Дополнительное примечание')),
                ('doctors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor', verbose_name='Врачи')),
            ],
            options={
                'verbose_name': 'Встреча',
                'verbose_name_plural': 'Встречи',
            },
        ),
    ]
