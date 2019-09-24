# Generated by Django 2.2.4 on 2019-09-24 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_despesa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=200)),
                ('unidadeCompra', models.CharField(max_length=30)),
                ('qtdPrevistoMes', models.DecimalField(decimal_places=2, max_digits=7)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('precoMaximo', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
