from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()


class Book(Base):
    __tablename__ = 'tb_usuarios'
    pk_id_usuario = Column(Integer, primary_key=True)
    login = Column(String)
    nome = Column(String)

    def __repr__(self):
        return "<Book(Login='{}', nome='{}')>"\
                .format(self.login, self.nome)