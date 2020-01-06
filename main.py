
import sqlite3
import datetime
import os
import time

# login

tela_login = '\n*** Sistema de Produtos ***'


# inicial

tela_inicial = '''\n*** INICIAL ***

1 - Usuário
2 - Produto
3 - Relatório

4 - Sair

***************************

Selecione uma opção: '''

# usuário

tela_usuario = '''\n*** USUÁRIO ***

1 - Consultar
2 - Cadastrar
3 - Excluir

***************************

Selecione uma opção: '''

# produto

tela_produto = '''\n*** PRODUTO ***

1 - Consultar
2 - Cadastrar
3 - Excluir

***************************

Selecione uma opção: '''

# relatório

tela_relatorio = '''\n*** RELATÓRIO ***

1 - Emitir relatório de Produto
2 - Emitir relatório de Estoque
3 - Emitir relatório de Preço

***************************

Selecione uma opção: '''

# sistema

class Sistema():

	# ************ sistema ************

	# login
	def entrarSistema(self, login, senha):
		con = sqlite3.connect('banco.db')
		cur = con.cursor()
		sql_select = 'SELECT * FROM USUARIO WHERE LOGIN = UPPER("{}") AND SENHA = UPPER("{}")'.format(login, senha)
		cur.execute(sql_select)
		resultado = cur.fetchall()
		cur.close()
		con.close()
		return len(resultado) >= 1
	
	# ************ usuário ************

	# consultar
	def consultarUsuario(self):
		usuario = input('\nDigite o login: ')
		print('\n')
		con = sqlite3.connect('banco.db')
		cur = con.cursor()
		sql_select = 'SELECT LOGIN AS USUARIO, DT_CADASTRO FROM USUARIO WHERE LOGIN LIKE UPPER("%{}%")'.format(usuario)
		cur.execute(sql_select)
		resultado = cur.fetchall()

		os.system('cls')
		print('\nRESULTADO: ')
		print('\nUSUÁRIO              DATA CADASTRO')
		print('-' * 20 + ' ' + '-' * 20)
		
		for registro in resultado:
			print(str(registro[0]).ljust(20) + ' ' + str(registro[1]))

	# cadastrar
	def cadastrarUsuario(self):
		x = False
		while x != True:
			login = input('\nDigite o login: ')
			senha = input('Digite a senha: ')
			data = datetime.date.today()

			if len(login) >= 5 and len(senha) >= 5:		
				con = sqlite3.connect('banco.db')
				cur = con.cursor()
				sql_insert = 'INSERT INTO USUARIO (LOGIN, SENHA, DT_CADASTRO) VALUES (?, ?, ?)'
				dataset = (login.upper(), senha.upper(), data)
				cur.execute(sql_insert, dataset)
				con.commit()
				cur.close()
				con.close()
				print('\nParabéns, usuário cadastrado com sucesso!')
				x = True
			else:
				print('\nPor favor, digite um login e/ou senha com no mínimo 5 caracteres.')

	# excluir
	def excluirUsuario(self):
		login = input('\nDigite o nome de usuário: ')
		con = sqlite3.connect('banco.db')
		cur = con.cursor()
		sql_delete = 'DELETE FROM USUARIO WHERE LOGIN = UPPER("{}")'.format(login)
		cur.execute(sql_delete)
		con.commit()
		cur.close()
		con.close()
		print('\nUsuário excluído com sucesso!')

	# ************ produto ************

	# consultar
	def consultarProduto(self):
		produto = input('\nDigite o nome do produto: ')
		print('\n')
		con = sqlite3.connect('banco.db')
		cur = con.cursor()

		sql_select = '''SELECT DESCRICAO AS PRODUTO,
							PRECO AS PREÇO,
							QUANTIDADE AS ESTOQUE
						FROM PRODUTO
						WHERE DESCRICAO LIKE UPPER("%{}%")
					'''.format(produto)

		cur.execute(sql_select)
		resultado = cur.fetchall()

		os.system('cls')
		print('\nRESULTADO: ')
		print('\nPRODUTO              PREÇO      ESTOQUE')
		print('-' * 20 + ' ' + '-' * 10 + ' ' + '-' * 10)
		
		for registro in resultado:
			print(str(registro[0]).ljust(20) + ' ' + str(registro[1]).ljust(10) + ' ' + str(registro[2]))

	# cadastrar
	def cadastrarProduto(self):
		cadastro = input('\nDigite a Descrição, Preço e Quantidade: ')
		lista = cadastro.split(', ')
		descricao = lista[0]
		preco = lista[1]
		quantidade = lista[2]

		con = sqlite3.connect('banco.db')
		cur = con.cursor()
		sql = 'INSERT INTO PRODUTO (DESCRICAO, PRECO, QUANTIDADE) VALUES (?, ?, ?)'
		dataset = (descricao.upper(), preco.upper(), quantidade)
		cur.execute(sql, dataset)
		con.commit()
		cur.close()
		con.close()

		print('\nProduto cadastrado com sucesso!')

	# excluir
	def excluirProduto(self):
		produto = input('\nDigite o produto: ')
		con = sqlite3.connect('banco.db')
		cur = con.cursor()
		sql = 'DELETE FROM PRODUTO WHERE DESCRICAO = UPPER("{}")'.format(produto)
		cur.execute(sql)
		con.commit()
		cur.close()
		con.close()

		print('\nProduto excluído com sucesso!')

	# ************ relatório ************

	# relatório de produto
	def relatorioProduto(self):
		con = sqlite3.connect('banco.db')
		cur = con.cursor()
		sql = 'SELECT DESCRICAO AS PRODUTO, PRECO AS PREÇO, QUANTIDADE AS ESTOQUE FROM PRODUTO'
		cur.execute(sql)
		resultado = cur.fetchall()

		os.system('cls')
		print('\nRESULTADO: ')
		print('\nPRODUTO              PREÇO      ESTOQUE')
		print('-' * 20 + ' ' + '-' * 10 + '-' * 10)
		
		for registro in resultado:
			print(str(registro[0]).ljust(20) + ' ' + str(registro[1]).ljust(10) + ' ' + str(registro[2]))

	# relatório de estoque
	def relatorioEstoque(self):
		con = sqlite3.connect('banco.db')
		cur = con.cursor()
		sql = 'SELECT DESCRICAO AS PRODUTO, QUANTIDADE AS ESTOQUE FROM PRODUTO'
		cur.execute(sql)
		resultado = cur.fetchall()

		os.system('cls')
		print('\nRESULTADO: ')
		print('\nPRODUTO              ESTOQUE')
		print('-' * 20 + ' ' + '-' * 10)
		
		for registro in resultado:
			print(str(registro[0]).ljust(20) + ' ' + str(registro[1]))

	# relatório de preço
	def relatorioPreco(self):
		con = sqlite3.connect('banco.db')
		cur = con.cursor()
		sql = 'SELECT DESCRICAO AS PRODUTO, PRECO AS PREÇO FROM PRODUTO'
		cur.execute(sql)
		resultado = cur.fetchall()

		os.system('cls')
		print('\nRESULTADO: ')
		print('\nPRODUTO              PREÇO')
		print('-' * 20 + ' ' + '-' * 10)

		for registro in resultado:
			print(str(registro[0]).ljust(20) + ' ' + str(registro[1]))

