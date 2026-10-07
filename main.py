from src.model.eventos import Aula
from src.model.pessoas import Aluno, Professor
from src.model.locais import Sala, Edificio
from src.model.estrutura import Curso, Disciplina, Turma, UnidadeAcademica

def main():
    print("--- Sistema Smart Campus Mackenzie ---")

    fci = UnidadeAcademica("Faculdade de Computação e Informática", "FCI")
    curso_cc = Curso("Ciência da Computação", "Bacharelado", 8)
    disciplina_ia = Disciplina("Inteligência Artificial", "IA001", 4)
    turma_ia = Turma("Turma IA 7CC", "IA7CC", disciplina_ia)

    gabriel = Aluno("Gabriel Ferreira", "000.000.000-00", "2000-01-01",
                    "gabriel.ferreira@mackenzie.br", "10442043", 7, 0.0)
    professor_ivan = Professor("Ivan Carlos Alcântara de Oliveira", "000.000.000-00",
                               "1970-01-01", "ivan.oliveira@mackenzie.br", "000000",
                               "Doutor", 40)

    predio_6 = Edificio("Prédio 6", True, "07:00-22:30", 6)
    sala_404 = Sala("Sala 404", True, "07:00-22:30", "404", 40, True)
    aula_ontologias = Aula("Aula de Ontologias", "2026-09-10 19:30", professor_ivan,
                           sala_404, "Presencial")

    relacoes = {
        "oferece": (fci, curso_cc),
        "matriculadoEm": (gabriel, curso_cc),
        "cursa": (gabriel, disciplina_ia),
        "pertenceA": (turma_ia, disciplina_ia),
        "ministra": (professor_ivan, turma_ia),
        "realizadoEm": (turma_ia, sala_404),
        "organiza": (professor_ivan, aula_ontologias),
        "ocorreEm": (aula_ontologias, sala_404),
    }

    print(f"Aluno: {gabriel.nome} - RA: {gabriel.tia_ra}")
    print(f"Unidade acadêmica: {fci.nome} ({fci.sigla})")
    print(f"Disciplina: {disciplina_ia.nome} - Código: {disciplina_ia.codigo}")
    print(f"Turma: {turma_ia.codigo_turma} - Sala: {sala_404.numero_sala}")
    print(f"Evento: {aula_ontologias.nome} - Professor: {professor_ivan.nome}")
    print(f"Relações modeladas: {', '.join(relacoes)}")
    print("--------------------------------------")

if __name__ == "__main__":
    main()
