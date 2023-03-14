# Generated by Django 4.0.6 on 2023-03-10 20:21

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('1', 'Admin'), ('2', 'Teacher'), ('3', 'Caller'), ('4', 'Student')], default=1, max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('no_of_students', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('academic_qualification', models.CharField(choices=[('10th', '10th'), ('12th', '12th'), ('Graduate', 'Graduate'), ('Other', 'Other')], max_length=20)),
                ('professional_qualification', models.CharField(max_length=50)),
                ('course', models.ManyToManyField(to='accounts.course')),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentEnquiry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('FatherHusband_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('mobile_number', models.CharField(max_length=15)),
                ('guardian_phone_number', models.CharField(max_length=15)),
                ('ParentHusband_occupation', models.CharField(max_length=50)),
                ('academic_qualification', models.CharField(choices=[('10th', '10th'), ('12th', '12th'), ('Graduate', 'Graduate'), ('Other', 'Other')], max_length=20)),
                ('professional_qualification', models.CharField(max_length=50)),
                ('institute_knowing', models.CharField(choices=[('Newspaper', 'Newspaper'), ('Family', 'Family'), ('Student of institute', 'Student of institute'), ('Social Sites', 'Social Sites'), ('Banner', 'Banner'), ('Website', 'Website')], max_length=50)),
                ('admission_done', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('enquiry_for_course', models.ManyToManyField(to='accounts.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('FatherHusband_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('mobile_number', models.CharField(max_length=15)),
                ('guardian_phone_number', models.CharField(max_length=15)),
                ('ParentHusband_occupation', models.CharField(max_length=50)),
                ('academic_qualification', models.CharField(choices=[('10th', '10th'), ('12th', '12th'), ('Graduate', 'Graduate'), ('Other', 'Other')], max_length=20)),
                ('professional_qualification', models.CharField(max_length=50)),
                ('adhar_card', models.CharField(max_length=10)),
                ('course_id', models.ManyToManyField(to='accounts.course')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Caller',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('academic_qualification', models.CharField(choices=[('10th', '10th'), ('12th', '12th'), ('Graduate', 'Graduate'), ('Other', 'Other')], max_length=20)),
                ('professional_qualification', models.CharField(max_length=50)),
                ('caller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.student')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('academic_qualification', models.CharField(choices=[('10th', '10th'), ('12th', '12th'), ('Graduate', 'Graduate'), ('Other', 'Other')], max_length=20)),
                ('professional_qualification', models.CharField(max_length=50)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]