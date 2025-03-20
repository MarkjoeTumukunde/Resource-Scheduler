import random
import time
from scheduler import ResourceScheduler
from models import Customer
import threading

def simulate_customers(scheduler):
    customer_id = 1  # Start customer IDs from 1
    while True:  # Keeps running
        priority = random.choice([1, 2, 3])  # 1: VIP, 2: Corporate, 3: Normal
        service_time = random.randint(2, 5)
        customer = Customer(customer_id, priority, service_time)
        scheduler.assign_task(customer, method="priority")
        print(f"New customer {customer_id} added.")
        customer_id += 1  # Increment customer ID
        time.sleep(random.uniform(1, 3))  # Generate a new customer every 1-3 seconds


if __name__ == "__main__":
    scheduler = ResourceScheduler(num_agents=3)

    # Starting scheduler thread
    scheduler_thread = threading.Thread(target=scheduler.process_tasks, args=("priority",), daemon=True)
    scheduler_thread.start()

    # Simulating customers
    simulate_customers(scheduler)

    # Keeping the main thread alive clearly:
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Simulation manually stopped.")
