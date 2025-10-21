# 🏭 Sistema MRP - Planificación de Requerimientos de Materiales

## 📋 Descripción del Proyecto

Sistema desarrollado en Excel con VBA que automatiza el proceso de Planificación de Requerimientos de Materiales (MRP). A partir de las Listas de Materiales (BOM) y demandas del cliente, calcula automáticamente el Plan Maestro de Producción (MPS) y los requerimientos de materiales.

## 🎯 Objetivo

Automatizar los cálculos de planificación de producción.

## ⚙️ Funcionalidades Principales

- **📊 Entrada de BOM:** Carga y gestión de Listas de Materiales
- **📈 Cálculo de MPS:** Generación automática del Plan Maestro de Producción
- **📦 Gestión de Inventarios:** Cálculo de necesidades netas considerando stock disponible
- **⏱ Planificación Temporal:** Distribución de requerimientos por períodos

## 🛠 Tecnologías Utilizadas

- **Microsoft Excel** (Interfaz principal)
- **VBA (Visual Basic for Applications)** (Lógica de negocio y automatización)

## 🚀 Cómo Usar

1. **Pestaña 1: Portada:**
   - Simplemente visual con un botón que te lleva a la segunda pestaña

2. **Pestaña 2: Dades**
   - Ingreso manual de los datos del BOM (en la parte de abajo esta toda la información del BOM con una explicación detallada de lo que es cada elemento)
   - Botón llamado "crear taules" que sirve para crear las tablas (creadas en la pestaña 3: Tabla), al pulsar se pedirá información sobre el numero numero de niveles que tiene el BOM y cuantos elementos hay en cada uno de ellos
       - En el caso de probar la plantilla MRP.xslm el numero de niveles es 3, habiendo 2 elementos en el nivel 0, 6 elementos en el nivel 1 y 8 elementos en el nivel 2

3. **Pestaña 3: Taules**
   - Las tablas se crearan a la izquierda de la hoja, habiendo algunas celdas en blanco y otras en gris. Nosotros tendremos que llenar las celdas en gris para así luego calcular las celdas blancas
       - Para no tener que hacerlo uno a uno, mas a la derecha hay una tabla ya creada con estos datos, solo hay que copiarla y pegarla siguiendo los pasos que ya se indican en el propio excel
   - El botón llamado "Calcular quantitats i entregues" calcula los datos que nos faltan (las celdas blancas) a partir de los datos que hemos introducido previamente en las celdas grises
  
3. **Pestaña 4: MRP**
   - Aqui se genera el MPS final con todos los datos ya calculados. Es necesario primero pulsar el botón de "Cargar Información" para que el otro botón funcione correctamente
   - El botón llamado "Cargar Informació" sirve para cargar la información del BOM al MPS para así ya poder calcular el MPS
   - El botón llamado "Crear Periòdes" sirve para calcular toda la información del MPS
       - Este gracias a la información cargada del BOM y a la información de las tablas creadas anteriormente es capaç de crear el MPS calculando las cantiadades y tiempos de entregas para cada elemento


## 💡 Valor Añadido

Este proyecto demuestra:
- Capacidad para entender procesos empresariales complejos
- Pensamiento lógico para resolver problemas operativos
- Habilidades en automatización de procesos
- Conocimientos de excel y VBA

---

*¿Preguntas o sugerencias? ¡No dudes en contactarme!*
