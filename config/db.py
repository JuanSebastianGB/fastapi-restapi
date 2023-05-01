from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()


URL = getenv("DATABASE_URL")
print(URL)
engine = create_engine(URL, echo=True)

Base = declarative_base()

session = sessionmaker(bind=engine, autocommit=False,
                       autoflush=False, expire_on_commit=False)
