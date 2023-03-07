from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True)
    username = Column(String)
    senha = Column(String)
    ativo = Column(String)
    pessoas = relationship("Pessoa", back_populates="usuario")
    permissao = relationship("Permissao", back_populates="usuario")
    
class Pessoa(Base):
    __tablename__ = 'pessoa'
    id_pessoa = Column(Integer, primary_key=True)
    nome = Column(String)
    documento = Column(String)
    tipo_documento = Column(String)
    ativo = Column(Boolean)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    pessoa = relationship("Usuario", back_populates='pessoa')

class Permissao(Base):
    __tablename__ = 'permissao'
    id_permissao = Column(Integer, primary_key=True)
    nivel_permissao = Column(Integer)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    permissao = relationship("Usuario", back_populates='permissao')

class Conhecimento(Base):
    __tablename__ = 'conhecimento'
    id_conhecimento = Column(Integer, primary_key=True)
    titulo = Column(String)
    texto_ajuda = Column(Text)
    anexos = relationship("Anexo", back_populates="conhecimento")
    relacionados = relationship("Relacionados", back_populates='conhecimento')

class Anexo(Base):
    __tablename__ = 'anexo'
    id_anexo = Column(Integer, primary_key=True)
    anexo = Column(Text)
    id_conhecimento = Column(Integer, ForeignKey('conhecimento.id_conhecimento'))
    anexo_r = relationship("Conhecimento", back_populates='anexo')

class Relacionados(Base):
    __tablename__ = 'relacionados'
    id_relacao = Column(Integer, primary_key=True)
    id_conhecimento_base = Column(Integer, ForeignKey('conhecimento.id_conhecimento'))
    id_conhecimento_relacionado = Column(Integer, ForeignKey('conhecimento.id_conhecimento'))
    conhecimento = relationship("Conhecimento", back_populates='relacionados')