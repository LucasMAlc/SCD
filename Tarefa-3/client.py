import Pyro4

server = Pyro4.Proxy(f"PYRONAME:tarefa3.server")

def start():
    continuar = 'S'
    while continuar == 'S':
        name = input("Qual seu nome? ")
        num1 = float (input("Digite o primeiro valor: "))
        num2 = float (input("Digite o segundo valor: "))
        

        opr = input("Qual é a operação? \n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n")

        if opr == '1':
            print("Resultado:")
            print(server.add(num1, num2, name))
        elif opr == '2':
            print("Resultado:")
            print(server.sub(num1, num2, name))
        elif opr == '3':
            print("Resultado:")
            print(server.mult(num1, num2, name))
        elif opr == '4':
            print("Resultado:")
            print(server.div(num1, num2, name))
        else: 
            print("Opereção inválida")
        
        continuar = input("Deseja continuar? [S/N]")

if __name__ == '__main__':
    try:
        start()
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit
