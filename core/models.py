from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta
from usuario.models import Profile


class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    data_de_criação = models.DateField(auto_now_add=True, null=True, blank=True)
    data_final = models.DateField(blank=True, null=True)
    profile = models.ForeignKey(
        Profile,
        models.CASCADE,
        blank=True,
        null=True
        )

    class Meta:
        db_table = "projeto"

    def __str__(self):
        return self.nome


class Registro(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField()


class Filtro(models.Model):
    nome = models.CharField(max_length=150)
    CATEGORIA_TAREFA = (
        (0, "Tarefa Normal"),
        (1, "Atenção"),
        (2, "Importante"),
        (3, "Urgente")
    )
    status = models.CharField(
        max_length=1,
        default=0,
        choices=CATEGORIA_TAREFA
        )


class Equipe(models.Model):
    nome = models.CharField(max_length=50)
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name="equipes"
    )
    membros = models.ManyToManyField(Profile)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "equipe"


class Tarefa(models.Model):

    STATUS_TAREFA = (
        (0, "ABERTA"),
        (1, "TRABALHANDO"),
        (2, "PAUSADA"),
        (3, "CONCLUíDA")
    )

    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    data_conclusao = models.DateTimeField(null=True)
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name="tarefas"
    )
    horario_de_inicio_atual = models.DateTimeField(null=True)
    duracao_total = models.DurationField(
        null=True,
        default=timedelta(seconds=0)
    )
    status = models.CharField(max_length=1, default=0, choices=STATUS_TAREFA)
    responsavel = models.ForeignKey(
        Profile,
        null=True,
        on_delete=models.SET_NULL)
    pre_requisito = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="pre_requisitos"
    )

    class Meta:
        db_table = "tarefa"

    def __str__(self):
        return "{}, {}".format(self.titulo, self.status)


class Checklist(models.Model):
    descricao = models.CharField(max_length=50)
    tarefa = models.ForeignKey(
        Tarefa,
        on_delete=models.CASCADE,
        related_name="checklists"
    )

    class Meta:
        db_table = "checklist"

    def __str__(self):
        return self.descricao


class Item(models.Model):
    descricao = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    checklist = models.ForeignKey(
        Checklist,
        on_delete=models.CASCADE,
        related_name="itens"
    )

    class Meta:
        db_table = "item"

    def __str__(self):
        return "{}, {}".format(self.descricao, self.status)


class Comentario(models.Model):

    conteudo = models.TextField()
    tarefa = models.ForeignKey(
        Tarefa,
        on_delete=models.CASCADE,
        related_name="comentarios"
    )
    criado_por = models.ForeignKey(Profile, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comentario"
        ordering = ['-criado_em']
