# Generated by Django 3.1.7 on 2021-05-01 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_equipamento_tecnico'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaTecnica',
            fields=[
                ('id_area_tec', models.AutoField(primary_key=True, serialize=False)),
                ('area_tec', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'area_tecnica',
            },
        ),
        migrations.DeleteModel(
            name='Area_Tecnica',
        ),
        migrations.AlterField(
            model_name='chamado',
            name='id_equipamento',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='id_tecnico',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='patrimonio',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tecnico',
            name='id_area_tec',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_centro_custo',
            field=models.IntegerField(),
        ),
    ]