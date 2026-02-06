# Isaac-Vargas-Portafolio
Portafolio web personal desarrollado con React, FastAPI y PostgreSQL.  Incluye panel de administración con CRUD para gestión de contenido y  soporte multiidioma (ES/EN).



# 🚀 Portfolio Full-Stack

Portafolio web personal desarrollado con tecnologías modernas para 
mostrar mis proyectos y experiencia como desarrollador.

![Portfolio Preview](screenshot.png)

## ✨ Características

- 🎨 Diseño responsive y moderno
- 🌐 Soporte multiidioma (Español/Inglés)
- 🔐 Panel de administración con autenticación JWT
- ✏️ Sistema CRUD para gestión de contenido
- ⚡ API REST documentada automáticamente
- 🎯 Optimizado para SEO

## 🛠️ Tecnologías

### Frontend
- React.js
- React Router
- i18next (internacionalización)
- Axios
- Tailwind CSS

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication
- Pydantic

## 📋 Prerequisitos

- Node.js (v18+)
- Python (v3.10+)
- PostgreSQL (v14+)

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tuusuario/portfolio-fullstack.git
cd portfolio-fullstack
```

### 2. Configurar Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Crear archivo `.env`:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/portfolio_db
SECRET_KEY=tu-clave-secreta
ALGORITHM=HS256
```

Ejecutar migraciones y servidor:
```bash
python app/main.py
```

### 3. Configurar Frontend
```bash
cd frontend
npm install
npm start
```

## 📁 Estructura del Proyecto
```
portfolio-fullstack/
├── frontend/          # Aplicación React
├── backend/           # API FastAPI
├── docs/              # Documentación
└── README.md
```

## 🔗 API Endpoints

La documentación interactiva está disponible en:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📸 Screenshots

![Home](docs/screenshots/home.png)
![Projects](docs/screenshots/projects.png)
![Admin Panel](docs/screenshots/admin.png)

## 🚀 Deployment

- **Frontend**: Vercel
- **Backend**: Railway
- **Database**: Railway PostgreSQL

## 📝 Licencia

MIT License - ver [LICENSE](LICENSE)

## 👤 Autor

**Tu Nombre**
- GitHub: [isaacvarg06](https://github.com/isaacvarg06)
- LinkedIn: [Isaac Esteban Vargas](https://www.linkedin.com/in/isaac-esteban-vargas-a021b4303/)
- Email: vargasisaac556@gmail.com

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor abre un issue primero 
para discutir los cambios que te gustaría hacer.

---

⭐ Si te gustó este proyecto, ¡dale una estrella en GitHub!
