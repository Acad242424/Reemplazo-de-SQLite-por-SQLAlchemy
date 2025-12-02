from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_USER = "tu_usuario"
DB_PASSWORD = "tu_contraseña"
DB_HOST = "localhost"
DB_NAME = "biblioteca"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
