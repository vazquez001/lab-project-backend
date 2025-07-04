#!/usr/bin/env bash
# exit on error
set -o errexit

# --- INICIO DE LA DEPURACIÓN ---
echo "--- Listando archivos y carpetas en el directorio raíz ---"
ls -la
echo "--- FIN DE LA DEPURACIÓN ---"

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate