::page{title="Proyecto Final: Desarrollo y Despliegue de Aplicaciones Web Basadas en IA"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/IDSN-logo.png" width="200"> <br>

Tiempo Estimado: 1 hora 45 minutos

## Escenario

Has sido contratado como ingeniero de software por una empresa de comercio electrónico para crear una aplicación web basada en IA que realice análisis sobre la retroalimentación de los clientes para sus productos insignia. Para lograr este requisito, crearás un sistema de Detección de Emociones que procesa la retroalimentación proporcionada por el cliente en formato de texto y descifra la emoción asociada expresada.

## Introducción

En este proyecto final, serás evaluado sobre el conocimiento adquirido en todos los aspectos de la creación de aplicaciones y su despliegue web a lo largo de este curso, y utilizaremos las bibliotecas de IA de Watson embebibles para crear una aplicación de detección de emociones.

La detección de emociones amplía el concepto de análisis de sentimientos al extraer emociones más sutiles, como alegría, tristeza, ira, y así sucesivamente, de las declaraciones en lugar de la simple polaridad que proporciona el análisis de sentimientos. Esto convierte a la detección de emociones en una rama de estudio muy importante, y las empresas utilizan ampliamente tales sistemas para sus sistemas de recomendación basados en IA, chatbots automatizados, y más.

## Directrices del proyecto

Para completar este proyecto, deberás realizar las siguientes 8 tareas, basadas en el conocimiento que has adquirido a lo largo del curso.

<b>Nota</b>: Esta plataforma no es persistente. Se recomienda que mantengas una copia de tu código en tus máquinas locales y guardes los cambios de vez en cuando. En caso de que vuelvas al laboratorio, necesitarás recrear los archivos en este entorno de laboratorio, utilizando las copias guardadas de tus máquinas.</p>			  

## Tareas y objetivos:
- Tarea 1: Hacer un fork y clonar el repositorio del proyecto
- Tarea 2: Crear una aplicación de detección de emociones utilizando la biblioteca NLP de Watson
- Tarea 3: Formatear la salida de la aplicación
- Tarea 4: Empaquetar la aplicación
- Tarea 5: Ejecutar pruebas unitarias en tu aplicación
- Tarea 6: Desplegar como aplicación web utilizando Flask
- Tarea 7: Incorporar manejo de errores
- Tarea 8: Ejecutar análisis de código estático

¡Comencemos!

::page{title="Nota"}

1. Por favor, asegúrate de que todas las actualizaciones y cambios realizados durante cada tarea estén debidamente completados y guardados antes de proceder a los siguientes pasos.  

2. Como se mencionó en el *“Resumen del Proyecto Final”*, puedes enviar tus entregables del proyecto a través de la Opción 1: Envío y Evaluación Calificada por IA o la Opción 2: Envío y Evaluación Calificada por Pares.

3. **Para la Opción 1: Envío y Evaluación Calificada por IA:**  
   El envío requiere: 
   - **URL del repositorio de GitHub** bajo **Tarea 1** y **Tarea 4 (Actividad 1)**.  
   - **Fragmentos de código** bajo **Tareas 2 a 8** para **Actividad 1**, y bajo **Tarea 7** para **Actividades 1 y 2** (excluyendo la Tarea 4).  
   - **Salidas de terminal** bajo **Tareas 2 a 4** y **Tarea 8** para **Actividad 2**.  
   - **Capturas de pantalla** bajo **Tarea 6** para **Actividad 2** y **Tarea 7** para **Actividad 3**.

4. **Para la Opción 2: Envío y Evaluación Calificada por Pares:**  
   - El envío requiere **capturas de pantalla** para todas las actividades bajo **Tareas 1 a 8**.  
   
> **Por favor, ejecuta este laboratorio en el **entorno del Laboratorio Theia de Skills Network**, no en tu IDE local (como VS Code). La API utilizada aquí está alojada en la plataforma Skills Network y solo es accesible dentro del Laboratorio Theia.** 

 ##

::page{title="Tarea 1: Hacer un fork y clonar el repositorio del proyecto"}

El repositorio de GitHub del proyecto está disponible en la URL mencionada a continuación.  
Como primer paso, necesitas hacer un fork de este repositorio, haz clic en el botón Fork en la esquina superior derecha de la página del repositorio.

```bash
https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai.git
```


*Puedes encontrar instrucciones sobre cómo bifurcar el repositorio visitando el ejercicio 2 en este [Laboratorio Práctico: Familiarízate con los comandos de Git](https://cf-courses-data.static.labs.skills.network/9Yqz09lYagTH_Eo5c9BXqQ/Get%20familiar%20with%20Git%20Commands-v1.md.html).*

>Nota: Asegúrate de que tu repositorio bifurcado sea Público. Esta acción creará una copia del repositorio bifurcado dentro de tu cuenta de GitHub.
1. Abre una nueva Terminal y crea el directorio `final_project` usando el comando mkdir.

2. Clona este repositorio de GitHub bifurcado utilizando la terminal de Cloud IDE a tu proyecto en una carpeta llamada `final_project`.
*Puedes encontrar instrucciones sobre cómo obtener la URL de clonación del repositorio visitando el ejercicio 3 en este [Laboratorio Práctico: Familiarízate con los comandos de Git](https://cf-courses-data.static.labs.skills.network/9Yqz09lYagTH_Eo5c9BXqQ/Get%20familiar%20with%20Git%20Commands-v1.md.html).*
3. Después de que la clonación esté completa, utiliza la terminal para cambiar al directorio actual `final_project`.

4. Ve a tu repositorio bifurcado y abre el README.md y agrega el nombre del proyecto en el archivo como `Final project`. Asegúrate de usar este nombre exacto, ya que es necesario para la entrega calificada por IA.

5. **Evaluación:**

   **Para la Opción 1 - Entrega y Evaluación Calificada por IA**: Copia y guarda la URL pública del repositorio de GitHub del archivo README.md, que contiene el nombre del proyecto `Final project` para la entrega y evaluación del proyecto final.

   **Para la Opción 2 - Entrega y Evaluación Calificada por Compañeros**: Toma una **captura de pantalla** de la estructura de tu carpeta y guárdala como `1_folder_structure.png` para la tarea de compañeros.

::page{title="Tarea 2: Crear una aplicación de detección de emociones utilizando la biblioteca Watson NLP"}

Las bibliotecas Watson NLP están integradas. Por lo tanto, no es necesario importarlas a tu código. Solo necesitas enviar una solicitud POST a la función correcta en la biblioteca y recibir la salida.

1. Para este proyecto, utilizarás la función <b>Emotion Predict</b> de la biblioteca Watson NLP. Para acceder a esta función, la URL, los encabezados y el formato json de entrada son los siguientes.

	```
	URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
	Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
	Input json: { "raw_document": { "text": text_to_analyze } }
	```

	Nota que `text_to_analyze` se está utilizando como una variable que contiene el texto escrito que necesita ser analizado.

2. Crea un archivo llamado `emotion_detection.py` en la carpeta `final_project`.
3. En el archivo `emotion_detection.py`, escribe la función para ejecutar la detección de emociones utilizando la función de Detección de Emociones apropiada. Nombra esta función `emotion_detector`.

	**Nota:** Supón que el texto a analizar se pasa a la función como un argumento y se almacena en la variable `text_to_analyze`. El valor que se devuelve debe ser el atributo `text` del objeto de respuesta recibido de la función de Detección de Emociones.

4. **Evaluación:**

   **Para Opción 1 - Envío y Evaluación Calificada por IA**: Copia y pega el código del archivo emotion_detection.py que muestra la función de la aplicación en un archivo de texto y guárdalo como `2a_emotion_detection` para la entrega y evaluación del proyecto final.

   **Para Opción 2 - Envío y Evaluación Calificada por Pares**: Toma una **captura de pantalla** del código que escribiste y guárdalo como `2a_emotion_detection.png` para la tarea de pares.

5. La aplicación ahora debería ser importable usando el intérprete de Python. Abre un intérprete `python3`.

6. Importa la aplicación. 

7. Después de importar la aplicación con éxito, prueba tu aplicación con el texto: <b>"Me encanta esta nueva tecnología."</b>

8. **Evaluación:**

   **Para Opción 1 - Envío y Evaluación Calificada por IA**: Copia y pega la salida del terminal que muestra que la aplicación fue importada y probada sin errores en un archivo de texto y guárdalo como `2b_application_creation` para la entrega y evaluación del proyecto final.

   **Para Opción 2 - Envío y Evaluación Calificada por Pares**: Toma una **captura de pantalla** del terminal con los tres pasos incluidos junto con la salida final. Nombra este archivo `2b_application_creation.png` para la tarea de pares.

Nota: En caso de que el intérprete de Python muestre un error `ModuleNotFoundError: No module named 'requests'`, puedes instalar la biblioteca `requests` en tu IDE utilizando el siguiente comando en el terminal.

```
python3 -m pip install requests
```


**Opcional:**

En cualquier momento, si deseas enviar tu código a tu repositorio de GitHub bifurcado, puedes hacerlo siguiendo las instrucciones proporcionadas en este [enlace](https://cf-courses-data.static.labs.skills.network/9Yqz09lYagTH_Eo5c9BXqQ/Get%20familiar%20with%20Git%20Commands-v1.md.html).

::page{title="Tarea 3: Formatear la salida de la aplicación"}

1. Convierte el texto de respuesta en un diccionario utilizando las funciones de la biblioteca `json`.

	Nota el formato del contenido en este diccionario.
	
2. Extrae el conjunto requerido de emociones, incluyendo ira, desagrado, miedo, alegría y tristeza, junto con sus puntuaciones.

3. Escribe la lógica del código para encontrar la emoción dominante, que es la emoción con la puntuación más alta.

4. Luego, modifica la función `emotion_detector` para devolver el siguiente formato de salida.

```
{
'anger': anger_score,
'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion': '<name of the dominant emotion>'
}
```


5. **Evaluación:**

   **Para la Opción 1 - Envío y Evaluación Calificada por IA**: Copia y pega el código del archivo emotion_detection.py que muestra que la función emotion_detector modificada devuelve el formato de salida correcto en un archivo de texto y guárdalo como `3a_output_formatting` para la presentación y evaluación del proyecto final.

   **Para la Opción 2 - Envío y Evaluación Calificada por Pares**: Toma una **captura de pantalla** del código de la función modificada y guárdala como `3a_output_formatting.png` para la tarea de pares.

6. Prueba la aplicación en el shell de `python3` nuevamente, con la declaración <b>Estoy tan feliz de estar haciendo esto</b>.

7. Verifica que la respuesta recibida tenga la emoción dominante como <b>alegría</b>.

8.  **Evaluación:**

    **Para la Opción 1 - Envío y Evaluación Calificada por IA**: Copia y pega la salida del terminal que muestra que el formato de salida es preciso en un archivo de texto y guárdalo como `3b_formatted_output_test` para la presentación y evaluación del proyecto final.

     **Para la Opción 2 - Envío y Evaluación Calificada por Pares**: Toma una **captura de pantalla** de la salida del shell del terminal y guárdala como `3b_formatted_output_test.png` para la tarea de pares.

**Opcional**

En cualquier momento si deseas subir tu código a tu repositorio de GitHub bifurcado, puedes hacerlo siguiendo las instrucciones proporcionadas en este [enlace](https://cf-courses-data.static.labs.skills.network/9Yqz09lYagTH_Eo5c9BXqQ/Get%20familiar%20with%20Git%20Commands-v1.md.html).

::page{title="Tarea 4: Empaquetar la aplicación"}

En esta tarea, empaquetarás la aplicación creada en los pasos anteriores.

1. Realiza los pasos relevantes para la creación del paquete. Establece el nombre del paquete como `EmotionDetection`.

2. **Evaluación:**

   **Para Opción 1 - Envío y Evaluación Calificada por IA**: Asegúrate de haber subido tu archivo `__init__.py` a tu repositorio de GitHub bifurcado siguiendo las instrucciones [link](https://cf-courses-data.static.labs.skills.network/9Yqz09lYagTH_Eo5c9BXqQ/Get%20familiar%20with%20Git%20Commands-v1.md.html) en el enlace proporcionado. Luego, copia y guarda la URL pública de GitHub del archivo `__init__.py` que contiene el código para importar el módulo de la aplicación para la entrega y evaluación del proyecto final.

   **Para Opción 2 - Envío y Evaluación Calificada por Pares**: Toma una captura de pantalla del contenido del archivo init junto con la estructura final de carpetas del directorio final_project. Asegúrate de que ambas imágenes quepan en una sola captura de pantalla y nómbrala `4a_packaging.png` para la tarea de pares.

3. Para asegurarte de que `EmotionDetection` es un paquete válido, necesitas probar el paquete. Para hacer esto:
		<ol><li>Ejecuta un shell de python en la terminal.</li> 		
		<li>Importa la función `emotion_detector` del paquete.</li>		
		<li>Si el paquete se creó correctamente, no recibirás ningún mensaje de error.</li>   		
		<li>Ejecuta la función nuevamente con la frase <b>Odio trabajar muchas horas</b>.</li> 		
		<li>Verifica que la salida muestre la emoción dominante como <b>ira</b>.</li> </ol>

4. **Evaluación:**

   **Para Opción 1 - Envío y Evaluación Calificada por IA**: Copia y pega la salida de la terminal que valida que EmotionDetection es un paquete válido y guárdala como `4b_packaging_test` para la entrega y evaluación del proyecto final.

   **Para Opción 2 - Envío y Evaluación Calificada por Pares**: Toma una **captura de pantalla** de esta salida de la terminal y guárdala como `4b_packaging_test.png` para la tarea de pares.

::page{title="Tarea 5: Ejecutar pruebas unitarias en tu aplicación"}

Con una aplicación funcional disponible, ahora necesitas ejecutar pruebas unitarias para validar la salida de la aplicación.

1. Para ejecutar pruebas unitarias, crea un nuevo archivo, `test_emotion_detection.py` que llame a la función de aplicación requerida del paquete y la pruebe para las siguientes declaraciones y emociones dominantes.

	|Declaración|Emoción Dominante|
	|-----------|-----------------|
	|Me alegra que esto haya sucedido|alegría|
	|Estoy realmente enojado por esto|ira|
	|Me siento disgustado solo de escuchar sobre esto|desagrado|
	|Estoy tan triste por esto|tristeza|
	|Tengo mucho miedo de que esto suceda|miedo|

2. **Evaluación:**
   **Para Opción 1 - Envío y Evaluación Calificada por IA**: Copia y pega el código del archivo test_emotion_detection.py que muestra las pruebas unitarias requeridas en un archivo de texto y guárdalo como `5a_unit_testing` para la entrega y evaluación del proyecto final.

    **Para Opción 2 - Envío y Evaluación Calificada por Pares**: Toma una **captura de pantalla** del código y guárdalo como `5a_unit_testing.png` para la tarea de pares.

3. Ejecuta el archivo `test_emotion_detection.py` en la terminal.

4. Verifica la salida de la prueba unitaria para confirmar que las pruebas unitarias han pasado.

5. **Evaluación:**
   **Para Opción 1 - Envío y Evaluación Calificada por IA**: Copia y pega la salida de la terminal que muestra que todas las pruebas unitarias pasaron en un archivo de texto y guárdalo como `5b_unit_testing_result` para la entrega y evaluación del proyecto final.

    **Para Opción 2 - Envío y Evaluación Calificada por Pares**: Toma una **captura de pantalla** de la salida y guárdala como `5b_unit_testing_result.png` para la tarea de pares.

**Opcional:**

En cualquier momento si deseas enviar tu código a tu repositorio de GitHub bifurcado, puedes hacerlo siguiendo las instrucciones proporcionadas en este [enlace](https://cf-courses-data.static.labs.skills.network/9Yqz09lYagTH_Eo5c9BXqQ/Get%20familiar%20with%20Git%20Commands-v1.md.html).

::page{title="Tarea 6: Despliegue web de la aplicación utilizando Flask"}

Después de que todas las pruebas se completen con éxito, necesitas desplegar la aplicación en la web. Esto permitirá al cliente acceder y utilizar la aplicación.

**Nota:** *El archivo `index.html` en la carpeta `templates` y el archivo `mywebscript.js` en la carpeta `static` han sido proporcionados como parte del repositorio. Estos archivos no necesitan ser actualizados en este proyecto.*

1. Debes crear el archivo `server.py` desde cero. Ten en cuenta los siguientes requisitos de esta tarea.

	**Nota:** `server.py` es parte de la carpeta `final_project`.

2. Asegúrate de que el decorador de Flask para la función de llamada de la aplicación sea `/emotionDetector`.

3. El cliente ha solicitado que la salida se muestre en el formato que se muestra en el ejemplo a continuación. 

	**Ejemplo de Salida** 
	Supongamos que deseas evaluar la declaración `Amo mi vida`. La declaración se procesa de la siguiente manera:

	```
	{
	"anger": 0.006274985, 
	"disgust": 0.0025598293, 
	"fear": 0.009251528, 
	"joy": 0.9680386, 
	"sadness": 0.049744144, 
	"dominant_emotion":"joy"
	}
	```

	La respuesta se muestra como:

	<p style="font-family: Courier new" style="color:DodgerBlue;">Para la declaración dada, la respuesta del sistema es 'anger': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 y 'sadness': 0.049744144. La emoción dominante es <b>joy</b>. </p>

4. La aplicación necesita ser desplegada en `localhost:5000`.

5. **Evaluación:**

    **Para Opción 1 - Envío y Evaluación Calificada por IA**: Copia y pega el código del archivo server.py que muestra el despliegue web de la aplicación utilizando Flask en un archivo de texto y guárdalo como `6a_server` para la entrega y evaluación del proyecto final.

    **Para Opción 2 - Envío y Evaluación Calificada por Pares**: Toma una captura de pantalla del contenido final de server.py y nómbrala `6a_server.png` para la tarea de pares.

6.  **Evaluación :**  Toma una captura de pantalla de la aplicación desplegada final, probándola con la declaración "Creo que me estoy divirtiendo". Nombra esta imagen como `6b_deployment_test.png` tanto para Opción 1 - entrega y evaluación del proyecto final como para Opción 2 - Envío Calificado por Pares.

**Opcional:**

En cualquier momento que desees subir tu código a tu repositorio de GitHub bifurcado, puedes hacerlo siguiendo las instrucciones proporcionadas en este [enlace](https://cf-courses-data.static.labs.skills.network/9Yqz09lYagTH_Eo5c9BXqQ/Get%20familiar%20with%20Git%20Commands-v1.md.html).

::page{title="Tarea 7: Incorporar Manejo de Errores"}

Incorpora la capacidad de manejo de errores en tu función `emotion_detector` para gestionar entradas en blanco de los usuarios, es decir, ejecutar la aplicación sin ninguna entrada.

1. Accede al atributo `status_code` de la respuesta del servidor para mostrar correctamente la respuesta del sistema para entradas en blanco.
	
	Para `status_code = 400`, haz que la función devuelva el mismo diccionario, pero con valores para todas las claves siendo `None`. 

2.   **Evaluación:** 

      **Para Opción 1 - Envío y Evaluación Calificada por IA**: Copia y pega el código del archivo emotion_detection.py mostrando la función emotion_detector actualizada para el código de estado 400 en un archivo de texto y guárdalo como `7a_error_handling_function` para la entrega y evaluación del proyecto final.

       **Para Opción 2 - Envío y Evaluación Calificada por Compañeros**: Toma una captura de pantalla de la función modificada y nómbrala `7a_error_handling_function.png` para la tarea de compañeros.

3. Modifica `server.py` para incorporar el manejo de errores cuando `dominant_emotion` es `None`. En este escenario, la respuesta debería mostrar un mensaje <b>¡Texto inválido! ¡Por favor, intenta de nuevo!</b>. 

4. **Evaluación:**

   **Para Opción 1 - Envío y Evaluación Calificada por IA**: Copia y pega el código del archivo server.py mostrando el manejo de errores de entrada en blanco en un archivo de texto y guárdalo como `7b_error_handling_server` para la entrega y evaluación del proyecto final.

      **Para Opción 2 - Envío y Evaluación Calificada por Compañeros**: Toma una captura de pantalla de este archivo editado y guárdalo como `7b_error_handling_server.png` para la tarea de compañeros.

5. Despliega la aplicación y pruébala para entradas en blanco.

6. La salida debería mostrar el mensaje de error, <b>¡Texto inválido! ¡Por favor, intenta de nuevo!</b>. 

4. **Evaluación:** 
   
   Toma una **captura de pantalla** de la salida mostrando el mensaje de error y nómbrala `7c_error_handling_interface.png` tanto para Opción 1 - entrega del proyecto final y evaluación como para Opción 2 - Envío Calificado por Compañeros.

**Opcional:**

En cualquier momento si deseas subir tu código a tu repositorio de GitHub bifurcado, puedes hacerlo siguiendo las instrucciones proporcionadas en este [enlace](https://cf-courses-data.static.labs.skills.network/9Yqz09lYagTH_Eo5c9BXqQ/Get%20familiar%20with%20Git%20Commands-v1.md.html).

::page{title="Tarea 8: Ejecutar análisis de código estático"}

Finalmente, es hora de verificar la conformidad del código.

1. Ejecuta el análisis de código estático en el código que creaste. Usa la biblioteca PyLint en el archivo `server.py` e intenta generar una puntuación de 10/10. Tendrás que modificar el archivo `server.py` para obtener esta puntuación.

   **Evaluación:**
   
   **Para la Opción 1 - Envío y Evaluación Calificada por IA**: Copia y pega el código del archivo server.py que demuestra la ejecución del análisis de código estático en un archivo de texto y guárdalo como `8a_server_modified` para la presentación y evaluación del proyecto final.

     **Para la Opción 2 - Envío y Evaluación Calificada por Pares**: Toma una captura de pantalla del archivo modificado y nómbrala como `8a_server_modified.png` para la tarea de pares.

	**Nota:** La diferencia entre una puntuación de 9/10 y una puntuación de 10/10 puede ser el uso de Docstrings. Incluye Docstrings en todas las funciones de tu código.

2.   **Evaluación:**
     
     **Para la Opción 1 - Envío y Evaluación Calificada por IA**: Copia y pega la salida del terminal que muestra una puntuación perfecta para el análisis de código estático en un archivo de texto y guárdalo como `8b_static_code_analysis` para la presentación y evaluación del proyecto final.

      **Para la Opción 2 - Envío y Evaluación Calificada por Pares**: Toma una captura de pantalla de una salida de 10/10 en el terminal después de ejecutar el análisis de código estático. Nombra la captura de pantalla como `8b_static_code_analysis.png` para la tarea de pares.

::page{title="Lista de Verificación de Envío"}

Sigue la lista de verificación a continuación para verificar que tu proyecto cumpla con todos los requisitos antes de la entrega.
	
**Envía tu trabajo a través de la Opción 1: Envío y Evaluación Calificada por IA o la Opción 2: Envío y Evaluación Calificada por Pares, dependiendo del camino de envío que elijas para la evaluación del proyecto.**

Sigue la lista de verificación de envío a continuación si estás procediendo con **Opción 1: Envío y Evaluación Calificada por IA**:

**-Tarea 1: Envía la URL del repositorio de GitHub**

* Envía la URL pública del repositorio de GitHub del archivo README.md, que contiene los detalles del nombre del proyecto.

**-Tarea 2: Crea una aplicación de detección de emociones utilizando la biblioteca Watson NLP**

* Actividad 1: Envía el código del archivo emotion_detection.py que muestra la función de la aplicación.
* Actividad 2: Envía la salida del terminal que muestra que la aplicación fue importada y probada sin errores.

**-Tarea 3: Formatea la salida de la aplicación**

* Actividad 1: Envía el código del archivo emotion_detection.py que muestra que la función emotion_detector modificada devuelve el formato de salida correcto.
* Actividad 2: Envía la salida del terminal que muestra que el formato de salida es preciso.

**-Tarea 4: Valida el paquete EmotionDetection**

* Actividad 1: Envía la URL pública del repositorio de GitHub del archivo **init**.py que incluye el código para importar el módulo de la aplicación.
* Actividad 2: Envía la salida del terminal validando que EmotionDetection es un paquete válido.

**-Tarea 5: Ejecuta pruebas unitarias en tu aplicación**

* Actividad 1: Envía el código del archivo test_emotion_detection.py que muestra las pruebas unitarias requeridas.
* Actividad 2: Envía la salida del terminal que muestra que todas las pruebas unitarias pasaron.

**-Tarea 6: Despliegue web de la aplicación utilizando Flask**

* Actividad 1: Envía el código del archivo server.py que muestra el despliegue web de la aplicación utilizando Flask.
* Actividad 2: Sube la captura de pantalla llamada 6b_deployment_test.png que muestra el despliegue de la aplicación.

**-Tarea 7: Incorpora manejo de errores**

* Actividad 1: Envía el código del archivo emotion_detection.py que muestra la función emotion_detector actualizada para el código de estado 400.
* Actividad 2: Envía el código del archivo server.py que muestra el manejo de errores de entrada en blanco.
* Actividad 3: Sube la captura de pantalla llamada 7c_error_handling_interface.png que valida la funcionalidad de manejo de errores.

**-Tarea 8: Ejecuta análisis de código estático**

* Actividad 1: Envía el código del archivo server.py que demuestra la ejecución del análisis de código estático.
* Actividad 2: Envía la salida del terminal que muestra una puntuación perfecta para el análisis de código estático.

Sigue la lista de verificación de envío a continuación si estás procediendo con **Opción 2: Envío y Evaluación Calificada por Pares**:

Por favor, asegúrate de verificar que has capturado todas las imágenes según lo indicado durante el transcurso del proyecto. Aquí hay un resumen rápido de lo requerido.

**Tarea 1: Clona el repositorio del proyecto**

`1_folder_structure.png`

**Tarea 2: Crea una aplicación de detección de emociones utilizando la biblioteca Watson NLP**

`2a_emotion_detection.png`
`2b_application_creation.png`

**Tarea 3: Formatea la salida de la aplicación**

`3a_output_formatting.png`
`3b_formatted_output_test.png`

**Tarea 4: Empaqueta la aplicación**

`4a_packaging.png`
`4b_packaging_test.png`

**Tarea 5: Ejecuta pruebas unitarias en tu aplicación**

`5a_unit_testing.png`
`5b_unit_testing_result.png`

**Tarea 6: Despliega como aplicación web utilizando Flask**

`6a_server.png`
`6b_deployment_test.png`

**Tarea 7: Incorpora manejo de errores**

`7a_error_handling_function.png`
`7b_error_handling_server.png`
`7c_error_handling_interface.png`

**Tarea 8: Ejecuta análisis de código estático**

`8a_server_modified.png`
`8b_static_code_analysis.png`

**Opcional:**

Si deseas enviar tu código a tu repositorio de GitHub bifurcado, puedes hacerlo siguiendo las instrucciones proporcionadas en este [enlace](https://cf-courses-data.static.labs.skills.network/9Yqz09lYagTH_Eo5c9BXqQ/Get%20familiar%20with%20Git%20Commands-v1.md.html). Esto asegura que puedas revisar tu trabajo fácilmente cuando sea necesario.

::page{title="Conclusión"}

Felicitaciones por completar el proyecto.

Al completar este proyecto, has:

1. Creado una aplicación de Detección de Emociones utilizando las funciones de bibliotecas de IA embebibles.

2. Extraído información relevante de la salida recibida de la función.

3. Probado y empaquetado la aplicación creada utilizando la función de Detección de Emociones.

4. Completado el despliegue web de tu aplicación utilizando Flask.

5. Incorporado manejo de errores en tu aplicación para tener en cuenta entradas inválidas.

6. Escrito códigos que cumplen perfectamente con las directrices PEP8, obteniendo un puntaje de 10/10 en análisis de código estático.

	
## Author(s)

### Ratima Raj Singh
## <h3 align="center"> © IBM Corporation. Todos los derechos reservados. <h3/>