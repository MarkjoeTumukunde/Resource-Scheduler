import threading
import time
import random
from queue import PriorityQueue, Queue
from models import Customer, Agent

class ResourceScheduler:
    def __init__(self, num_agents=3):
        self.agents = [Agent(i) for i in range(num_agents)]
        self.queue_priority = PriorityQueue()
        self.queue_round_robin = Queue()
        self.queue_shortest_job = []  # List for Shortest Job Next Scheduling
        self.lock = threading.Lock()
        self.current_rr_index = 0  # To track Round Robin assignments
        self.wait_times = []  # List to track customer waiting times
        self.agent_utilization = {agent.agent_id: 0 for agent in self.agents}  # Tracks how much time agents spend working
        self.total_tasks = 0

    def assign_task(self, customer, method="priority"):
        customer.arrival_time = time.time()  # Track when customer joins queue
        if method == "priority":
            self.queue_priority.put(customer)
        elif method == "round_robin":
            self.queue_round_robin.put(customer)
        elif method == "shortest_job_next":
            self.queue_shortest_job.append(customer)
            self.queue_shortest_job.sort(key=lambda x: x.service_time)  # Sort by shortest job first

    def process_tasks(self, method="priority"):
        threading.Thread(target=self.monitor_agents, daemon=True).start()  # Start monitoring
        
        while True:
            with self.lock:
                available_agents = [agent for agent in self.agents if agent.available]
                if not available_agents:
                    continue
                
                if method == "priority" and not self.queue_priority.empty():
                    customer = self.queue_priority.get()
                elif method == "round_robin" and not self.queue_round_robin.empty():
                    customer = self.queue_round_robin.get()
                elif method == "shortest_job_next" and self.queue_shortest_job:
                    customer = self.queue_shortest_job.pop(0)  # Pick the shortest job
                else:
                    continue
                
                # Track customer waiting time
                wait_time = time.time() - customer.arrival_time
                self.wait_times.append(wait_time)
                self.total_tasks += 1
                
                agent = available_agents[self.current_rr_index % len(available_agents)]
                self.current_rr_index += 1  # Rotate index for Round Robin
                agent.available = False
                print(f"Agent {agent.agent_id} is serving Customer {customer.customer_id}")

                threading.Thread(target=self.complete_task, args=(agent, customer)).start()
                time.sleep(1)

    def complete_task(self, agent, customer):
        time.sleep(customer.service_time)
        print(f"Customer {customer.customer_id} served by Agent {agent.agent_id}")
        agent.available = True
        self.agent_utilization[agent.agent_id] += customer.service_time

    def monitor_agents(self):
        while True:
            time.sleep(5)  # Update every 5 seconds
            print("Agent Status Update:")
            for agent in self.agents:
                status = "Available" if agent.available else "Busy"
                print(f"Agent {agent.agent_id}: {status}")

            if self.total_tasks > 0:
                total_wait_time = sum(self.wait_times) or 1  # Prevent division by zero
                avg_wait_time = total_wait_time / len(self.wait_times)
                utilization_rate = {
                    agent_id: (util / total_wait_time) * 100 for agent_id, util in self.agent_utilization.items()
                }
                print(f"Average Wait Time: {avg_wait_time:.2f} seconds")
                print(f"Agent Utilization: {utilization_rate}")
