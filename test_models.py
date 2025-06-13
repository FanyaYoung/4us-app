import sys
import os
from pathlib import Path

# Add the backend directory to Python path
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend'))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app.db.base import Base, engine
from app.db.models.user import User

# Create all tables
Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")
print("User table columns:", [column.name for column in User.__table__.columns])
