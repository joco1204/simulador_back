# SIMULADOR CREDITO BACKEND

# Creación del entorno
```bash
python -m venv venv
```

# Activar entorno
1. **Windows**:
```bash
    .\venv\Scripts\activate 
```

2. **Linux**:
```bash
    source ./venv/Scripts/activate
```

# Instalar dependencias
```bash
pip install -r requirements.txt
```

# Variables de entorno, crear .env
```bash
DB_DRIVE="mysql"
DB_CONTROLLER="pymysql"
DB_HOST=""
DB_USER=""
DB_PASS=""
DB_NAME=""
DB_PORT=""
SECRET_KEY=""
```

# Iniciar BD
```bash
flask db init
```

# Migrar tablas
```bash
flask db migrate -m "Migrate tables"
```

# Actualizar BD
```bash
flask db upgrade
```
# Iniciar Aplicación
```bash
python run.py 
```
# URL y Puerto por defecto http://localhost:5000
