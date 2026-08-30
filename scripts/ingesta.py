import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from config import GEMINI_MODEL

# Carga el archivo .env oculto
load_dotenv()

# Lee la clave de manera segura desde las variables de entorno
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Leemos el manual de reglas
with open("GEMINI.md", "r", encoding="utf-8") as archivo_reglas:
    reglas = archivo_reglas.read()

# 3. Recorremos todas las notas crudas en raw/
notas = sorted(f for f in os.listdir("raw") if f.endswith(".md"))

if not notas:
    print("No hay notas en raw/. Coloca ahí tus apuntes en formato .md.")

for nombre_archivo in notas:
    with open(os.path.join("raw", nombre_archivo), "r", encoding="utf-8") as archivo_nota:
        mi_nota = archivo_nota.read()

    instruccion = f"""
Lee esta nota cruda y conviértela en un resumen estructurado para mi Wiki.
Recuerda enlazar los conceptos importantes con [[dobles corchetes]].
Aquí está la nota:
{mi_nota}
"""

    print(f"El bibliotecario está leyendo y pensando sobre '{nombre_archivo}'...")

    # 4. Gemini procesa la información
    respuesta = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=instruccion,
        config=types.GenerateContentConfig(
            system_instruction=reglas,
            temperature=0.2 # Esto hace que sea preciso y no invente cosas
        )
    )

    # 5. Guardamos el resultado en la carpeta wiki, con el mismo nombre de archivo
    with open(os.path.join("wiki", nombre_archivo), "w", encoding="utf-8") as archivo_final:
        archivo_final.write(respuesta.text)

    print(f"¡Listo! '{nombre_archivo}' fue procesada y guardada en wiki/.")
