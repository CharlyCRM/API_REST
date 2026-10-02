# Primera API de productos con Flask

Este ejercicio fue una forma de aprender las operaciones básicas de una API: consultar una lista, añadir un producto, modificarlo y eliminarlo. Para centrarme en las rutas HTTP utilicé una lista de Python en lugar de una base de datos.

## Rutas

| Método | Ruta | Operación |
| --- | --- | --- |
| GET | `/products` | Consultar productos |
| GET | `/products/<nombre>` | Buscar por nombre |
| POST | `/products` | Añadir un producto |
| PUT | `/products/<nombre>` | Modificar un producto |
| DELETE | `/products/<nombre>` | Eliminar un producto |

`/ping` devuelve la lista de productos; no es una comprobación independiente de salud.

## Probar en local

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requierements.txt
python app.py
```

El archivo de dependencias se llama `requierements.txt`. El servidor utiliza el puerto 5000. Para crear o modificar un producto, el cuerpo JSON contiene `nombre`, `precio` y `cantidad`.

```sh
curl http://127.0.0.1:5000/products
```

## Qué representa esta versión

Los cambios se pierden al reiniciar porque la lista vive en memoria. Las respuestas conservan el formato del ejercicio, incluido el campo `mensage`; no hay un contrato de errores uniforme ni validación completa de entradas.

El servidor arranca con debug y no tiene autenticación. Úsalo solo como práctica local, no como servicio público. Las dependencias son las de la formación y esta revisión no cambia el comportamiento.

El siguiente paso de aquel aprendizaje está en [API_REST_ORM](https://github.com/CharlyCRM/API_REST_ORM), donde los productos se guardan con SQLAlchemy.
