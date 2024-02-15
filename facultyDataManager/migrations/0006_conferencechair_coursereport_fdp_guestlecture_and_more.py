# Generated by Django 5.0.1 on 2024-01-27 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyDataManager', '0005_rename_contactnumer_faculty_contactnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceChair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.CharField(max_length=20)),
                ('name_of_the_conference', models.CharField(max_length=255)),
                ('title_of_the_conference', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CourseReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.CharField(max_length=20)),
                ('title_of_course', models.CharField(max_length=255)),
                ('course_code', models.CharField(max_length=255)),
                ('lecture', models.CharField(max_length=5)),
                ('tutorial', models.CharField(max_length=5)),
                ('phase_1', models.CharField(max_length=5)),
                ('phase_2', models.CharField(max_length=5)),
                ('pass_percentage', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FDP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.CharField(max_length=20)),
                ('name_of_the_fdp', models.CharField(max_length=255)),
                ('name_of_the_institute', models.CharField(max_length=255)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('duration', models.CharField(max_length=20)),
                ('fdp_organized', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='GuestLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.CharField(max_length=20)),
                ('name_of_the_faculty', models.CharField(max_length=255)),
                ('name_of_the_host_institute', models.CharField(max_length=255)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.CharField(max_length=20)),
                ('name_of_the_workshop', models.CharField(max_length=255)),
                ('name_of_the_institute', models.CharField(max_length=255)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('duration', models.CharField(max_length=20)),
                ('workshop_organized', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='faculty',
            name='college_level',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faculty',
            name='department_level',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
    ]