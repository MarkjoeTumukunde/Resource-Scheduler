# Resource Scheduler

This project is a Resource Scheduler designed to optimize the allocation of bank tellers or call center agents to customer requests. The scheduler minimizes wait times, maximizes resource utilization, and ensures fairness in task distribution.

## 📌 Features

- Simulates customer arrivals with randomized service times and priority levels (VIP, Corporate, Normal).
- Dynamically assigns employees (bank tellers or agents) based on availability and workload.
- Implements scheduling algorithms:
  - Round Robin Scheduling
  - Priority Scheduling (VIP > Corporate > Normal)
  - Shortest Job Next
- Real-time monitoring and updates every 5 seconds.
- Performance metrics tracking:
  - Average customer waiting time
  - Agent utilization rate
  - Fairness in task distribution

## 🛠 Tech Stack

- Python
- Docker (Containerization)
- GitHub Actions (CI/CD)

## 🚀 Setup Instructions

### Step 1: Clone Repository

```bash
git clone <repository_url>
cd Resource-Scheduler
