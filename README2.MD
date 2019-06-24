- folder
- create venv
- import django
- create project - customer_base
- create app - core
- add app to installed apps in project settings
- migrate models to db
- create superuser (admin / markham77)
- code the core/model (database table)
- in admin, register models
- add data via admin
- add routers that access to viewset to get db items, and serialize and expose it as an api
- install djangorestframework, markdown, , django-filter
- register fraemwork as new app in settings of project customer_base
- register url  (add routes in project c_b)
- create serializer in core
- describe the viewset in core
- add routes for it in urls of customer_base



workflow of djangorestframework
- begins with url / endpoint (client submits a http request against a specific url)
- request passed to viewset, which communicates with models, which grabs data from db
- data then passed to serializer, which formats as json 
- then data returned to viewset and passed to client
- (the serializer takes the place of an HTML template)

url ---- viewseet --- model --- db
            |
          serializer


Entry - a kind of object from the db / name of your model
all = a method that retrieves all


all_entries = Entry.objects.all()


other methods

get() returns a single object directly:

>>> one_entry = Entry.objects.get(pk=1)

filter(**kwargs)
Returns a new QuerySet containing objects that match the given lookup parameters.
exclude(**kwargs)
Returns a new QuerySet containing objects that do not match the given lookup parameters.

For example, to get a QuerySet of blog entries from the year 2006, use filter() like so:

Entry.objects.filter(pub_date__year=2006)

chaining filters

Entry.objects.filter(
...     headline__startswith='What'
... ).exclude(
...     pub_date__gte=datetime.date.today()
... ).filter(
...     pub_date__gte=datetime.date(2005, 1, 30)
... )

