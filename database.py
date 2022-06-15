import os

import dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# init dotenv
dotenv.load_dotenv()

if os.getenv("STAGE") == "prd":
    user_db = os.getenv("DB_USER_PRD")
    pass_db = os.getenv("DB_PASS_PRD")
    host_db = os.getenv("DB_HOST_PRD")
    name_db = os.getenv("DB_NAME_PRD")

else:
    user_db = os.getenv("DB_USER_DEV")
    pass_db = os.getenv("DB_PASS_DEV")
    host_db = os.getenv("DB_HOST_DEV")
    name_db = os.getenv("DB_NAME_DEV")

SQLALCHEMY_DATABASE_URL = f"postgresql://{user_db}:{pass_db}@{host_db}/{name_db}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
