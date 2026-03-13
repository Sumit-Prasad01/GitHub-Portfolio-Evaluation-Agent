"""
Initialize database and create all tables.
Run this script once before starting the application.
"""

from app.core.database import engine
from app.models.db_models import Base


def init_db():
    print("Creating database tables...")

    Base.metadata.create_all(bind=engine)

    print("Database initialized successfully!")


if __name__ == "__main__":
    init_db()