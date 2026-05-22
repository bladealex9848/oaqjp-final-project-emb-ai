# Final project

# AI-Based Web Application Development and Deployment: Emotion Detection

Este repositorio contiene la solución completa para el **Proyecto Final del curso de Desarrollo y Despliegue de Aplicaciones Web Basadas en IA**. El proyecto consiste en el diseño, desarrollo, empaquetado, pruebas, despliegue y análisis estático de una aplicación web para la **detección de emociones** a partir de opiniones o comentarios de clientes, utilizando la API de Watson NLP y Flask como framework de servidor.

---

## 📝 Descripción del Proyecto

El sistema procesa texto proporcionado por el usuario en formato libre, analiza y puntúa cinco emociones básicas (**ira** (*anger*), **desagrado** (*disgust*), **miedo** (*fear*), **alegría** (*joy*) y **tristeza** (*sadness*)), e identifica la **emoción dominante** que se expresa en la declaración. 

El desarrollo se estructuró en 8 tareas secuenciales que cubren el ciclo de vida completo de la aplicación, desde la integración con la API de Watson NLP hasta el análisis estático del código fuente para el cumplimiento de estándares PEP 8.

---

## 🛠️ Tecnologías y Herramientas Utilizadas

*   **Lenguaje de Programación:** Python 3
*   **Framework Web:** Flask (v2.x/v3.x)
*   **Librerías de Terceros:** `requests` para peticiones HTTP a la API Watson NLP, `unittest` para pruebas de caja blanca
*   **Análisis Estático de Código:** `pylint` (alcanzando una puntuación perfecta de **10.00/10**)
*   **Control de Versiones y Despliegue:** Git y GitHub
*   **Interfaz de Usuario:** HTML5, CSS3, JavaScript (provistos en la plantilla original)

---

## 📂 Estructura del Directorio de Trabajo

```text
oaqjp-final-project-emb-ai/
├── EmotionDetection/                  # Paquete de Python creado para la detección de emociones
│   ├── __init__.py                    # Inicialización del paquete e importación de la función principal
│   └── emotion_detection.py           # Lógica de detección, petición HTTP y fallback offline
├── static/                            # Archivos estáticos de la interfaz web
│   └── mywebscript.js                 # Script JS para peticiones asíncronas a la API Flask
├── templates/                         # Plantillas HTML
│   └── index.html                     # Página principal de la interfaz de usuario
├── submission/                        # Carpeta de entregables oficiales (textos y capturas PNG)
├── server.py                          # Servidor web Flask principal (calificado 10/10 por PyLint)
├── test_emotion_detection.py          # Conjunto de pruebas unitarias automatizadas
├── README.md                          # Este archivo de documentación del proyecto
├── commit-simple.sh                   # Script auxiliar de Git para commits automáticos
└── Final-project-emb-ai-Mark-v1.md    # Guías e instrucciones del laboratorio
```

---

## 🚀 Detalle de las Tareas Completadas

### Tarea 1: Bifurcar y Clonar el Repositorio del Proyecto
Se realizó el fork del repositorio original de IBM Developer Skills Network a la cuenta personal de GitHub y se clonó localmente en la ruta de trabajo. Se editó el archivo `README.md` incluyendo el título exacto requerido para la evaluación automática: `Final project`.
*   *Respaldo Visual:* `submission/1_folder_structure.png` (Estructura de directorios inicial).

### Tarea 2: Crear una Aplicación de Detección de Emociones usando Watson NLP
Se creó el módulo `EmotionDetection/emotion_detection.py` definiendo la función `emotion_detector(text_to_analyze)`. Esta función se conecta a la API de Watson Emotion Predict y procesa la entrada de texto de manera asíncrona. Además, para garantizar la portabilidad y evitar fallos fuera del entorno de red de Skills Network, se implementó un mecanismo inteligente de **fallback offline (mocking basado en palabras clave)**.
*   *Código:* `submission/2a_emotion_detection`
*   *Respaldo Visual:* `submission/2a_emotion_detection.png` (Código implementado) y `submission/2b_application_creation.png` (Consola de Python importando y ejecutando la función en consola).

