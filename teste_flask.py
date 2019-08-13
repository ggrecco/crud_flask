from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:123@localhost:5433/teste',
                       convert_unicode=True,
                       echo=False)
# __table_args = {'schema': 'conf'}
print(engine.table_names())
Base = declarative_base()
Base.metadata.reflect(engine)

from sqlalchemy.orm import relationship, backref


class Usuarios(Base):
    __tablename__ = 'tb_usuarios'
    __table__ = Base.metadata.tables['coisa']
    __table_args__ = {'schema': 'conf'}


if __name__ == '__main__':
    from sqlalchemy.orm import scoped_session, sessionmaker, Query
    db_session = scoped_session(sessionmaker(bind=engine))

    for item in db_session.query(Usuarios.id, Usuarios.name):
        print(item)