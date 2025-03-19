class Customer:
    def __init__(self, customer_id, priority, service_time):
        self.customer_id = customer_id
        self.priority = priority
        self.service_time = service_time

    def __lt__(self, other):
        return self.priority < other.priority

class Agent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.available = True
