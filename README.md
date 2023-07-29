
## Bot de Discord para consultar artículos en el área de la salud

## Tabla de contenido

- [Bot de Discord para consultar artículos en el área de la salud](#Bot-de-Discord-para-consultar-artículos-en-el-área-de-la-salud)
  
  - [Tabla de contenido](#Tabla-de-contenido)
  - [Descripción](#Descripción)
  - [Instalación](#Instalación)
  - [Uso y ejemplos](#uso-y-ejemplos)
  - [Futuras mejoras](#Futuras-mejoras)


## Descripción 

La información en el campo de la salud se actualiza constantemente, por lo que es fundamental estar al tanto de los últimos artículos publicados sobre temas específicos.
Nuestro bot de Discord te permite obtener un archivo con los últimos artículos relacionados con palabras clave que ingreses.

Los artículos son obtenidos de los siguientes sitios:

**PubMed**: Es un motor de búsqueda de libre acceso que te permite consultar principalmente los contenidos de la base de datos MEDLINE. También puedes acceder a una variedad de revistas científicas de similar calidad, que no forman parte de MEDLINE. A través de este buscador, puedes obtener referencias bibliográficas y resúmenes de investigaciones biomédicas.

**BVsalud**: Biblioteca Virtual de Salud (BVS) fue establecida en 1998 como modelo, estrategia y plataforma operacional de cooperación técnica de la Organización Panamericana de la Salud (OPS) para la gestión de información y conocimiento en salud en la Región de América Latina y el Caribe (AL&C).
BVS es una Red de Redes construida de manera colaborativa y coordinada por BIREME. Se desarrolla de forma descentralizada a través de instancias nacionales (como BVS Argentina, BVS Brasil, etc.) y redes temáticas de instituciones relacionadas con la investigación, la enseñanza o los servicios (como BVS Enfermería, BVS Ministerio de Salud, etc.).

¡Consulta los últimos avances en salud con nuestro bot de Discord y mantente actualizado en tu campo de interés!

## Archivos del proyecto
**bot.ipynb**: Es el archivo principal del bot
**pubmed_scraper.py**: Scraper del buscador PUBMED (https://pubmed.ncbi.nlm.nih.gov/)
**bvsalud_scraper**: Scraper del buscador BVsalud (https://bvsalud.org/en/)
**read_cred.py**: Lector de claves secretas

## Instalación 
1. Asegurate de tener instalado python en tu sistema y descarga la aplicacion de Discord
2. Creacion del bot de Discord 
   Ingresa a https://discord.com/developers/applications, crea una nueva aplicacion en 'New Application'
   Dale un nombre a ti aplicacion y haz click en 'Create'
   En la pestaña 'Bot' en la izquierda, haz click en 'Add Bot'  y confirma.
   Copia el token que se encuentra la seccion 'Token'. Este token es esencial para el funionamiento de tu bot y debe mantenerse secreto.
3. Clona este repositorio: 'git clone https://github.com/Analia2020/discord_bot'
4. Ingresa a la carpeta del proyecto discord_bot
5. Configura un nuevo entorno virtual e instala 'requirements.txt'
6. Configura tu archivo credentials.yaml con el token que obtuviste previamente. Agregalo a un archivo .gitignore
7. Ejecuta el archivo bot.ipynb
   
## Uso
Estos son los comandos para usar el bot:

**+pubmed**palabra y/o palabras claves 

**+bvsalud** palabra y/o palabras claves

**+adios** para salir

**+hola** para comenzar de nuevo si saliste

Ejemplos: 

Busqueda en Pubmed

![Busqueda en Pubmed](https://github.com/Analia2020/discord_bot/blob/main/discord_pubmed.jpg)

Busqueda en BVsalud

![Busqueda en BVsalud](https://github.com/Analia2020/discord_bot/blob/main/discord_bvsalud.jpg)

## Futuras mejoras
**Optimización del código**: Realizar una revisión exhaustiva del código para mejorar la eficiencia y la legibilidad

**Implementación de bot en whatsapp**: Configurar un bot en whatsapp