### Tarea 3: Formatear la Salida de la Aplicación
Se modificó la lógica en `emotion_detector` para decodificar la respuesta JSON y transformarla en un diccionario de Python. La función calcula dinámicamente cuál de las 5 emociones evaluadas tiene la mayor puntuación, asignando su clave al campo `dominant_emotion`.
*   *Código:* `submission/3a_output_formatting`
*   *Respaldo Visual:* `submission/3a_output_formatting.png` (Código modificado) y `submission/3b_formatted_output_test.png` (Prueba en consola confirmando respuesta estructurada y emoción dominante).

### Tarea 4: Empaquetar la Aplicación
Se empaquetó la aplicación creando el archivo `EmotionDetection/__init__.py`, permitiendo la importación directa y estructurada del detector como un paquete nativo de Python (`from EmotionDetection.emotion_detection import emotion_detector`).
*   *Respaldo Visual:* `submission/4a_packaging.png` (Vista combinada de `__init__.py` y la estructura del paquete) y `submission/4b_packaging_test.png` (Prueba de importación del paquete en shell y evaluación del enunciado *"I hate working long hours"* devolviendo la emoción dominante **anger**).

### Tarea 5: Ejecutar Pruebas Unitarias
Se desarrolló un conjunto robusto de pruebas unitarias (`test_emotion_detection.py`) heredando de `unittest.TestCase`. Se validó la correspondencia de enunciados con las emociones esperadas:
1.  *"I am glad this happened"* ➡️ **joy**
2.  *"I am really mad about this"* ➡️ **anger**
3.  *"I feel disgusted just hearing about this"* ➡️ **disgust**
4.  *"I am so sad about this"* ➡️ **sadness**
5.  *"I am really afraid that this will happen"* ➡️ **fear**
*   *Código:* `submission/5a_unit_testing`
*   *Respaldo Visual:* `submission/5a_unit_testing.png` (Código del test suite) y `submission/5b_unit_testing_result.png` (Resultado exitoso de ejecución en consola indicando `OK`).

### Tarea 6: Despliegue de la Aplicación Web usando Flask
Se creó el archivo de servidor web `server.py` que arranca una aplicación Flask en el puerto `5000` y expone el endpoint `/emotionDetector`. La ruta recupera el texto a través de un parámetro GET y retorna una cadena formateada para ser mostrada dinámicamente por `static/mywebscript.js`.
*   *Código:* `submission/6a_server`
*   *Respaldo Visual:* `submission/6a_server.png` (Código del servidor) y `submission/6b_deployment_test.png` (Prueba de uso en el navegador web con la oración *"I think I am having fun"* devolviendo alegría con una interfaz responsiva).

### Tarea 7: Incorporar Manejo de Errores
Se mejoró la resiliencia del sistema incorporando el control de cadenas vacías o espacios en blanco en la API Watson NLP. Si el texto de entrada es nulo o la API devuelve un código de estado `400 Bad Request`, `emotion_detector` retorna un diccionario con todos sus valores establecidos en `None`. Por su parte, el servidor Flask detecta si `dominant_emotion` es `None` y responde con el mensaje descriptivo *"¡Texto inválido! ¡Por favor, intenta de nuevo!"*.
*   *Código (Función):* `submission/7a_error_handling_function`
*   *Código (Servidor):* `submission/7b_error_handling_server`
*   *Respaldo Visual:* `submission/7a_error_handling_function.png` (Modificaciones en detector), `submission/7b_error_handling_server.png` (Modificaciones en servidor) y `submission/7c_error_handling_interface.png` (Interfaz web desplegando correctamente el error en rojo ante un input vacío).

### Tarea 8: Realizar Análisis de Código Estático (PyLint)
Se optimizó completamente el archivo `server.py` corrigiendo todas las observaciones del linter (líneas de comentarios iniciales de módulo, docstrings descriptivos para todas las funciones, corrección de nombres de variables y orden de importaciones). Esto permitió obtener una calificación de cumplimiento perfecta de **10.00/10**.
*   *Código:* `submission/8a_server_modified`
*   *Respaldo Visual:* `submission/8a_server_modified.png` (Servidor documentado conforme a PEP 8) y `submission/8b_static_code_analysis.png` (Salida de consola de `pylint server.py` confirmando la puntuación de `10.00/10`).

---

## 📂 Directorio de Entregables Generados (`submission/`)

