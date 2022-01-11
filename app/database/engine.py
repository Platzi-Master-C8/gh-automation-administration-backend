from sqlmodel import create_engine

from app.database.connections import get_uri

uri = get_uri()
engine = create_engine(uri)
