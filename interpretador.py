import time
import re

# Simula sensores e atuadores, com métodos para verificar a existência de peças, detectar cores e ativar atuadores.
class Controlador:
	def __init__(self):
		#insere lista de peças a serem analisadas
		self.pecas = ["vermelho", "verde", "azul", "amarelo", "verde"]
		self.indice = 0

	def existe_pecas(self):
		return self.indice < len(self.pecas)

	def sensor_cor(self):
		if self.existe_pecas():
			return self.pecas[self.indice]
		return None

	def atuar(self, cor):
		if cor == "vermelho":
			print("Acionando Atuador Pneumático 1, movendo peças descartadas para esteira de descarte.")
			print("-----------------------------------------------------------------------------------")
		elif cor == "amarelo":
			print("Acionando Atuador Pneumático 2, movendo peças com defeito para esteira de revisão.")
			print("-----------------------------------------------------------------------------------")
		elif cor == "azul":
			print("Acionando Atuador Pneumático 3, movendo peças em excesso da esteira de produção.")
			print("-----------------------------------------------------------------------------------")
		elif cor == "verde":
			print("Acionando Atuador Pneumático 4, movendo peças corretas para produção.")
			print("-----------------------------------------------------------------------------------")
		else:
			print("Nenhum atuador ativado, sem movimentação de peças.")
			print("-----------------------------------------------------------------------------------")

	def pausar(self, ms):
		time.sleep(ms / 1000)

# Análise Lexica: Lê o código e divide em tokens usando expressões regulares. Os tokens são palavras e símbolos.
def analisar_lexica(codigo):
	tokens = []
	for linha in codigo.splitlines():
		linha = linha.strip()
		if linha:
			tokens.extend(re.findall(r'\w+|[()=<>]+|;', linha))
	return tokens

# Análise Sintática : Constrói uma árvore de sintaxe abstrata (AST) a partir dos tokens. Capturamos estruturas de controle, como o laço WHILE(ENQUANTO).
def analisar_sintatica(tokens):
	ast = []
	i = 0
	while i < len(tokens):
		token = tokens[i]
		if token == "ENQUANTO":
			condicao = tokens[i + 1:i + 4]  # Captura a condição
			bloco = []
			i += 5  # Pula o bloco inicial (inclui o 'DO')
			while i < len(tokens) and tokens[i] != "FINALIZE":
				bloco.append(tokens[i])
				i += 1
			ast.append(("ENQUANTO", condicao, bloco))
		i += 1
	return ast

# Execução : Interpreta a AST e executa as ações correspondentes. Neste caso, ele processa o laço WHILE(ENQUANTO) e as instruções contidas.
def executar(ast, controlador):
	for comando in ast:
		if comando[0] == "ENQUANTO":
			condicao, bloco = comando[1], comando[2]
			while controlador.existe_pecas():
				cor_atual = controlador.sensor_cor()
				print(f"Cor da peça: {cor_atual}")

				if cor_atual == "vermelho":
					controlador.atuar("vermelho")
				elif cor_atual == "verde":
					controlador.atuar("verde")
				elif cor_atual == "azul":
					controlador.atuar("azul")
				elif cor_atual == "amarelo":
					controlador.atuar("amarelo")
				else:
					controlador.atuar("nenhum")

				controlador.indice += 1
				controlador.pausar(100)


# Função principal para executar o interpretador : Orquestra o fluxo, chamando a análise lexical, sintática e a execução.
def start(codigo):
	tokens = analisar_lexica(codigo)
	ast = analisar_sintatica(tokens)
	controlador = Controlador()
	executar(ast, controlador)


