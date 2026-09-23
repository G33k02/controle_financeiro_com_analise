import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dados.csv')
df_t = pd.read_csv('Transactions.csv')

saldo = df["Saldo"][0]
credito = df["Credito"][0]

print(saldo, credito)



class Conta:

    def __init__(self, saldo, credito, df_transactions):

        self._saldo = saldo
        self._credito = credito
        self.df_t = df_transactions

    def verif_insert(self):
        while True:
            try:
                choise = int(input("1- receita ou 2- despesa: "))

                if choise != 1 and choise != 2:
                    print('Digite uma opção valida.')
                    continue
                else:
                    if choise == 1:

                        desc = str(input("Digite a descrição da transação: "))

                        while True:
                            try:
                                value = float(input("Digite o valor da transação: "))
                                break
                            except ValueError:
                                print("Digite um Formato correto.")
                                continue

                        data = str(input("Digite a data: "))

                        categoria = str(input('Digite a categoria:'))

                        self._receita(desc, value, data, categoria, "Receita")
                        
                    else:
                               
                        desc = str(input("Digite a descrição da transação: "))

                        while True:
                            try:
                                value = float(input("Digite o valor da transação: "))
                                break
                            except ValueError:
                                print("Digite um formato correto.")
                                continue
                    
                        data = str(input("Digite a data: "))
                    
                        categoria = str(input('Digite a categoria da despesa: '))

                        while True:
                            try:
                                tipo = int(input("Escolha 1-Pix, 2-Débito ou 3-Crédito: "))

                                if tipo == 1:
                                    tipo = 'Pix'
                                elif tipo == 2:
                                    tipo = 'Debito'
                                elif tipo == 3:
                                    tipo = 'Credito'
                                else:
                                    print("Digite um dos numeros citados.")
                                    continue
                                break
                            except ValueError:
                                print("Digite um formato correto.")
                                continue

                    
                        self._despesa(desc, value, data, categoria, tipo)

                break
                        
            except ValueError:
                print("Digite um formato correto.")


    def _receita(self, desc, value, data, categoria, tipo):
        self._saldo += value
        self.df_t.loc[len(self.df_t)] = [desc, value, data, categoria, tipo]

    
    def _despesa(self, desc, value, data, categoria, tipo):

            if tipo == 'Pix' or tipo == 'Debito':
                self._saldo -= value
            elif tipo == 'Credito':
                self._credito -= value
            print(f"Seu saldo atual é de R${self._saldo:.2f}, e seu credito é de R${self._credito:.2f}")

            self.df_t.loc[len(self.df_t)] = [desc, value,  data, categoria, tipo] 

    def print_all_tran(self):
        if len(self.df_t) == 0 :
            print("Nenhuma transação realizada até o momento.")
            return
        
        print(self.df_t)


    def resumo(self):

        df_temp = self.df_t[self.df_t['type'] == 'Receita']  
        receita = sum(df_temp['value'])
        print(f"Receitas: R${receita:.2f}")

        df_temp = self.df_t[self.df_t['type'] == 'Pix' ]
        pix = sum(df_temp['value'])
        df_temp = self.df_t[self.df_t['type'] == 'Credito' ]
        credito = sum(df_temp['value'])
        df_temp = self.df_t[self.df_t['type'] == 'Debito' ]
        debito = sum(df_temp['value'])

        total_despesa = pix + credito + debito

        print(f"Despesas: R${total_despesa:.2f} - Sendo Pix: R${pix:.2f} | Débito: R${debito:.2f} | Crédito: R${credito:.2f}")
        print('\n')
        print(f"Saldo: R${self._saldo:.2f}")
        print(f"Credito disponivel: R${self._credito:.2f}")

    def alterar_credito(self):
        value = int(input(f"Valor de credito atual é R$ {self._credito:.2f}, deseja alterar ? [1-sim 2-não]: "))

        if value ==1:
            self._credito = float(input("Digite o novo valor de crédito atual: "))
            print(f"Alterado com sucesso, novo valor : R${self._credito:.2f}")
        elif value == 2:
            print("Até a proxima então.")
            return

    def salvar(self):

        df.loc[0, "Saldo"] = self._saldo
        df.loc[0, "Credito"] = self._credito

        df.to_csv('Dados.csv', index=False)
        self.df_t.to_csv('Transactions.csv', index=False)
        return
    
gg = Conta(saldo, credito, df_t)




print("Bem Vindo ao seu CONTROLE FINANCEIRO")

while True:
    try:
        print('''
========== CONTROLE FINANCEIRO ==========

1 - Nova transação
2 - Mostrar transações
3 - Resumo
4 - Salvar e Sair
5 - Editar crédito
6 - Estatísticas
''')
        escolhas = [1, 2, 3, 4, 5, 6]
        escolha = int(input("Digite sua escolha: "))

        if escolha not in escolhas:
            print('Sua escolha não esta entre as possíveis.')
            continue

        if escolha == 1:
            gg.verif_insert()
        elif escolha == 2:
            gg.print_all_tran()
        elif escolha == 3:
            gg.resumo()
        elif escolha == 4:

            print("Salvando...")

            gg.salvar()

            print("Salvo com sucesso!!!\n")

            print("Bye Bye até a proxima transação. :v")
            break
        elif escolha == 5:
            gg.alterar_credito()

        elif escolha == 6:
            ...

    except ValueError:
        print("Digite um valor válido")