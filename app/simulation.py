import random
import time
from scheduler import ResourceScheduler
from models import Customer
import threading

def simulate_customers(scheduler):
    for i in range(10):
        priority = random.choice([1, 2, 3])  # 1: VIP, 2: Corporate, 3: Normal
        service_time = random.randint(2, 5)
        customer = Customer(i, priority, service_time)
        scheduler.assign_task(customer, method="priority")
        time.sleep(random.uniform(0.5, 2))

if __name__ == "__main__":
    scheduler = ResourceScheduler(num_agents=3)

    # Clearly start scheduler thread
    scheduler_thread = threading.Thread(target=scheduler.process_tasks, args=("priority",), daemon=True)
    scheduler_thread.start()

    # Clearly simulate customers
    simulate_customers(scheduler)

    # Explicitly keep the main thread alive clearly:
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Simulation manually stopped.")
