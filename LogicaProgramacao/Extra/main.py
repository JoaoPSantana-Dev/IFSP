class Aluno:
    """
    Classe responsavel por representar um aluno.
    """

    def __init__(
        self,
        nome,
        prontuario,
        curso,
        disciplina,
        professor,
        nota1,
        nota2
    ):
        self.nome = nome
        self.prontuario = prontuario
        self.curso = curso
        self.disciplina = disciplina
        self.professor = professor
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        """
        Calcula e retorna a media das duas notas.
        """
        return (self.nota1 + self.nota2) / 2

    def verificar_situacao(self):
        """
        Verifica se o aluno esta aprovado ou reprovado.
        Para este exercecio:
        media >= 6.0 -> Aprovado
        media < 6.0 -> Reprovado
        """

        media = self.calcular_media()

        if media >= 6:
            return "APROVADO"
        else:
            return "REPROVADO"

    def alterar_notas(self, nota1, nota2):
        """
        Altera as notas do aluno.
        """

        self.nota1 = nota1
        self.nota2 = nota2

    def exibir_dados(self):
        """
        Exibe os dados completos do aluno.
        """

        print("\n" + "=" * 60)
        print("DADOS DO ALUNO")
        print("=" * 60)

        print(f"Nome.............: {self.nome}")
        print(f"Prontuario.......: {self.prontuario}")
        print(f"Curso............: {self.curso}")
        print(f"Disciplina.......: {self.disciplina}")
        print(f"Professor........: {self.professor}")
        print(f"Nota 1...........: {self.nota1:.2f}")
        print(f"Nota 2...........: {self.nota2:.2f}")
        print(f"Media............: {self.calcular_media():.2f}")
        print(f"Situacao.........: {self.verificar_situacao()}")

        print("=" * 60)


# --------------------------------------------------------
# LISTA QUE ARMAZENAR� OS OBJETOS DA CLASSE ALUNO
# --------------------------------------------------------

alunos = []


# --------------------------------------------------------
# FUNCAO PARA VALIDAR NOTA
# --------------------------------------------------------

def ler_nota(mensagem):
    """
    Solicita uma nota entre 0 e 10.
    """

    while True:

        try:

            nota = float(input(mensagem))

            if nota < 0 or nota > 10:
                print("ERRO: a nota deve estar entre 0 e 10.")
            else:
                return nota

        except ValueError:
            print("ERRO: digite um numero valido.")


# --------------------------------------------------------
# FUN��O PARA LOCALIZAR ALUNO
# --------------------------------------------------------

def buscar_aluno_por_prontuario(prontuario):
    """
    Percorre a lista procurando um aluno
    pelo prontuario informado.
    """

    for aluno in alunos:

        if aluno.prontuario.lower() == prontuario.lower():
            return aluno

    return None


# --------------------------------------------------------
# CADASTRAR ALUNO
# --------------------------------------------------------

def cadastrar_aluno():

    print("\n" + "=" * 60)
    print("CADASTRO DE ALUNO")
    print("=" * 60)

    nome = input("Nome: ").strip()

    prontuario = input("Prontuario: ").strip()

    # Verifica se o prontu�rio j� existe
    aluno_existente = buscar_aluno_por_prontuario(prontuario)

    if aluno_existente is not None:
        print("\nERRO: ja existe um aluno com esse prontuario.")
        return

    curso = input("Curso: ").strip()

    disciplina = input("Disciplina: ").strip()

    professor = input("Professor: ").strip()

    nota1 = ler_nota("Nota 1: ")

    nota2 = ler_nota("Nota 2: ")

    # Criacao do objeto
    novo_aluno = Aluno(
        nome,
        prontuario,
        curso,
        disciplina,
        professor,
        nota1,
        nota2
    )

    # Adiciona o objeto a lista
    alunos.append(novo_aluno)

    print("\nAluno cadastrado com sucesso.")


# --------------------------------------------------------
# LISTAR TODOS OS ALUNOS
# --------------------------------------------------------

def listar_alunos():

    print("\n" + "=" * 90)
    print("LISTA DE ALUNOS")
    print("=" * 90)

    if len(alunos) == 0:

        print("Nenhum aluno cadastrado.")

        return

    print(
        f"{'PRONTUARIO':<15}"
        f"{'NOME':<25}"
        f"{'CURSO':<20}"
        f"{'MEDIA':<10}"
        f"{'SITUACAO':<15}"
    )

    print("-" * 90)

    for aluno in alunos:

        print(
            f"{aluno.prontuario:<15}"
            f"{aluno.nome:<25}"
            f"{aluno.curso:<20}"
            f"{aluno.calcular_media():<10.2f}"
            f"{aluno.verificar_situacao():<15}"
        )

    print("=" * 90)


# --------------------------------------------------------
# CONSULTAR ALUNO
# --------------------------------------------------------

