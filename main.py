import os, time, datetime

def limpa():
	""" Função responsavel por limpar a tela. """
	os.system("clear")


def line():
	""" Essa função escreve uma linha divisória. """
	print("=" * 40)


def cab():
	""" Essa função exibe o cabeçalho. """
	line()
	print(f"{'Agenda em Python':^40}")
	line()


def menu():
	""" Função que exibe o menu. """
	print("""\
(1) - Agendar um novo evento
(2) - ver eventos agendados
(3) - lumpar todos eventos
(4) - sair do programa""")
	line()


def agendar_evento(arquivo, evento):
	""" Função que ira inserir os eventos em um arquivo. """
	if os.path.exists(arquivo):
		with open(arquivo, "a") as file:
			file.write(evento + "\n")
		print("Evento registrado com sucesso!")
	else:
		# Se o evento não existir abrimos ele com o w+
		# Feito isso escrevemos os evento no arquivo.
		with open(arquivo, "w+") as file:
			file.write(evento + "\n")
		print("Evento registrado com sucesso!")


def exibir_eventos(arquivo):
	""" Essa função exibe os eventos marcados pelo usuaeio. """
	if os.path.exists(arquivo):
		with open(arquivo, "r") as file:
			print("Eventos agendados: \n")
			for event in file:
				print(f"{datetime.date.today()}: {event}")
	else:
		print("No momento não temos nenhuma informação.")


def excluir_agenda(arquivo):
	""" Função que apaga a agenda. """
	if os.path.exists(arquivo):
		opc = str(input("Tem certeza de quer fazer issso? (S/n): ")).upper()
		while opc != 'S' and opc != 'N':
			print("Opção invalida. Digite S ou N.")
			opc = str(input("Sim ou Não? (S/n): ")).upper()
		if opc == "S":
			os.remove(arquivo)
			print(f"{datetime.date.today()}: Arquivo {arquivo} excluido com  succeso!")
		else:
			print("Ok... não resetarei a agenda.")
	else:
		print("Não recebemos nenhuma informação até agora.")


# Programa principal
while True:
	try:
		limpa()
		cab()
		menu()
		opc = int(input("Escolha uma opção: "))
		line()
		if opc == 1:
			ev = input("Me diga o evento que deseja registrar: ")
			agendar_evento("eventos.txt", ev)
		elif opc == 2:
			exibir_eventos("eventos.txt")
		elif opc == 3:
			excluir_agenda("eventos.txt")
		elif opc == 4:
			print("Espero que que tenha gostado! Xau!")
			break
		else:
			print("Opção invalida. Tente novamente.")
		line()
		time.sleep(5)
		print("Reiniciando sistema...")
	except Exception as erro:
		print(erro)
		time.sleep(5)


line()

