import Pyro4

@Pyro4.expose
class Calculadora(object):
    def add(self, num1, num2, name):
        print(f"{name} escolheu adição. Resultado: {num1} + {num2} = {num1+num2}")
        return num1+num2
    
    def sub(self, num1, num2, name):
        print(f"{name} escolheu subtração. Resultado: {num1} - {num2} = {num1-num2}")
        return num1-num2
    
    def mult(self, num1, num2, name):
        print(f"{name} escolheu multiplicação. Resultado: {num1} * {num2} = {num1*num2}")
        return num1*num2
    
    def div(self, num1, num2, name):
        print(f"{name} escolheu divisão. Resultado: {num1} / {num2} = {num1/num2}")
        return num1/num2

def start_server():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(Calculadora)
    ns.register('tarefa3.server', str(uri))
    print(f'Calculadora pronta.')
    daemon.requestLoop()


if __name__ == '__main__':
    try:
        start_server()
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit