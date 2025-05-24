# This file contains the prompt for the OpenAI API.

## Summary a complete paper

```python
prompt = (
f"""
Asume el rol de un investigador experto en ciencias sociales con experiencia redactando artículos académicos. Tu tarea es analizar un artículo de investigación empírica en ciencias sociales. A partir del texto completo del artículo, identifica los hallazgos más relevantes del estudio, así como cualquier inferencia clave que se desprenda de la argumentación del autor.

Redacta un único párrafo expositivo, adecuado para integrarse en la sección teórica de un artículo académico. Utiliza un tono argumentativo y formal, destacando las ideas centrales de forma sintética, coherente y articulada. No hagas listados ni bullet points.Enfócate únicamente en los hallazgos sustantivos y en su relevancia teórica.

Si el artículo contiene resultados estadísticos, consigna el método e integra los resultados de una forma interpretativa, no las cifras crudas.
Al final, asegúrate de que el párrafo pueda leerse como una síntesis conceptual relevante para sustentar una discusión teórica o un marco analítico.
Acá va el texto:

{context}
""")
```

## Extract the authors from literature review

```python
prompt = (
f"""
1. Asume el rol de un investigador experto en ciencias sociales con habilidades avanzadas en análisis de textos académicos. Tu tarea es leer un artículo académico y extraer todas las referencias a autores que el texto menciona explícitamente como parte del marco teórico, discusión o antecedentes.

2. No incluyas referencias que sean meramente formales o que no tengan contenido conceptual asociado como aquellas consignadas en la bibliografía.

3. Para cada autor citado (o conjunto de autores), identifica la idea que se les atribuye. Estas ideas deben aparecer explícitamente o poder inferirse de la redacción del artículo.

4. Entrega el resultado en formato de lista con viñetas (bullet points), siguiendo exactamente este formato de elementos separados por ";":
"Apellido/s; año; idea afirmada de forma concisa"
Ejemplo:
"Bourdieu; 1984; el capital cultural influye en la reproducción de desigualdades"

5. Si alguna idea está asociada a varios autores, consigna todos los autores con comas simples. Como en el siguiente ejemplo:
"Putnam(2000) y Gutierrez(2010) afirman que el capital social se ha erosionado en las últimas décadas". En este caso, la respuesta sería:
"Putnam,Perez y Gutierrez; 2000,2010; el capital social se ha erosionado en las últimas décadas"

6. Este listado debe ser útil para reconstruir el mapa teórico que el artículo utiliza o discute.

Acá va el artículo:

{context}
""")
```