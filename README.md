## TODO 8 — Pruebas de autenticación y permisos

Comando ejecutado:

```powershell
uv run pytest -c app/pytest.ini app/tests/test_demo.py -q
```

Resultado: 3 passed in 7.28s, sin advertencias.

Las pruebas verifican el registro de usuarios, la asignación del autor
desde el token y los permisos para crear, editar y eliminar publicaciones.

La primera ejecución produjo advertencias por la longitud de la clave JWT.
Se configuró una clave aleatoria mediante la variable de entorno SECRET_KEY
en PowerShell y se repitieron las pruebas correctamente. La clave no se
incluye en el repositorio y debe configurarse nuevamente en otra sesión.


## Clase 3 — TODO 7 y 8: pruebas de likes

Se incorporaron las pruebas en app/tests/test_likes.py,
conservando las pruebas anteriores de test_demo.py.

Comando:
uv run pytest -c app/pytest.ini app/tests -q

Resultado: 12 passed in 14.05s, sin advertencias.

Se verificaron los contadores, dar y quitar likes de forma
idempotente, los listados, los permisos y la eliminación de
likes asociados al borrar una publicación.

El test del TODO 8 se tomó de la solución docente y se corrigió
la comprobación de la respuesta del like agregando assert.
No se registró una ejecución inicial antes de implementar los TODO.