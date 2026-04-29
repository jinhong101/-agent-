from .base_agent import BaseAgent
import queue
import time

class WorkerAgent(BaseAgent):
    def __init__(self, name, task_queue: queue.Queue):
        super().__init__(name)
        self.task_queue = task_queue

    def step(self):
        try:
            task = self.task_queue.get_nowait()
            print(f"[{self.name}] 执行任务: {task}")
            time.sleep(0.5)  # 模拟任务耗时
        except queue.Empty:
            print(f"[{self.name}] 暂无任务")