
class Endereco:
    def __init__(self, rua: str, numero: int, bairro: str, cidade: str, cep: str):
        self.rua = rua.capitalize()
        self.numero = numero
        self.bairro = bairro.capitalize()
        self.cidade = cidade.capitalize()
        self.cep = cep

    def formatar_endereco(self) -> str:
        return f'{self.rua}, Nº {self.numero}, {self.bairro} - {self.cidade} (CEP: {self.cep[:5]}-{self.cep[5:]})'

    def atualizar_dados(self, rua: str, numero: int, bairro: str, cidade: str, cep: str) -> str:
        self.rua = rua.capitalize()
        self.numero = numero
        self.bairro = bairro.capitalize()
        self.cidade = cidade.capitalize()
        self.cep = cep
        return Endereco



class Aluno:
    def __init__(self, matricula: str, nome: str, endereco: Endereco):
        self.matricula = matricula
        self.nome = nome
        self.endereco = endereco

    def estudando(self):
        return f'O aluno {self.nome} (Matrícula: {self.matricula}) está estudando.'


class SalaDeAula:
    def __init__(self, numero: int, capacidade: int):
        self.numero = numero
        self.capacidade = capacidade

    def exibir_detalhes(self) -> str:
        return f'Sala {self.numero} (Capacidade: {self.capacidade} alunos)'


class Professor:
    def __init__(self, nome: str, cpf: str, disciplina: str):
        self.nome = nome
        self.cpf = cpf
        self.disciplina = disciplina

    def lecionar(self):
        return f'O prof. {self.nome} está lecionando a disciplina de {self.disciplina}.'


class Escola:
    def __init__(self, nome: str, cnpj: str):
        self.nome = nome
        self.cnpj = cnpj
        self.salas = []
        self.professores = []

    
    def criar_sala(self, numero: int, capacidade: int):
        nova_sala = SalaDeAula(numero, capacidade)
        self.salas.append(nova_sala)

    
    def adicionar_professor(self, professor: Professor):
        if professor not in self.professores:
            self.professores.append(professor)

    def listar_estrutura(self):
        print(f"\n--- Estrutura da Escola: {self.nome} ---")
        print("Salas de Aula:")
        for sala in self.salas:
            print(f"  - {sala.exibir_detalhes()}")
        print("Professores Cadastrados:")
        for professor in self.professores:
            print(f"  - Prof. {professor.nome} ({professor.disciplina})")



oi = Endereco('Rua ', 3, 'cavalcante', 'PARNAIBA', '64212211')
print(oi.formatar_endereco())