class Estrutura:
    def __init__(self, nome: str):
        self.nome = nome

class UnidadeAcademica(Estrutura):
    def __init__(self, nome: str, sigla: str):
        super().__init__(nome)
        self.sigla = sigla

class Curso(Estrutura):
    def __init__(self, nome: str, tipo: str, duracao_semestres: int):
        super().__init__(nome)
        self.tipo = tipo
        self.duracao_semestres = duracao_semestres

class Disciplina(Estrutura):
    def __init__(self, nome: str, codigo: str, creditos: int):
        super().__init__(nome)
        self.codigo = codigo
        self.creditos = creditos

class Turma(Estrutura):
    def __init__(self, nome: str, codigo_turma: str, disciplina: Disciplina):
        super().__init__(nome)
        self.codigo_turma = codigo_turma
        self.disciplina = disciplina
