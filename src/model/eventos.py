from .pessoas import Pessoa
from .locais import Local

class Evento:
    def __init__(self, nome: str, data_hora: str, organizador: Pessoa, local: Local):
        self.nome = nome
        self.data_hora = data_hora
        self.organizador = organizador
        self.local = local

class Aula(Evento):
    def __init__(self, nome: str, data_hora: str, organizador: Pessoa, local: Local,
                 tipo_aula: str):
        super().__init__(nome, data_hora, organizador, local)
        self.tipo_aula = tipo_aula

class Avaliacao(Evento):
    def __init__(self, nome: str, data_hora: str, organizador: Pessoa, local: Local,
                 tipo_avaliacao: str):
        super().__init__(nome, data_hora, organizador, local)
        self.tipo_avaliacao = tipo_avaliacao

class EventoExtracurricular(Evento):
    def __init__(self, nome: str, data_hora: str, organizador: Pessoa, local: Local,
                 tema: str):
        super().__init__(nome, data_hora, organizador, local)
        self.tema = tema