def consultar_aluno():

    print("\n" + "=" * 60)
    print("CONSULTA DE ALUNO")
    print("=" * 60)

    prontuario = input(
        "Digite o prontuario do aluno: "
    ).strip()

    aluno = buscar_aluno_por_prontuario(prontuario)

    if aluno is None:

        print("\nAluno nao encontrado.")

        return

    aluno.exibir_dados()


# --------------------------------------------------------
# ALTERAR NOTAS
# --------------------------------------------------------

def alterar_notas():

    print("\n" + "=" * 60)
    print("ALTERACAO DE NOTAS")
    print("=" * 60)

    prontuario = input(
        "Digite o prontuario do aluno: "
    ).strip()

    aluno = buscar_aluno_por_prontuario(prontuario)

    if aluno is None:

        print("\nAluno nao encontrado.")

        return

    print("\nAluno encontrado:")

    print(f"Nome: {aluno.nome}")

    print(f"Nota atual 1: {aluno.nota1:.2f}")

    print(f"Nota atual 2: {aluno.nota2:.2f}")

    print()

    nova_nota1 = ler_nota(
        "Digite a nova Nota 1: "
    )

    nova_nota2 = ler_nota(
        "Digite a nova Nota 2: "
    )

    aluno.alterar_notas(
        nova_nota1,
        nova_nota2
    )

    print("\nNotas alteradas com sucesso.")

    print(
        f"Nova media: "
        f"{aluno.calcular_media():.2f}"
    )

    print(
        f"Situacao: "
        f"{aluno.verificar_situacao()}"
    )


# --------------------------------------------------------
# EXCLUIR ALUNO
# --------------------------------------------------------

def excluir_aluno():

    print("\n" + "=" * 60)
    print("EXCLUSAO DE ALUNO")
    print("=" * 60)

    prontuario = input(
        "Digite o prontuario do aluno: "
    ).strip()

    aluno = buscar_aluno_por_prontuario(prontuario)

    if aluno is None:

        print("\nAluno nao encontrado.")

        return

    aluno.exibir_dados()

    confirmacao = input(
        "\nDeseja realmente excluir este aluno? (S/N): "
    ).strip().upper()

    if confirmacao == "S":

        alunos.remove(aluno)

        print("\nAluno excluido com sucesso.")

    else:

        print("\nExclusao cancelada.")


# --------------------------------------------------------
# IMPRIMIR RELATORIO COMPLETO
# --------------------------------------------------------

def imprimir_relatorio():

    print("\n")
    print("=" * 70)
    print("RELATORIO GERAL DE ALUNOS")
    print("=" * 70)

    if len(alunos) == 0:

        print("Nenhum aluno cadastrado.")

        return

    for numero, aluno in enumerate(alunos, start=1):

        print(f"\nALUNO N° {numero}")
        print("-" * 70)

        print(f"Nome.............: {aluno.nome}")
        print(f"ProntuArio.......: {aluno.prontuario}")
        print(f"Curso............: {aluno.curso}")
        print(f"Disciplina.......: {aluno.disciplina}")
        print(f"Professor........: {aluno.professor}")
        print(f"Nota 1...........: {aluno.nota1:.2f}")
        print(f"Nota 2...........: {aluno.nota2:.2f}")

        print(
            f"Media............: "
            f"{aluno.calcular_media():.2f}"
        )

        print(
            f"Situacao.........: "
            f"{aluno.verificar_situacao()}"
        )

    print("\n" + "=" * 70)

    print(
        f"Total de alunos cadastrados: "
        f"{len(alunos)}"
    )

    print("=" * 70)


# --------------------------------------------------------
# EXIBIR MENU
# --------------------------------------------------------

def exibir_menu():

    print("\n")
    print("=" * 60)
    print("SISTEMA DE CADASTRO DE ALUNOS")
    print("=" * 60)

    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Consultar aluno")
    print("4 - Alterar notas")
    print("5 - Excluir aluno")
    print("6 - Imprimir relat�rio completo")
    print("0 - Encerrar")

    print("=" * 60)


# --------------------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------------------

def main():

    while True:

        exibir_menu()

        opcao = input(
            "Escolha uma opcao: "
        ).strip()

        if opcao == "1":

            cadastrar_aluno()

        elif opcao == "2":

            listar_alunos()

        elif opcao == "3":

            consultar_aluno()

        elif opcao == "4":

            alterar_notas()

        elif opcao == "5":

            excluir_aluno()

        elif opcao == "6":

            imprimir_relatorio()

        elif opcao == "0":

            print("\nPrograma encerrado.")

            break

        else:

            print(
                "\nOpcao invalida. "
                "Escolha novamente."
            )


# --------------------------------------------------------
# IN�CIO DO PROGRAMA
# --------------------------------------------------------

if __name__ == "__main__":
    main()
