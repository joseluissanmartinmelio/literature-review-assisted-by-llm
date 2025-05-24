# Revisión de literatura con LLMs

## Descripción

Esta es una aplicación cuya finalidad es facilitar la revisión de grandes corpus de literatura, especialmente, en ciencias sociales. El proceso consisten en extraer el texto de un pdf, evadir el header del texto (puede sensibilizarse en el código fuente), integrar el texto a una ventana de contexto para algún modelo de lenguage natural utilizando el paquete Openai (openai y deepseek). Los prompts consigandos tienen dos funciones, la primera es realizar un resumen general del texto, incorporando los principales argumentos teóricos y la metodología utilizada junto a sus principales resultados, la segunda función es extraer la revisión de literatura del texto, obteniendo una lista de los/as autores/as citados y las principales ideas asociadas a ellos/as.

## Tecnologías usadas

LLM: GPT-4o-mini; DeepSeek-V3	
Librerias: PyMuPDF; Openai

## Instalación

```bash
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo
pip install -r requirements.txt
```

## Cómo usar

1. Coloca tu archivo PDF en la carpeta deseada (por defecto: test/).
2. Asegúrate de tener configurado tu archivo de prompt en prompts/ (hay dos prompts por defecto)
3. Ejecuta el script main.py:

```bash
python main.py
```

El script hará lo siguiente:

*1. Extraer el texto principal del PDF, ignorando encabezados.*

*2. Calcular estadísticas de palabras (totales, únicas, más frecuentes).*

*3. Se genera la tarea requerida al LLM.*

*4. Volver a calcular estadísticas sobre el texto generado.*

*5. Guardar la salida en un archivo .md con el nombre del autor y año del artículo.*

Puedes modificar el prompt fácilmente cambiando el archivo en esta línea del código:

```python
prompt_path = "prompts/summarize_prompt.txt"
```

# TODO

1. Trabajando en una interfaz simple
2. Estableciendo algunas métricas pra medir el rendimiento con distintos modelos de LLM de código abierto y de paga.