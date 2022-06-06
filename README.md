# TestQuick

## Instalar pipenv para manejar el ambiente virtual del proyecto
Para instalar pip, simplemente ejecute:

    $ pip install --user pipx
Una vez que esté pipxlisto en su sistema, continúe instalando Pipenv:

    $ pipx instalar pipenv

### Despues de instalar pipenv, dirijase al directorio donde se encuentra el archivo ` Pipfile ` y ejecute. De esta forma tendra activado el ambiente virtual del proyecto:
    $ pipenv install

### Para iniciar el servidor el proyecto, dirijase al directorio donde se encuentra el archivo `manage.py `y ejecute el siguiente comando: 

    $ python manage.py runserver

### De igual forma se anexa archivo `requirements.txt` , si desea realizar la instalaciòn de los paquetes del proyecto atraves de otro gestor de ambientes virtuales 


## Los endpoints del proyecto son:

| EndPoint | Request | Description |
| ------ | ------ |----------- |
| http://127.0.0.1:8000/api/clients/all/ |GET|Obtiene todos los clientes|
| http://127.0.0.1:8000/api/clients/all/ |POST|Crea un cliente con data JSON |
| http://127.0.0.1:8000/api/client/<int:pk>/ |PUT|Actualiza cliente por medio de PK|
| http://127.0.0.1:8000/api/client/<int:pk>/ |DELETE|Elimina cliente por medio de PK|
| http://127.0.0.1:8000/api/bills/all/ |GET|Obtiene todas las facturas|
| http://127.0.0.1:8000/api/bills/all/ |POST|Crea una factura con data JSON |
| http://127.0.0.1:8000/api/bill/<int:pk>/ |PUT|Actualiza factura por medio de PK|
| http://127.0.0.1:8000/api/bill/<int:pk>/ |DELETE|Elimina factura por medio de PK|
| http://127.0.0.1:8000/api/products/all/ |GET|Obtiene todos los productos|
| http://127.0.0.1:8000/api/products/all/ |POST|Crea un product con data JSON|
| http://127.0.0.1:8000/api/product/<int:pk>/|PUT|Actualiza producto por medio de PK|
| http://127.0.0.1:8000/api/product/<int:pk>/|DELETE|Elimina producto por medio de PK|
| http://127.0.0.1:8000/api/up_down_csv/|GET|Descarga archivo CSV con resumen de clientes y facturas|
| http://127.0.0.1:8000/api/up_down_csv/|POST|Cargue archivo CSV para creacion de clientes|
| http://127.0.0.1:8000/api/register/|POST|Registra un usuario nuevo y retorna JW token de autenticaciòn|
| http://127.0.0.1:8000/api/login/|POST|Acceso al usuario por medio de JW token|


## NOTA:
- El archivo generado en el endpoint http://127.0.0.1:8000/api/up_down_csv/ por medio del metodo GET, serà descargado con el nombre `Bills.zip` en el directorio raiz del proyecto. Es necesario extraer dicho archivo para obtener el documento.csv
- Para testear el proyecto, se adjunta thunder-collection_TestQuick.json de todos los requests elaborados para cada endpoint.
- Adicionalmente se crearon los test.py correspondientes a cada entidad del proyecto
- Con el fin de validar los datos generados en los request de testeo se adjunta archivo db.sqlite3
- Para acceder a cada endpoint es necesario que el usuario se haya creado previamente y se encuentre autenticado de manera correcta; enviando el JW Token en el cabecero de la solicitud HTTP.






