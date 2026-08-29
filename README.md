```markdown
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
│   ├── ingesta.py       # Script de transformación y estructuración con IA
│   └── consulta.py     # Interfaz de consulta contextual sobre la wiki
│
├── .env                  # Credenciales privadas (Ignorado en Git)
├── .gitignore            # Configuración de seguridad y privacidad
├── GEMINI.md             # Manual de reglas y directivas del sistema
└── README.md             # Documentación principal

```

---

## 🚀 Guía de Instalación Rápida

### 1. Clonar el repositorio

```bash
git clone [https://github.com/CesarY10/gemini-second-brain.git](https://github.com/CesarY10/gemini-second-brain.git)
cd gemini-second-brain

```

### 2. Instalar dependencias

```bash
py -m pip install google-genai python-dotenv

```

### 3. Configurar credenciales

Crea un archivo llamado `.env` en la raíz del proyecto y añade tu clave de acceso:

```env
GEMINI_API_KEY=tu_api_key_real_aqui

```

### 4. Uso del Sistema

* **Ingesta:** Coloca tus notas crudas en la carpeta `raw/` y ejecuta el script:
```bash
py scripts/ingesta.py

```


* **Consulta:** Realiza preguntas directas a tu base de conocimientos ejecutando:
```bash
py scripts/consulta.py

```



---

## 🛡️ Privacidad y Seguridad

Las carpetas de contenido personal (`raw/` y `wiki/`) junto con el archivo de credenciales (`.env`) se encuentran completamente excluidos del control de versiones mediante `.gitignore`. Este repositorio funciona como una **plantilla segura** lista para ser clonada por cualquier usuario.

```

### Pasos finales:
1. Reemplaza todo el contenido de tu `README.md` en VS Code con este código de arriba.
2. Guarda los cambios con **`Ctrl + S`**.
3. Haz el **Commit** y el **Push** desde tu pestaña de Source Control en VS Code.
4. Recarga tu página de GitHub y verás que ahora sí aparecen los iconos de colores de los badges y un diseño limpio y profesional.

```