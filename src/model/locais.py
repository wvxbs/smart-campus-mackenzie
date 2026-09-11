class Local:
    def __init__(self, nome: str, acessivel_pcd: bool, horario_funcionamento: str):
        self.nome = nome
        self.acessivel_pcd = acessivel_pcd
        self.horario_funcionamento = horario_funcionamento

class Edificio(Local):
    def __init__(self, nome: str, acessivel_pcd: bool, horario_funcionamento: str,
                 numero_predio: int):
        super().__init__(nome, acessivel_pcd, horario_funcionamento)
        self.numero_predio = numero_predio

class EspacoAberto(Local):
    def __init__(self, nome: str, acessivel_pcd: bool, horario_funcionamento: str,
                 tipo_espaco: str):
        super().__init__(nome, acessivel_pcd, horario_funcionamento)
        self.tipo_espaco = tipo_espaco

class Acesso(Local):
    def __init__(self, nome: str, acessivel_pcd: bool, horario_funcionamento: str,
                 tipo_acesso: str):
        super().__init__(nome, acessivel_pcd, horario_funcionamento)
        self.tipo_acesso = tipo_acesso

class Sala(Local):
    def __init__(self, nome: str, acessivel_pcd: bool, horario_funcionamento: str,
                 numero_sala: str, capacidade_pessoas: int, possui_ar_condicionado: bool):
        super().__init__(nome, acessivel_pcd, horario_funcionamento)
        self.numero_sala = numero_sala
        self.capacidade_pessoas = capacidade_pessoas
        self.possui_ar_condicionado = possui_ar_condicionado

class Servico(Local):
    def __init__(self, nome: str, acessivel_pcd: bool, horario_funcionamento: str,
                 tipo_servico: str):
        super().__init__(nome, acessivel_pcd, horario_funcionamento)
        self.tipo_servico = tipo_servico
