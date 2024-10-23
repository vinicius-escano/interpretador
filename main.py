import interpretador as it

# Código de exemplo
codigo_exemplo = """
ENQUANTO existe_pecas() REALIZE
    SENSOR cor -> cor_atual
    	SE cor_atual == "vermelho" ENTAO
	       		ATUADOR ligar "pneu1"
    	SENAO  cor_atual == "verde" ENTAO
       			ATUADOR ligar "pneu2"
    	SENAO
       			ATUADOR desligar "pneu1"
       			ATUADOR desligar "pneu2"
    	PAUSA(100)
FINALIZE
"""
#Laço WHILE(ENQUANTO) com uma condição diferente
codigo_exemplo_1 = """
ENQUANTO existe_pecas() REALIZE
	SENSOR cor -> cor_atual
	SE cor_atual == "azul" ENTAO
		ATUADOR ligar "pneu3"
	SENAO
		ATUADOR desligar "pneu3"
	PAUSA(200)
FINALIZE
"""

#Múltiplos IF(SE) e uma condição de saída
codigo_exemplo_2 = """
ENQUANTO existe_pecas() REALIZE
	SENSOR cor -> cor_atual
	SE cor_atual == "vermelho" ENTAO
		ATUADOR ligar "pneu1"
	SSENAO cor_atual == "verde" ENTAO
		ATUADOR ligar "pneu2"
	SENAO cor_atual == "amarelo" ENTAO
		ATUADOR ligar "pneu3"
	SENAO
		ATUADOR desligar "pneu1"
		ATUADOR desligar "pneu2"
		ATUADOR desligar "pneu3"
	PAUSA(150)
FINALIZE
"""

#Um laço que faz ações diferentes com base em diferentes condições
codigo_exemplo_3 = """
ENQUANTO existe_pecas() DREALIZE
	SENSOR cor -> cor_atual
	SE cor_atual == "verde" ENTAO
		ATUADOR ligar "pneu2"
		PAUSA(50)
		ATUADOR desligar "pneu1"
	SENAO cor_atual == "vermelho" ENTAO
		ATUADOR ligar "pneu1"
		PAUSA(50)
		ATUADOR desligar "pneu2"
	SENAO
		ATUADOR desligar "pneu1"
		ATUADOR desligar "pneu2"
	PAUSA(100)
FINALIZE
"""
#Verificação de múltiplas peças
codigo_exemplo_4 = """
ENQUANTO existe_pecas() REALIZE
	SENSOR cor -> cor_atual
	SE cor_atual == "azul" ENTAO
		ATUADOR ligar "pneu3"
	SENAO cor_atual == "amarelo" ENTAO
		ATUADOR ligar "pneu4"
	SENAO
		ATUADOR desligar "pneu3"
		ATUADOR desligar "pneu4"
	PAUSA(300)
FINALIZE
"""

#Laço com uma condição de parada
codigo_exemplo_5 = """
ENQUANTO existe_pecas() REALIZE
	SENSOR cor -> cor_atual
	SE cor_atual == "vermelho" ENTAO
		ATUADOR ligar "pneu1"
		PAUSA(100)
		ATUADOR desligar "pneu1"
	SENAO cor_atual == "verde" ENTAO
		ATUADOR ligar "pneu2"
		PAUSA(100)
		ATUADOR desligar "pneu2"
	PAUSA(50)
FINALIZE
"""

# Executar o interpretador
it.start(codigo_exemplo)
print("\n  ######### \n")
it.start(codigo_exemplo_1)
print("\n  ######### \n")
it.start(codigo_exemplo_2)
print("\n  ######### \n")
it.start(codigo_exemplo_3)
print("\n  ######### \n")
it.start(codigo_exemplo_4)
print("\n  ######### \n")
it.start(codigo_exemplo_5)