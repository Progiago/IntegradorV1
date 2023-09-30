from django.db import models
from usuario.models import Profile


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    creation_date = models.DateField(auto_now_add=True, null=True, blank='')
    profile = models.ForeignKey(
        Profile,
        models.CASCADE,
        blank=True,
        null=True
        )

    class Meta:
        db_table = "projeto"

    def __str__(self):
        return self.title


class Filter(models.Model):
    category_name = models.CharField(max_length=150)
    TASK_CATEGORY = (
        ("0", "Tarefa Normal"),
        ("1", "Atenção"),
        ("2", "Importante"),
        ("3", "Urgente")
    )
    status = models.CharField(
        max_length=1,
        default=0,
        choices=TASK_CATEGORY
        )


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="equipes"
    )
    menbers = models.ManyToManyField(Profile)

    def __str__(self):
        return self.team_name

    class Meta:
        db_table = "team"


class Task(models.Model):

    TASK_STATUS = (
        ("0", "ABERTA"),
        ("1", "TRABALHANDO"),
        ("2", "PAUSADA"),
        ("3", "CONCLUíDA")
    )

    task_title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    completion_date = models.DateTimeField(null=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tarefas"
    )
    current_start_time = models.DateTimeField(
        null=True, auto_now_add=True)
    total_duration = models.DurationField(
        null=True,
    )
    status = models.CharField(max_length=1, default=0, choices=TASK_STATUS)
    responsible = models.ForeignKey(
        Profile,
        null=True,
        on_delete=models.SET_NULL)

    class Meta:
        db_table = "tarefa"

    def __str__(self):
        return "{}, {}".format(self.titulo, self.status)


class Checklist(models.Model):
    description = models.CharField(max_length=50)
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="checklists",
        null=True
    )

    class Meta:
        db_table = "checklist"

    def __str__(self):
        return self.description


class Item(models.Model):
    description = models.CharField(max_length=50)
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


class Comment(models.Model):

    content = models.TextField()
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="comentarios",
        null=True
    )
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_in = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comentario"
        ordering = ['-created_in']
    
