import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from config import GEMINI_MODEL

# Carga el archivo .env oculto
load_dotenv()

# Lee la clave de manera segura desde las variables de entorno
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def leer_nota(nombre_archivo):
    with open(os.path.join("wiki", nombre_archivo), "r", encoding="utf-8") as f:
        return f.read()

# 2. Leemos tu base de conocimientos (todas las notas en la carpeta wiki)
notas_wiki = sorted(f for f in os.listdir("wiki") if f.endswith(".md"))
mi_wiki = "\n\n".join(leer_nota(nombre) for nombre in notas_wiki)

# 3. Hazle una pregunta a tu Segundo Cerebro (puedes cambiar esta pregunta)
mi_pregunta = "¿Qué base de datos elegí para mi proyecto personal y por qué?"

# 4. Le damos la instrucción estricta a Gemini
instruccion = f"""
Eres la interfaz de consulta de mi Segundo Cerebro. 
Responde a mi pregunta basándote ÚNICAMENTE en la siguiente información de mis notas. 
No uses información externa. Si la respuesta no está en las notas, di que no lo sabes.

Notas de mi wiki:
{mi_wiki}

Mi pregunta: {mi_pregunta}
"""

print("Buscando en tus notas...")

# 5. Gemini genera la respuesta
respuesta = client.models.generate_content(
    model=GEMINI_MODEL,
    contents=instruccion,
    config=types.GenerateContentConfig(
        temperature=0.1 # Muy baja para que sea súper literal y no invente
    )
)

print("\n🧠 RESPUESTA DE TU SEGUNDO CEREBRO:")
print(respuesta.text)
print("-" * 40)