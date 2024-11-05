@echo off


cd "C:\Users\Pañol Pc\Documents\Gestor-TIP-Web"


call venv\Scripts\activate
start chrome http://127.0.0.1:5000
python run.py


