"""
Definition of models.
"""

from django.db import models

# Criem os model aqui das tabelas que forem necessarias
# primeiro precisa ser descrito como sera a classe/tabela abaixo
# depois rodar abrir um terminal (ctrl + `) e rodar o comando python .\manage.py makemigrations 
# rodar o comando python .\manage.py migrate
# e pronto a tabela tera sido criada 


STATUS_CHOICES = (
    (1, 'Aberto'),
    (2, 'Em processamento'),
    (3, 'Cancelado'),
    (4, 'Concluido'),
)

EQUIPMENT_CHOICES = (
    (1, 'Computador'),
    (2, 'Servidor'),
    (3, 'Telefone'),
)

TECHNICIAN_CHOICES = (
    (1, 'Tecnico Roberto'),
    (2, 'Tecnico Paulo'),
)

TECH_AREA_CHOICES = (
    (1, 'Administrativo'),
    (2, 'Financeiro'),
    (3, 'TI'),
    (4, 'Almox'),
)

TYPE_USER_CHOICES = (
    (1, 'Comum'),
    (2, 'Tecnico'),
    (3, 'Admin'),
)

class Chamado(models.Model):
    id_chamado = models.AutoField(primary_key = True)
    assunto = models.CharField(max_length = 255, null=True)
    texto = models.CharField(max_length = 999, null=True)
    data_abertura = models.DateField(null=True)
    data_fechamento = models.DateField(null=True)
    status = models.IntegerField(choices=STATUS_CHOICES,null=True)
    id_equipamento = models.IntegerField(choices=EQUIPMENT_CHOICES,null=True)
    id_usuario = models.IntegerField(null=True)
    id_tecnico = models.IntegerField(choices=TECHNICIAN_CHOICES, null=True)
    id_area_tec = models.IntegerField(choices=TECH_AREA_CHOICES, null=True)

    class Meta:
        db_table = 'chamado'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 255)
    email = models.CharField(max_length = 999)
    senha = models.CharField(max_length = 255)
    tipo = models.IntegerField(choices=TYPE_USER_CHOICES)
    token = models.CharField(max_length = 255)
    id_centro_custo = models.IntegerField(choices=TECHNICIAN_CHOICES)
    id_area_tec = models.IntegerField(choices=TECH_AREA_CHOICES)

    class Meta:
        db_table = 'usuario'



    def __str__(self):
        return self.name

class Tecnico(models.Model):
    id_tecnico = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 255)
    id_usuario = models.IntegerField(null=True)
    id_area_tec = models.IntegerField(choices=TECH_AREA_CHOICES)

    class Meta:
        db_table = 'tecnico'