```markdown
# 🧠 AI-Powered Second Brain (Gemini + Obsidian)

Un sistema de gestión de conocimiento personal automatizado basado en el patrón "LLM Wiki" (popularizado por Andrej Karpathy), construido utilizando **Python**, la **API oficial de Google Gemini** y **Obsidian**.

## 🚀 Características
- **Separación de Capas:** Aislamiento estricto entre documentos de entrada crudos (`raw/`) y conocimiento sintetizado (`wiki/`).
- **Ingesta Automatizada (`ingesta.py`):** Procesa notas desordenadas aplicando un manual de reglas de estructuración y enlazado inteligente.
- **Consulta Contextual (`consulta.py`):** Interfaz para consultar directamente tu base de conocimientos sin salir de la terminal.
- **Integración Visual:** Soporte directo con Obsidian y plugins de IA para una experiencia fluida.

## 📁 Estructura del Proyecto

```text
My_Second_Brain/
│
├── raw/               # Apuntes desordenados y borradores (Ignorado en Git)
├── wiki/              # Base de conocimientos estructurada y enlazada (Ignorado en Git)
├── scripts/
│   ├── ingesta.py     # Script para procesar notas crudas con Gemini
│   └── consulta.py    # Script para consultar el segundo cerebro
│
├── .env               # Credenciales privadas (Ignorado en Git)
├── .gitignore         # Configuración de exclusión para privacidad
├── GEMINI.md          # Manual de reglas y esquema del sistema para la IA
└── README.md          # Documentación del proyecto

```

## ⚙️ Configuración e Instalación

1. **Clona el repositorio:**
```bash
git clone [https://github.com/TU-USUARIO/TU-REPOSITORIO.git](https://github.com/TU-USUARIO/TU-REPOSITORIO.git)
cd My_Second_Brain

```


2. **Instala las dependencias de Python:**
```bash
py -m pip install google-genai python-dotenv

```


3. **Configura tus credenciales:**
Crea un archivo llamado `.env` en la raíz y añade tu API Key de Gemini:
```env
GEMINI_API_KEY=tu_api_key_aqui

```


4. **Uso:**
* Coloca tus notas en `raw/` y corre el script de ingesta: `py scripts/ingesta.py`
* Realiza consultas a tu cerebro digital ejecutando: `py scripts/consulta.py`



```

```