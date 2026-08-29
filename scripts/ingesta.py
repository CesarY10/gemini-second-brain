import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Carga el archivo .env oculto
load_dotenv()

# Lee la clave de manera segura desde las variables de entorno
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Leemos el manual de reglas
with open("GEMINI.md", "r", encoding="utf-8") as archivo_reglas:
    reglas = archivo_reglas.read()

# 3. Leemos tu nota cruda y desordenada
with open("raw/nota_desordenada.md", "r", encoding="utf-8") as archivo_nota:
    mi_nota = archivo_nota.read()

instruccion = f"""
Lee esta nota cruda y conviértela en un resumen estructurado para mi Wiki.
Recuerda enlazar los conceptos importantes con [[dobles corchetes]].
Aquí está la nota:
{mi_nota}
"""

print("El bibliotecario está leyendo y pensando...")

# 4. Gemini procesa la información
respuesta = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=instruccion,
    config=types.GenerateContentConfig(
        system_instruction=reglas,
        temperature=0.2 # Esto hace que sea preciso y no invente cosas
    )
)

# 5. Guardamos el resultado en la carpeta wiki
with open("wiki/resumen_limpio.md", "w", encoding="utf-8") as archivo_final:
    archivo_final.write(respuesta.text)

print("¡Listo! Revisa tu carpeta wiki.")