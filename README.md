# App de Reserva de Eventos

## Alkemy - Comisión 1 Squad 3

# Índice
* <span><a href="#descripcion">Descripción del Proyecto</a></span>
* <span><a href="#visual"></a></span>
* <span><a href="#modulos">Módulos</a></span>
* <span><a href="#ejecutar">Ejecutar Proyecto</a></span>
* <span><a href="#colaboradores">Colaboradores</a></span>

<h2 id="descripcion">Descripción del Proyecto</h2>
Aplicación web desarrollada en Python con framework Django que permite registrar los servicios que la empresa ofrece, registrar empleados y clientes, poder reservar un servicio para un cliente y visualizar diferentes tipos de listados. También se puede acceder a la información de los servicios a través de un endpoint en donde se podrán consultar todos los servicios disponibles y poder filtrarlos por el id en donde se visualizará el detalle completo del mismo.

<h2 id="modulos">Módulos</h2>
<ul>
    <li>api</li>
    <li>clientes</li>
    <li>coordinadores</li>
    <li>empleados</li>
    <li>reservas</li>
    <li>servicios</li>
</ul>

<h2 id="ejecutar">Ejecutar Proyecto en Windows</h2>
<h3>Requerimiento Python 3.9 o superior</h3>

python -m venv venv <br />
venv/Scripts/activate <br />
pip install -r requirements.txt <br />
cd src <br />
python manage.py makemigrations <br />
python manage.py migrate <br />
python manage.py runserver <br />


<h2 id="colaboradores">Colaboradores</h2>

* Mendez, Eusebio
* Camacho, Pablo
* Zelaya, Fernando
* Chachagua, Daniel