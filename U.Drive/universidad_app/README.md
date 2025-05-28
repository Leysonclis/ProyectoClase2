# Universidad App

Este proyecto es una aplicación de gestión de viajes para una universidad. Permite a los conductores publicar viajes y a los usuarios tomar esos viajes. Además, los usuarios pueden agregar un contacto (por ejemplo, un número de teléfono) al tomar un viaje.

## Características

- **Publicación de Viajes**: Los conductores pueden publicar viajes disponibles.
- **Toma de Viajes**: Los usuarios pueden ver y tomar los viajes publicados.
- **Agregar Contacto**: Al tomar un viaje, los usuarios pueden agregar un contacto para facilitar la comunicación.

## Estructura del Proyecto

```
universidad_app/
├── gestion_viajes/          # Aplicación para gestionar viajes
├── usuarios/                # Aplicación para gestionar usuarios
├── universidad_app/         # Configuración del proyecto Django
├── manage.py                # Herramienta de gestión del proyecto
└── requirements.txt         # Dependencias del proyecto
```

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd universidad_app
   ```

2. Crea un entorno virtual y actívalo:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Realiza las migraciones:
   ```
   python manage.py migrate
   ```

5. Inicia el servidor:
   ```
   python manage.py runserver
   ```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.