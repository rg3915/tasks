# Tasks

Task scheduling system made in Django 1.7


## Notas

### Boas práticas

* Crie o app fora da pasta de configuração mesmo, ou seja,

	.
	├── manage.py
	├── task_project
	│   ├── settings.py
	│   └── urls.py
    └── task
        ├── admin.py
        ├── forms.py
        ├── models.py
        ├── tests.py
        └── views.py
 
* Importe todos os `Fields` separadamente, isso melhora a performance.

	from django.db.models import CharField
	from django.db.models import TextField
	from django.db.models import BooleanField
	from django.db.models import DateTimeField

