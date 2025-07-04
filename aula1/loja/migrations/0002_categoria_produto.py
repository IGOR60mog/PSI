# Generated by Django 4.2.7 on 2025-04-28 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Categoria', models.CharField(max_length=100)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('alterado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Produto', models.CharField(max_length=100)),
                ('destaque', models.BooleanField(default=True)),
                ('promocao', models.BooleanField(default=True)),
                ('msgPromocao', models.CharField(max_length=100, null=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('alterado_em', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categoria', to='loja.categoria')),
                ('fabricante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fabricante', to='loja.fabricante')),
            ],
        ),
    ]
