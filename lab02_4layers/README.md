# Lab 2 - App de arquitectura de 4 Capas

Esta es una aplicación con una arquitectura de 4 capas, donde cada capa corre de manera independiente a través de contenedores Docker conectados a una misma red de Docker Compose. Además, los contenedores están relacionados mediante volúmenes con los directorios del repositorio para permitir la persistencia de datos y facilitar el desarrollo.
## Descripción del Proyecto

El sistema está compuesto por las siguientes capas:  
1. **Capa de Presentación**: Aplicación desarrollada en React, corriendo en el puerto `3000`.  
2. **Capa de Lógica de Negocio**: Implementada en NestJS, corriendo en el puerto `4000`.  
3. **Capa de Servicios**: También desarrollada en NestJS, corriendo en el puerto `5000`.  
4. **Capa de Acceso a Datos**: Base de datos PostgreSQL corriendo en el puerto `5432`.  

Todas las capas están interconectadas mediante una red definida en el archivo de configuración de Docker Compose.

---

## Prerrequisitos

Antes de ejecutar esta aplicación, asegúrate de tener instalados los siguientes componentes:  
- [Docker](https://www.docker.com/)  
- [Docker Compose](https://docs.docker.com/compose/)  

---

## Pasos para Ejecutar la Aplicación

1. Clona este repositorio en tu máquina local:  
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```
   
2. Verifica que Docker y Docker Compose estén correctamente instalados:
   ```
   docker --version
   docker-compose --version
   ```
3. Construye, ejecuta los contenedores y los scriptas de creación y poblamiento de la base de datos usando Docker Compose:
   ```
   docker-compose up --build
   ```
4. Una vez que los contenedores estén en ejecución, puedes acceder a la aplicación a través de :
   - Capa de Presentación (React): http://localhost:3000
  
## Comandos Adicionales

- Para detener los contenedores sin eliminarlos, utiliza:  
   ```
   docker-compose stop
   ```
- Si deseas reiniciar los contenedores después de detenerlos, usa:
   ```
   docker-compose up
   ```
- Si necesitas detener y eliminar los contenedores, la red y los volúmenes asociados, utiliza:
   ```
   docker-compose down
   ```
- Si realizas cambios en la configuración o dependencias y necesitas reconstruir todo, ejecuta:
   ```
   docker-compose up --build
   ```
