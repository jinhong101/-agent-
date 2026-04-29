import queue
from agents.worker_agent import WorkerAgent
from agents.monitor_agent import MonitorAgent
import time

def main():
    task_queue = queue.Queue()

    # 创建 Agent
    workers = [WorkerAgent(f"Worker-{i}", task_queue) for i in range(3)]
    monitor = MonitorAgent("Monitor", task_queue)

    # 启动 Agent
    for w in workers:
        w.start()
    monitor.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("停止所有 Agent...")
        monitor.stop()
        for w in workers:
            w.stop()

if __name__ == "__main__":
    main()