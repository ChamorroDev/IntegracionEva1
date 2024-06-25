@echo off
REM Activar el entorno virtual
cd /d "C:\Users\alexa\OneDrive\Documentos\Github\entorno-virtual"
call Scripts\activate.bat

REM Navegar al directorio del proyecto Django
cd /d "C:\Users\alexa\OneDrive\Documentos\Github\IntegracionEva1-1
REM Ejecutar el servidor de desarrollo de Django
py manage.py runserver

REM Mantener la ventana abierta
pause
