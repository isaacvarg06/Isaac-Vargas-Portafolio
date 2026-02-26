from app.database import engine, Base
from app.models.project import Project

# Crear todas las tablas
Base.metadata.create_all(bind=engine)
print("✅ Tablas creadas exitosamente")