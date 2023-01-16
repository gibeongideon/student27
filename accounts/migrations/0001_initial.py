# Generated by Django 3.1.13 on 2022-12-22 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('tokens', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('actual_balance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('withraw_power', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('refer_balance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('trial_balance', models.DecimalField(blank=True, decimal_places=2, default=50000, max_digits=12, null=True)),
                ('cum_deposit', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('cum_withraw', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                'db_table': 'w_accounts',
                'ordering': ('-user_id',),
            },
        ),
        migrations.CreateModel(
            name='AccountSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('min_redeem_refer_credit', models.FloatField(blank=True, default=1000, null=True)),
                ('auto_approve', models.BooleanField(blank=True, default=False, null=True)),
                ('auto_approve_cash_trasfer', models.BooleanField(blank=True, default=False, null=True)),
                ('withraw_factor', models.FloatField(blank=True, default=1, null=True)),
                ('paypill', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 'w_accounts_setup',
            },
        ),
        migrations.CreateModel(
            name='CentralBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('give_away', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='give_away')),
                ('to_keep', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='to_keep')),
                ('give_away_marketer', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='give_away_marketer')),
                ('to_keep_marketer', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='to_keep_marketer')),
            ],
            options={
                'db_table': 'w_central_banks',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'Currencies',
                'db_table': 'currencies',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('running_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('trans_type', models.CharField(blank=True, max_length=120, null=True)),
                ('currency', models.CharField(blank=True, max_length=120, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
            options={
                'db_table': 'w_transactions',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='CashWithrawal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='amount')),
                ('tokens', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('approved', models.BooleanField(blank=True, default=False, null=True)),
                ('cancelled', models.BooleanField(blank=True, default=False, null=True)),
                ('withrawned', models.BooleanField(blank=True, null=True)),
                ('confirmed', models.BooleanField(blank=True, null=True)),
                ('has_record', models.BooleanField(blank=True, null=True)),
                ('withr_type', models.CharField(blank=True, default='shop', max_length=100, null=True)),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.currency')),
            ],
            options={
                'db_table': 'w_withrawals',
                'get_latest_by': 'id',
            },
        ),
        migrations.CreateModel(
            name='CashDeposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('tokens', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('confirmed', models.BooleanField(blank=True, default=False, null=True)),
                ('deposited', models.BooleanField(blank=True, null=True)),
                ('deposit_type', models.CharField(blank=True, default='Shop Deposit', max_length=100, null=True)),
                ('has_record', models.BooleanField(blank=True, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.currency')),
            ],
            options={
                'db_table': 'w_deposits',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='cbank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.centralbank'),
        ),
    ]