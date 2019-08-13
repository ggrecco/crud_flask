from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
engine = create_engine(DATABASE_URI)