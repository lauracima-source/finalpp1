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

Inicialmente copié el test del TODO 8 de la solución docente
sin modificarlo. En una revisión posterior agregué el assert
que faltaba para comprobar que la respuesta al dar like fuera 200.
Volví a ejecutar las pruebas: 12 aprobadas en 11,43 segundos,
sin advertencias en esa ejecución.

No registré una ejecución inicial antes de implementar los TODO.

## Clase 4 — TODO 8 y 9: pruebas de seguimiento y feed

Incorporé las pruebas en app/tests/test_follow.py, conservando
las pruebas de las clases anteriores.

El archivo copiado ya incluía resuelto el test del TODO 9.
Verifica que las listas de seguidores y seguidos no estén invertidas.

Comando ejecutado:
uv run pytest -c app/pytest.ini app/tests -q

Resultado: 22 pruebas aprobadas en 24,07 segundos, sin advertencias
en esa ejecución.

También se verificaron los contadores, la idempotencia del seguimiento,
el rechazo del auto seguimiento, el contenido del feed y que la cantidad
de consultas SQL no aumente al seguir a más usuarios.

No registré una ejecución inicial con fallos antes de implementar
las funcionalidades.