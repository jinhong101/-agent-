from .base_agent import BaseAgent
import queue
import random
from tasks.task_definitions import SAMPLE_TASKS

class MonitorAgent(BaseAgent):
    def __init__(self, name, task_queue: queue.Queue):
        super().__init__(name)
        self.task_queue = task_queue

    def step(self):
        task = random.choice(SAMPLE_TASKS)
        print(f"[{self.name}] 生成任务: {task}")
        self.task_queue.put(task)