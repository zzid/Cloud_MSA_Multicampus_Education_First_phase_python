### dJango
<pre>
<a href = "../../docs/Django웹프레임워크.pdf">Doc</a>

* SI(System Integration), SM(System Management?)

* Spagetti code :  massy code

<del><< partition the roles >></del>
"Seperation Of Concerns(Responsibility)"
* MVC pattern : 
    M(Model) - connect with DB
    V(View) - View(output?)
    C(Controller) - Make connection between View and Model

* MTV pattern : 
    M(Model) - connect with DB
    T(Template) - View(output?)
    V(View) - Make connection between Template and Model (Simillar with Controller in MVC pattern)

>> django-admin startproject mydjango django_src
    (mydjango >> project name, django_src >> folder name)
>> python manage.py migrate
    (Create DB)
>> python manage.py runserver
    (Run server)
>> python manage.py createsuperuser
    (Create Superuser account)
>> python manage.py startapp blog
    (Create App directory ('blog'))
>> python manage.py makemigrations blog
    (Create migration file :: written with SQL)
>>  python manage.py migrate blog
    (use migration file :: Model to Table)

* ORM mapping rule : 
    Class               <-> Table
    Object              <-> Row(Record)
    Variable(Attribute) <-> Column

qs = Post.objects.all()
    >> This is ORM
    >> That means, you don't need to write a query like SQL
    >> objects all mean same with [ select * from post ]
    
</pre>
