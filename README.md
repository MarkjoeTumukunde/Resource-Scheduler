# Resource Scheduler

This project is a Resource Scheduler designed to optimize the allocation of bank tellers or call center agents to customer requests. The scheduler minimizes wait times, maximizes resource utilization, and ensures fairness in task distribution.

## Features

- Simulates customer arrivals with randomized service times and priority levels (VIP, Corporate, Normal).
- Dynamically assigns employees (bank tellers or agents) based on availability and workload.
- Implements scheduling algorithms:
  - Round Robin Scheduling
  - Priority Scheduling (VIP > Corporate > Normal)
  - Shortest Job Next
    - Real-time monitoring and updates every 5 seconds.
    - Performance metrics
  - Average customer waiting time
  - Agent utilization rate
  - Fairness in task distribution
  - Fully containerized using Docker.
  - Automated CI/CD deployment using GitHub Actions.

## Tech Stack

- Python (Flask) -> Web API
- Docker (Containerization)
- GitHub Actions -> CI/CD Automation


## Project Structure
Resource-Scheduler/
️│── app/                  # Main Flask application
️│   ├── main.py           # Flask server & API endpoints
️│   ├── scheduler.py      # Scheduling logic & task handling
️│   ├── models.py         # Data models for Customer & Agent
️│   └── simulation.py     # Simulates customer arrivals
️│── .github/workflows/    # CI/CD pipeline for GitHub Actions
️│── Dockerfile            # Docker container configuration
️│── requirements.txt      # Required Python dependencies
️│── README.md             # Project documentation

## Setup Instructions

### Step 1: Clone Repository
```zsh
git clone https://github.com/MarkjoeTumukunde/Resource-Scheduler.git
cd Resource-Scheduler
```

###  Step 2: Setup Python Virtual Environment
```zsh
python -m venv env
source env/bin/activate  # Mac/Linux
pip install -r requirements.txt
```
### Step 3: Run Flask Locally
``` zsh
cd app
python main.py
```
