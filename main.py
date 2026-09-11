from src.model.pessoas import Aluno, Professor
from src.model.locais import Sala, Edificio
from src.model.estrutura import Curso, Disciplina

def main():
    print("--- Sistema Smart Campus Mackenzie ---")
    
    # Criando instancias da Estrutura
    curso_cc = Curso(nome="Ciência da Computação", tipo="Bacharelado", duracao_semestres=8)
    disciplina_ia = Disciplina(nome="Inteligência Artificial", codigo="CC3100", creditos=4)
    
    # Criando instancias de Pessoa
    aluno = Aluno(nome="João Silva", cpf="123.456.789-00", data_nascimento="2000-01-01", 
                  email_institucional="joao@mackenzie.br", tia_ra="3214567", 
                  semestre_atual=5, indice_rendimento=8.5)
                  
    professor = Professor(nome="Maria Souza", cpf="987.654.321-00", data_nascimento="1980-05-10", 
                          email_institucional="maria@mackenzie.br", dr_registro="123456", 
                          titulacao="Doutora", carga_horaria=40)
                          
    # Criando instancias de Local
    predio_31 = Edificio(nome="Prédio 31 - FCI", acessivel_pcd=True, 
                         horario_funcionamento="07:00-22:30", numero_predio=31)
                         
    sala_415 = Sala(nome="Laboratório de IA", acessivel_pcd=True, 
                    horario_funcionamento="07:00-22:30", numero_sala="415", 
                    capacidade_pessoas=40, possui_ar_condicionado=True)
                    
    print(f"Aluno: {aluno.nome} - TIA: {aluno.tia_ra}")
    print(f"Professor: {professor.nome} - Titulação: {professor.titulacao}")
    print(f"Disciplina: {disciplina_ia.nome} - Créditos: {disciplina_ia.creditos}")
    print(f"Sala: {sala_415.nome} (Capacidade: {sala_415.capacidade_pessoas} alunos) no {predio_31.nome}")
    print("--------------------------------------")

if __name__ == "__main__":
    main()
