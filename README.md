# tu_empleado_perfecto_simpli_latam
 
Tu Empleado Perfecto: Solución prueba tecnica
====================================

Tu Empleado Perfecto es una solución que tiene por objetivo mantener datos de empresas 
y empleados.

Aquí podrás encontrar un módulo (backend_django) escrito en lenguaje Pyhton + Django + RestFramework para el despliegue 
de Servicio Api. (backend)

Tambien encontrarás un módulo (frontend_vue) escrito en lenguaje VueJS 3 para la gestion y visualización de
la información correspondiente a empresas y/o empleados. (frontend)

La solución se construye originalmente para ser evaluada por equipo técnico de
[simplilatam](https://www.simplilatam.com/).

Esta solucion solo se basó en los requerimientos solicitados en el documento compartido
por simplilatam.


Funcionalidades implementadas
-----------------------------

- Conexión a servidor [15.235.86.83](https://desapli.com/Principal).
- Motor de base de datos MySQL
- Obtención listado de empresas.
- Obtención listado de empleados por empresa.
- Agregar/Editar información de empresas.
- Agregar/Editar información de empleados.
- Acciones en cuanto a validación y formatos:
    - Formato rut ya establecido en los formularios.
    - Validación rut en base modulo 11.
    - Validación rut ya existente.

Instalación de la solución
-----------

Versión python:

    Python 3.12.4

Clonar repositorio directamente o desde la terminal con:

	git clone -b $ https://github.com/AnthoGonza/tu_empleado_perfecto_simpli_latam.git

Crear y levantar VirtualEnv del modulo backend_django

    paso 1: py -m venv "env"
    paso 2: .\env\scripts\activate

Instalar dependencias del modulo backend_django:

    pip install -r requirements.txt 
    
Instalar dependencias del modulo frontend_vue:

    npm install

El sistama está/estará disponibles en el siguiente link
[https://tuempleadoperfecto.desapli.com](https://tuempleadoperfecto.desapli.com/).

Términos y condiciones de uso
-----------------------------

Al utilizar este proyecto, total o parcialmente, automáticamente se acepta
cumplir con los términos y condiciones de uso de La
[Licencia Pública General Affero de GNU (AGPL)](https://es.wikipedia.org/wiki/GNU_General_Public_License).

Contribuir al proyecto
----------------------

Si deseas contribuir con el proyecto, especialmente resolviendo algunos puntos
pendientes y/mejoras de la solución, debes:

1. Hacer fork del proyecto en [GitHub](https://github.com/AnthoGonza/tu_empleado_perfecto_simpli_latam.git)
2. Crear una *branch* para los cambios: git checkout -b nombre-branch
3. Modificar código: git commit -am 'Se agrega...'
4. Publicar cambios: git push origin nombre-branch
5. Crear un *pull request* para unir la nueva *branch* con LibreDTE.

**IMPORTANTE**: antes de hacer un *pull request* verificar que el código
cumpla con los estándares [PSR-1](http://www.php-fig.org/psr/psr-1),
[PSR-2](http://www.php-fig.org/psr/psr-2) y
[PSR-4](http://www.php-fig.org/psr/psr-4).

Contacto y redes sociales
-------------------------

- Sitio web: <https://desapli.com/Principal>
- Linkedin: <https://www.linkedin.com/in/anthony-brando-gonzales-alvarez-316198228/>
