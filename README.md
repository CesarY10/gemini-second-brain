# 🧠 AI-Powered Second Brain
### Un sistema de conocimiento personal automatizado, impulsado por Obsidian y la API de Google Gemini.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Obsidian](https://img.shields.io/badge/Obsidian-Knowledge%20Base-7c3aed?style=for-the-badge&logo=obsidian&logoColor=white)](https://obsidian.md/)
[![Gemini API](https://img.shields.io/badge/Google%20Gemini-API-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## 💡 Sobre el Proyecto
Este proyecto implementa la arquitectura **"LLM Wiki"** para la gestión de conocimiento personal. Separa estrictamente el contenido en bruto de la síntesis estructurada, permitiendo automatizar la ingesta y consulta de notas mediante inteligencia artificial sin comprometer la privacidad local.

---

## 🛠️ Arquitectura y Tecnologías
| Componente | Tecnología / Herramienta | Propósito |
| :--- | :--- | :--- |
| **Interfaz de Usuario** | Obsidian + Gemini Scribe | Interacción visual y navegación mediante enlaces tipo wiki (`[[links]]`). |
| **Automatización** | Python (`google-genai`, `python-dotenv`) | Procesamiento backend, ingesta de notas y consultas contextuales. |
| **Modelo de IA** | Google Gemini (`gemini-flash`) | Análisis semántico, estructuración y control alucinatorio estricto. |
| **Control de Versiones** | Git / GitHub | Gestión de código fuente y distribución de plantillas. |

---

## 📂 Estructura del Repositorio
```text
My_Second_Brain/
│
├── raw/                  # Apuntes desordenados y borradores (Ignorado en Git)
├── wiki/                 # Base de conocimientos estructurada (Ignorado en Git)
├── scripts/
│   ├── config.py        # Constantes compartidas (ej. modelo de Gemini)
│   ├── ingesta.py       # Script de transformación y estructuración con IA
│   └── consulta.py     # Interfaz de consulta contextual sobre la wiki
│
├── .env                  # Credenciales privadas (Ignorado en Git)
├── .env.example          # Plantilla de variables de entorno
├── .gitignore            # Configuración de seguridad y privacidad
├── requirements.txt      # Dependencias de Python
├── GEMINI.md             # Manual de reglas y directivas del sistema
└── README.md             # Documentación principal
```

---

## 🚀 Guía de Instalación Rápida

### 1. Clonar el repositorio
```bash
git clone https://github.com/CesarY10/gemini-second-brain.git
cd gemini-second-brain
```

### 2. Instalar dependencias

**Windows:**
```bash
py -m pip install -r requirements.txt
```

**macOS / Linux:**
```bash
python3 -m pip install -r requirements.txt
```

### 3. Configurar credenciales
Copia `.env.example` a `.env` y añade tu clave de acceso real:

```bash
cp .env.example .env
```

```env
GEMINI_API_KEY=tu_api_key_real_aqui
```

### 4. Uso del Sistema
* **Ingesta:** Coloca todas tus notas crudas (`.md`) dentro de `raw/` y ejecuta el script. Cada nota se procesa y se guarda en `wiki/` con el mismo nombre de archivo:
  * Windows: `py scripts/ingesta.py`
  * macOS / Linux: `python3 scripts/ingesta.py`

* **Consulta:** Edita la variable `mi_pregunta` en `scripts/consulta.py` con tu pregunta y ejecútalo:
  * Windows: `py scripts/consulta.py`
  * macOS / Linux: `python3 scripts/consulta.py`

---

## 🛡️ Privacidad y Seguridad
Las carpetas de contenido personal (`raw/` y `wiki/`) junto con el archivo de credenciales (`.env`) se encuentran completamente excluidos del control de versiones mediante `.gitignore`. Este repositorio funciona como una **plantilla segura** lista para ser clonada por cualquier usuario.