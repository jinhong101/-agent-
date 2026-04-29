import threading
import time

class BaseAgent(threading.Thread):
    def __init__(self, name):
        super().__init__(daemon=True)
        self.name = name
        self._running = True

    def run(self):
        while self._running:
            self.step()
            time.sleep(1)

    def step(self):
        raise NotImplementedError

    def stop(self):
        self._running = False