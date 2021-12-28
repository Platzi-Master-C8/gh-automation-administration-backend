from sqlmodel import create_engine

DB_FILE = "/code/app/database/gh-aut-admin-api.db"
DB_URL = f"sqlite:///{DB_FILE}"

engine = create_engine(DB_URL)
