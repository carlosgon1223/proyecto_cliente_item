#!/bin/bash

pip install -r requirements.txt


# Iniciar la aplicación con Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000
