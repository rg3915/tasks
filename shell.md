# Shell do Django

	from task.models import Task
	Task.objects.all()
	dir(Task.objects)
	Task.objects.create()
	Task.objects.filter(finalized=False)
	Task.objects.filter(id__gte=2)
	Task.objects.filter(id__in=ids)
	Task.objects.all().values()
	Task.objects.filter(id__in=ids).values('name')
	Task.objects.filter(id__in=ids).values_list('name')
	q = Task.objects.all()
	print(q.query)

gt = greater

gte = greater then

lt = lower

lte = lower then

Com case-sensitive

	Task.objects.filter(name__contains='Coffee', id__in=ids)

Sem case-sensitive

	Task.objects.filter(name__icontains='coffee')

Começa com ...

	Task.objects.filter(name__startswith='Coffee')

fk --> atributo_set

m2m --> atributos

o2o --> atributo

	u = User.objects.all()
	u.tasks

	Task.objects.values('user__username')
	Task.objects.filter(user__username='admin')

	Task.objects.filter(id__in=(2,4)).update(user=2)

	Task.objects.exclude(user=None)

	from django.contrib.auth.models import User

	Task.objects.get(name__contains='Almoçar').user

	u = User.objects.get(username='admin')
	u.last_name='Santos'
	u.save()

	from django.db.models import F, Q
	from task.models import Task
	Task.objects.filter(Q(name__contains='almoçar') | Q(name__contains='estudar'))
	Task.objects.filter(Q(name__contains='almoçar') | ~Q(name__contains='estudar'))
