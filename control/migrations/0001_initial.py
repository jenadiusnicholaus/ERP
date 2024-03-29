# Generated by Django 2.2.6 on 2020-04-14 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('opening_balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('street', models.CharField(blank=True, max_length=200, null=True)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='branch_manager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
                'permissions': (('block_region', 'Can Block Region'), ('unblock_region', 'Can Unblock Region')),
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('salary_take_home', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('salary_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_salary', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Salary',
                'verbose_name_plural': 'Salaries',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'UserType',
                'verbose_name_plural': 'UserTypes',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user_type', models.CharField(choices=[('Customer', 'Customer'), ('Borrower', 'Borrower'), ('Supplier', 'Supplier'), ('Staff', 'Staff')], default='Staff', max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('credit_limit', models.CharField(blank=True, max_length=200, null=True)),
                ('credit_day', models.IntegerField(blank=True, null=True)),
                ('balance', models.CharField(blank=True, max_length=200, null=True)),
                ('salary_amount', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('registered_date', models.DateField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='added_by', to=settings.AUTH_USER_MODEL)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_branch', to='control.Branch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserProfile',
                'verbose_name_plural': 'UserProfiles',
            },
        ),
        migrations.CreateModel(
            name='SalaryDeduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('salary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='control.Salary')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NotePad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('priority', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='note_reated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Note Pad',
                'verbose_name_plural': 'Note Pads',
            },
        ),
        migrations.AddField(
            model_name='branch',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='branch_region', to='control.Region'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('time_in', models.CharField(blank=True, max_length=20, null=True)),
                ('time_out', models.TimeField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendant', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendances',
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('asset_number', models.CharField(blank=True, max_length=200, null=True)),
                ('condition', models.CharField(choices=[('working', 'working'), ('not working', 'not working')], default='working', max_length=100)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asset_branch', to='control.Branch')),
            ],
            options={
                'verbose_name': 'Asset',
                'verbose_name_plural': 'Assets',
            },
        ),
        migrations.CreateModel(
            name='AccountTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('transanction_type', models.CharField(choices=[('deposit', 'deposit'), ('withdraw', 'withdraw'), ('transfer', 'transfer')], default='deposit', max_length=100)),
                ('transanction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='transanction_bank', to='control.Account')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transaction_personel', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'AccountTransaction',
                'verbose_name_plural': 'AccountTransactions',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch_account', to='control.Branch'),
        ),
    ]
