from sqlalchemy import create_engine, inspect, func, select
from sqlalchemy.orm import declarative_base, sessionmaker
import os


Base = declarative_base()

def init_db():
    """Initialize database if tables don't exist."""
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWD')

    if not username or not password:
        raise ValueError("Database credentials not found in environment variables")

    database_url = f"mysql+pymysql://{username}:{password}@localhost/spotidb"
    engine = create_engine(database_url)

    # Import the models to register them with Base
    from .Album import Album
    from .Artist import Artist
    from .Track import Track
    from .Stream import Stream

    # Create only tables that don't exist
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()

    # Create tables that don't exist yet
    Base.metadata.create_all(engine, checkfirst=True)

    # Return engine and session maker for potential usage
    Session = sessionmaker(bind=engine)
    return engine, Session





