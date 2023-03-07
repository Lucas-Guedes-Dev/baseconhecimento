from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, DeclarativeBase, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True)
    username = Column(String)
    senha = Column(String)
    ativo = Column(String)
    pessoas = relationship("Pessoa", back_populates="usuario")
    
class Pessoa(Base):
    __tablename__ = 'pessoa'
    id_pessoa = Column(Integer, primary_key=True)
    nome = Column(String)
    documento = Column(String)
    tipo_documento = Column(String)
    ativo = Column(Boolean)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    pessoa = relationship("Usuario", back_populates='pessoa')