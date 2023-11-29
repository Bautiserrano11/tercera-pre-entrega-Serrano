# tercera-pre-entrega-Serrano # Mi Proyecto Django

Este proyecto Django implementa una aplicación simple para gestionar libros y películas, con funcionalidades como agregar datos, listar y buscar.

## Instrucciones de Uso

Segui estos pasos para ejecutar y probar la aplicación:

1. **Clonar el Repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd NOMBRE_DEL_PROYECTO
Configuración del Entorno Virtual:

bash
Copy code
python -m venv venv
source venv/bin/activate  # En Windows, use 'venv\Scripts\activate'
Instalar Dependencias:

bash
Copy code
pip install -r requirements.txt
Migrar la Base de Datos:

bash
Copy code
python manage.py migrate
Crear un Superusuario:

bash
Copy code
python manage.py createsuperuser
Iniciar el Servidor de Desarrollo:

bash
Copy code
python manage.py runserver
Acceder a la Aplicación:

Visita http://127.0.0.1:8000/myapp/post_list/ para ver la lista de libros.
Visita http://127.0.0.1:8000/myapp/add_data/ para agregar datos.
Visita http://127.0.0.1:8000/myapp/search/ para realizar búsquedas.
Acceder a la Interfaz de Administración de Django:

Visita http://127.0.0.1:8000/admin/ e iniciá sesión con las credenciales del superusuario.
Notas Adicionales
Este proyecto utiliza Django como framework web.
