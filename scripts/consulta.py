import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Carga el archivo .env oculto
load_dotenv()

# Lee la clave de manera segura desde las variables de entorno
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Leemos tu base de conocimientos (la carpeta wiki)
with open("wiki/resumen_limpio.md", "r", encoding="utf-8") as f:
    mi_wiki = f.read()

# 3. Hazle una pregunta a tu Segundo Cerebro (puedes cambiar esta pregunta)
mi_pregunta = "¿Qué problemas tuve configurando el servidor de Minecraft y cómo se llama el modpack?"

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
    model='gemini-3.6-flash',
    contents=instruccion,
    config=types.GenerateContentConfig(
        temperature=0.1 # Muy baja para que sea súper literal y no invente
    )
)

print("\n🧠 RESPUESTA DE TU SEGUNDO CEREBRO:")
print(respuesta.text)
print("-" * 40)