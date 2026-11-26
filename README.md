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