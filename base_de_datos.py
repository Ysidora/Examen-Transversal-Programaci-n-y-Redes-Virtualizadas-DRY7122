# Importar gestión de claves
from cryptography.fernet import Fernet
import hashlib

# Importar uso de base de datos SQL (SQLite)
import sqlite3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '¡Sitio web creado correctamente en el puerto 5800!'

if __name__ == '__main__':
    app.run(port=5800)

# Función para hashear la contraseña
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Ejemplo de almacenamiento de usuario y contraseña hasheada
usuarios = {
    'usuario1': hash_password('password1'),
    'usuario2': hash_password('password2')
}

def validar_usuario(usuario, password):
    if usuario in usuarios:
        hashed_password = hash_password(password)
        if usuarios[usuario] == hashed_password:
            return True
    return False

# Ejemplo de validación
usuario = 'usuario1'
password = 'password1'
if validar_usuario(usuario, password):
    print(f'Usuario {usuario} validado correctamente.')
else:
    print(f'Usuario {usuario} no validado.')

import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Crear tabla de usuarios
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                (nombre TEXT PRIMARY KEY, hash_password TEXT)''')

# Insertar usuarios y contraseñas hasheadas
cursor.execute("INSERT INTO usuarios VALUES ('usuario1', ?)", (hash_password('password1'),))
cursor.execute("INSERT INTO usuarios VALUES ('usuario2', ?)", (hash_password('password2'),))

# Guardar cambios
conn.commit()

# Cerrar conexión
conn.close()

