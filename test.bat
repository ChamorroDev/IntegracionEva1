@echo off
REM Activar el entorno virtual
cd ..
cd entorno-virtual
call Scripts\activate.bat

REM Navegar al directorio del proyecto Django
cd ..
cd IntegracionEva1-1

REM Ejecutar el servidor de desarrollo de Django
python manage.py runserver

REM Mantener la ventana abierta
pause
