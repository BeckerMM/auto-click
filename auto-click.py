import time
import threading
from tracemalloc import stop
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

botao = Button.left
delay = 0.001
start = KeyCode(char='t')
stop = KeyCode(char='y')
finalizarPrograma= KeyCode(char='f')

class ClickMouse(threading.Thread):
    def __init__(self, delay, botao):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = botao
        self.running = False
        self.program_running = True
        self.finalizar = True
        
    def finalizarTudo(self):
        self.finalizar = False 
        
    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.finalizar:
            while self.program_running:
                while self.running:
                    mouse.click(self.button)
                    time.sleep(self.delay)
                    time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, botao)
click_thread.start()


def on_press(key):
    if key == start:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == stop:
        click_thread.exit()
    elif key == finalizarPrograma:
         listener.stop()
        


with Listener(on_press=on_press) as listener:
    listener.join()