def main():

	sistema = Sistema()

	x = False
	while x != True:
		print(tela_login)
		login = input('\nLogin: ')
		senha = input('Senha: ')
		x = sistema.entrarSistema(login, senha)
		if x == True:
			print('\nSeja bem vindo ' + login + '!')
		else:
			print('\nLogin e/ou senha incorreto(s)')
		time.sleep(1)
		os.system('cls')

	opcao = 0
	while opcao != '4':

		opcao = input(tela_inicial)
		os.system('cls')

		# usuário
		if opcao == '1':
			usuario_opcao = input(tela_usuario)

			# consultar
			if usuario_opcao == '1':
				sistema.consultarUsuario()
			
			# cadastrar
			if usuario_opcao == '2':
				sistema.cadastrarUsuario()
			
			# excluir
			if usuario_opcao == '3':
				sistema.excluirUsuario()

			input('\nPressione "Enter" para voltar ...')
			os.system('cls')
		
		# produto
		elif opcao == '2':
			produto_opcao = input(tela_produto)

			# consultar
			if produto_opcao == '1':
				sistema.consultarProduto()
			
			# cadastrar
			elif produto_opcao == '2':
				sistema.cadastrarProduto()

			# excluir
			elif produto_opcao == '3':
				sistema.excluirProduto()

			input('\nPressione "Enter" para voltar ...')
			os.system('cls')

		# relatório
		elif opcao == '3':
			produto_opcao = input(tela_relatorio)

			# produto
			if produto_opcao == '1':
				sistema.relatorioProduto()
			
			# estoque
			elif produto_opcao == '2':
				sistema.relatorioEstoque()

			# preço
			elif produto_opcao == '3':
				sistema.relatorioPreco()

			input('\nPressione "Enter" para voltar ...')
			os.system('cls')

if __name__ == "__main__":
	main()