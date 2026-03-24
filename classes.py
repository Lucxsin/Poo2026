from datetime import datetime


class Campus:
    def __init__(self, nome: str, cidade: str):
        self.nome = nome
        self.cidade = cidade
        self.cursos = []  # relação: Campus 1:N Curso

    def adicionar_curso(self, curso):
        self.cursos.append(curso)

    def __repr__(self):
        return f"Campus(nome={self.nome}, cidade={self.cidade})"


class Curso:
    def __init__(self, nome: str, duracao: int, periodo: str, campus: Campus):
        self.nome = nome
        self.duracao = duracao
        self.periodo = periodo
        self.campus = campus
        self.turmas = []  # relação: Curso 1:N Turma

        campus.adicionar_curso(self)

    def adicionar_turma(self, turma):
        self.turmas.append(turma)

    def __repr__(self):
        return f"Curso(nome={self.nome}, periodo={self.periodo})"


class Turma:
    def __init__(self, codigo: str, ano: int, min_matriculas: int, curso: Curso):
        self.codigo = codigo
        self.ano = ano
        self.min_matriculas = min_matriculas
        self.curso = curso
        self.matriculas = []  # relação: Turma 1:N Matrícula

        curso.adicionar_turma(self)

    def adicionar_matricula(self, matricula):
        self.matriculas.append(matricula)

    def total_matriculas(self):
        return len(self.matriculas)

    def pode_iniciar(self):
        return self.total_matriculas() >= self.min_matriculas

    def __repr__(self):
        return f"Turma(codigo={self.codigo}, ano={self.ano})"


class Estudante:
    def __init__(self, nome: str, cpf: str, data_nasc: str):
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.matriculas = []  # relação: Estudante 1:N Matrícula

    def adicionar_matricula(self, matricula):
        self.matriculas.append(matricula)

    def __repr__(self):
        return f"Estudante(nome={self.nome}, cpf={self.cpf})"


class Matricula:
    def __init__(self, estudante: Estudante, turma: Turma, ra: str):
        self.estudante = estudante
        self.turma = turma
        self.ra = ra
        self.data_matricula = datetime.now()

        # cria as ligações automaticamente
        estudante.adicionar_matricula(self)
        turma.adicionar_matricula(self)

    def __repr__(self):
        return f"Matricula(ra={self.ra}, estudante={self.estudante.nome}, turma={self.turma.codigo})"


# =========================
# Exemplo de uso
# =========================

if __name__ == "__main__":
    campus = Campus("IFPR Paranavaí", "Paranavaí")

    curso = Curso("Informática", 3, "Noturno", campus)

    turma = Turma("INFO-2026", 2026, min_matriculas=2, curso=curso)

    aluno1 = Estudante("João", "12345678900", "2000-01-01")
    aluno2 = Estudante("Maria", "98765432100", "2001-02-02")

    m1 = Matricula(aluno1, turma, "RA001")
    m2 = Matricula(aluno2, turma, "RA002")

    print(turma.total_matriculas())   # 2
    print(turma.pode_iniciar())       # True