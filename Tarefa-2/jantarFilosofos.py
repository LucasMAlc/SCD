import threading
import time

class Filosofo:
    def __init__(self, nome, hashi_esquerda, hashi_direita, contador_refeicoes, monitor):
        self.nome = nome
        self.hashi_esquerda = hashi_esquerda
        self.hashi_direita = hashi_direita
        self.contador_refeicoes = contador_refeicoes
        self.monitor = monitor

    def pegar_hashi_esquerda(self):
        with self.monitor: # adquire o monitor para sincronização
            while not self.hashi_esquerda: # aguarda até que o hashi esteja disponível
                self.monitor.wait()
            self.hashi_esquerda = False # marca o hashi como indisponível
            print(f'{self.nome} pegou o hashi da esquerda.')

    def pegar_hashi_direita(self):
        with self.monitor: # adquire o monitor para sincronização
            while not self.hashi_direita: # aguarda até que o hashi esteja disponível
                self.monitor.wait()
            self.hashi_direita = False # marca o hashi como indisponível
            print(f'{self.nome} pegou o hashi da direita.')

    def soltar_hashis(self):
        with self.monitor: # adquire o monitor para sincronização
            self.hashi_esquerda = True # marca o hashi como disponível
            self.hashi_direita = True # marca o hashi como disponível
            self.monitor.notify_all() # notifica outras threads que os hashis foram liberados

    def comer(self):
        with self.monitor: # adquire o monitor para sincronização
            print(f'{self.nome} esta comendo agora.')
            time.sleep(3)
            self.contador_refeicoes += 1 # contabiliza o número de refeições realizadas
            print(f'{self.nome} terminou de comer.')

    def pensar(self):
        print(f'{self.nome} esta pensando agora.')
        time.sleep(3)

    def jantar(self):
        while self.contador_refeicoes < 3: # realiza até três refeições
            self.pensar() # o filósofo pensa antes de tentar pegar os hashis
            with self.monitor: # adquire o monitor para sincronização
                self.pegar_hashi_esquerda()
                self.pegar_hashi_direita()
                self.comer() # come enquanto segura os hashis
                self.soltar_hashis() # solta os hashis quando termina de comer

if __name__ == '__main__':
    # cria uma lista com cinco hashis disponíveis
    hashis = [True for _ in range(5)] 

    # cria uma lista com o número de refeições realizadas por cada filósofo
    contador_refeicoes = [0 for _ in range(5)] 

    # cria um objeto Condition que será usado como monitor
    monitor = threading.Condition() 

    # cria uma lista com os nomes dos filósofos
    filosofos_nome = ["Rafael", "Michelangelo", "Leonardo", "Donatello", "Splinter"] 

    filosofos = [Filosofo(filosofos_nome[i], hashis[i], hashis[(i+1)%5], contador_refeicoes[i], monitor) for i in range(5)]
    threads = [threading.Thread(target=filosofo.jantar) for filosofo in filosofos]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
