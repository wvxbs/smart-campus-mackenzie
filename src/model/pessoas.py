class Pessoa:
    def __init__(self, nome: str, cpf: str, data_nascimento: str, email_institucional: str):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.email_institucional = email_institucional

class Aluno(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: str, email_institucional: str,
                 tia_ra: str, semestre_atual: int, indice_rendimento: float):
        super().__init__(nome, cpf, data_nascimento, email_institucional)
        self.tia_ra = tia_ra
        self.semestre_atual = semestre_atual
        self.indice_rendimento = indice_rendimento

class Professor(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: str, email_institucional: str,
                 dr_registro: str, titulacao: str, carga_horaria: int):
        super().__init__(nome, cpf, data_nascimento, email_institucional)
        self.dr_registro = dr_registro
        self.titulacao = titulacao
        self.carga_horaria = carga_horaria

class Visitante(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: str, email_institucional: str,
                 motivo_visita: str):
        super().__init__(nome, cpf, data_nascimento, email_institucional)
        self.motivo_visita = motivo_visita