Para facilitar el proceso de revisión y evaluación (tanto en la opción **AI-Graded** como en la opción **Peer-Graded**), se han guardado copias exactas y capturas de pantalla de cada fase del laboratorio dentro del directorio [submission](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/):

### Capturas de Pantalla (Peer-Graded)

| Código de Archivo | Descripción del Respaldo Visual | Enlace Local |
|:---|:---|:---|
| `1_folder_structure.png` | Estructura inicial de carpetas clonada. | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/1_folder_structure.png) |
| `2a_emotion_detection.png` | Código de la función inicial `emotion_detector`. | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/2a_emotion_detection.png) |
| `2b_application_creation.png` | Consola interactiva probando e importando el detector. | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/2b_application_creation.png) |
| `3a_output_formatting.png` | Código del detector con la salida formateada en diccionario. | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/3a_output_formatting.png) |
| `3b_formatted_output_test.png` | Consola demostrando la salida con dominant_emotion. | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/3b_formatted_output_test.png) |
| `4a_packaging.png` | Vista del archivo `__init__.py` y el árbol del directorio. | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/4a_packaging.png) |
| `4b_packaging_test.png` | Consola importando el paquete y testeando dominant_emotion. | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/4b_packaging_test.png) |
| `5a_unit_testing.png` | Código del archivo `test_emotion_detection.py`. | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/5a_unit_testing.png) |
| `5b_unit_testing_result.png` | Consola ejecutando las pruebas unitarias con éxito (OK). | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/5b_unit_testing_result.png) |
| `6a_server.png` | Código fuente inicial de la aplicación Flask en `server.py`. | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/6a_server.png) |
| `6b_deployment_test.png` | Aplicación funcionando en navegador con respuesta exitosa. | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/6b_deployment_test.png) |
| `7a_error_handling_function.png` | Manejo de errores implementado en la lógica del detector. | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/7a_error_handling_function.png) |
| `7b_error_handling_server.png` | Código de `server.py` controlando respuestas nulas de emoción. | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/7b_error_handling_server.png) |
| `7c_error_handling_interface.png` | Interfaz gráfica mostrando el mensaje de entrada inválida en rojo. | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/7c_error_handling_interface.png) |
| `8a_server_modified.png` | Código de `server.py` adaptado a los estándares de PyLint. | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/8a_server_modified.png) |
| `8b_static_code_analysis.png` | Consola con la ejecución de pylint indicando puntaje 10.00/10. | [Ver Imagen](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/8b_static_code_analysis.png) |

---

## 🏃 Instrucciones de Ejecución

### 1. Requisitos Previos e Instalación de Dependencias
Asegúrate de contar con Python 3 instalado en tu sistema. Luego, instala las librerías necesarias ejecutando en tu terminal:

```bash
pip install requests flask pylint
```

### 2. Ejecutar las Pruebas Unitarias
Para validar que las emociones se analicen correctamente y que la lógica del detector responda de forma consistente:

```bash
python3 test_emotion_detection.py
```
*Deberías ver una salida indicando que las 5 pruebas se ejecutaron exitosamente (`OK`).*

### 3. Iniciar el Servidor Web Flask
Inicia la aplicación ejecutando el archivo del servidor:

```bash
python3 server.py
```
Una vez que el servidor esté activo, abre tu navegador favorito y accede a:
[http://localhost:5000](http://localhost:5000)

Escribe cualquier frase en inglés (por ejemplo, *"I feel amazing today"* o *"I am so sad today"*) y haz clic en **Analyze Sentiment** para ver los resultados de forma dinámica en la pantalla.

### 4. Ejecutar el Análisis de Código Estático (PyLint)
Para comprobar el cumplimiento de estándares del servidor web, ejecuta:

```bash
pylint server.py
```
*El resultado reportará una calificación perfecta de **10.00/10**.*

---

## 🏢 Créditos y Licencia
*   **Autor de Solución:** Alexander Oviedo Fadul
*   **Autor del Laboratorio Base:** Ratima Raj Singh (IBM Corporation)
*   **Licencia:** Este proyecto se distribuye bajo los términos de la Licencia MIT (consulte el archivo [LICENSE](file:///Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/LICENSE) para más detalles).
