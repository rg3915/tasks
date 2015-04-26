from django.db.models import Model
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import EmailField
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


class Person(Model):
    cpf = CharField(verbose_name='CPF', max_length=11)
    first_name = CharField(verbose_name='Nome', max_length=20)
    last_name = CharField(verbose_name='Sobrenome', max_length=20)
    email = EmailField(verbose_name='e-mail', unique=True)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name + " " + self.last_name
    full_name = property(__str__)


class Customer(Person):
    pass

    class Meta:
        verbose_name = u'cliente'
        verbose_name_plural = u'clientes'


class Seller(Person):
    active = BooleanField(verbose_name='ativo', default=True)
    internal = BooleanField(verbose_name='interno', default=True)
    commissioned = BooleanField(verbose_name='comissionado', default=True)

    class Meta:
        verbose_name = u'vendedor'
        verbose_name_plural = u'vendedores'
