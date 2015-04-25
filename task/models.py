from django.db.models import Model
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import BooleanField
from django.db.models import DateTimeField


class Task(Model):
    name = CharField(verbose_name='nome', max_length=50)
    description = TextField(verbose_name='descrição')
    finalized = BooleanField(default=False, verbose_name='finalizado')
    date_execution = DateTimeField(
        verbose_name='data de execução', blank=True, null=True)
    created_at = DateTimeField(
        auto_now_add=True, auto_now=False, verbose_name='criado em')
    modified_at = DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'tarefa'
        verbose_name_plural = 'tarefas'

    def __str__(self):
        return self.name
