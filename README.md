# entregable-sprint-7

Antes de comenzar a ejecutar el proyecto, se debe dirigir al archivo 
Auth y agregar en el Modelo AbstractUser la siguiente propiedad

customer_id = models.IntegerField(default=-1)


(En caso de no encontrar el archivo, dirígase a
  C:\Users\< su_usuario >\AppData\Local\Programs\Python\Python310\Lib\site-package\django\contrib\auth\models.py
)

Luego ingrese los comandos

cd homebanking

python manage.py makemigrations

python manage.py migrate