# OPERATING SYSTEMS | TASK 2

#### Tumukunde Markjoe
 sep22/bsc/1647u

#### Wandira Kevin 
 may22/bist/1566u

#### Mugendi Amujjadi
Sep23/bist/3749u

#### Resource Scheduler
This project is a Resource Scheduler designed to optimize the allocation of bank tellers or call center agents to customer requests. The scheduler minimizes wait times, maximizes resource utilization and ensures fairness in task distribution.

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

### How the project starts.
- The main script simulation.py initializes and runs the project by:
  - Importing required modules (random, time, threading)
  - Creating a scheduler instance (ResourceScheduler)
  - Generating random customers with different priorities
  - Assigning tasks based on priority
  - Running a background thread to process scheduled tasks

### Running the Project
To start the project, follow these steps:
- Ensure dependencies are installed:
- Run the simulation script:
This will start the scheduler, generate customers, and assign them tasks based on priority.

### Breakdown of simulation.py
1. #### Imports
- random & time: Simulate real-world randomness.
- scheduler & models: Import project-specific classes.
- threading: Allows background task processing.

2. #### Customer Simulation
- Generates 10 customers with random priority and service time.
- Assigns tasks to the scheduler based on priority scheduling.
- Introduces random wait times between customer arrivals.

3. #### Customer Simulation
- Generates 10 customers with random priority and service time.
- Assigns tasks to the scheduler based on priority scheduling.
- Introduces random wait times between customer arrivals.Initializing the Scheduler
  - Creates a ResourceScheduler with 3 worker agents.
  - Runs the scheduler processing in a separate thread.
  - Starts simulating customer requests.
  - Keeps the script running until manually stopped (Ctrl+C).

4. #### Initializing the Scheduler
- Creates a ResourceScheduler with 3 worker agents.
- Runs the scheduler processing in a separate thread.
- Starts simulating customer requests.
- Keeps the script running until manually stopped (Ctrl + C)

#### Breakdown of ResourceScheduler
The ResourceScheduler class is responsible for managing task assignments and scheduling.
#### Key Responsibilities:
- Implements three scheduling methods:
  - Priority Scheduling – Higher priority customers get served first.
  - Round Robin Scheduling – Customers are served in a rotating order.
  - Shortest Job Next – Customers with the shortest service time are served first.
- Manages a set number of agents (workers).
- Uses multi-threading to handle concurrent tasks.
- Tracks waiting times and agent utilization.

#### Class Breakdown
1. Initialization (__init__)
- Creates worker agents.
- Initializes three different queues for task scheduling.
- Uses a thread lock to prevent race conditions.

2. Assigning Tasks (assign_task)
- Assigns customers to different queues based on scheduling method.
- Sorts Shortest Job Next tasks by service time.

3. Processing Tasks (process_tasks)
- Finds available agents.
- Picks the next customer task based on the selected scheduling method.
- Assigns an agent and starts processing in a new thread.

4. Completing Tasks (complete_task)
- Simulates task execution.
- Releases the agent after completion.

5. Monitoring Agents (monitor_agents****)
- Prints agent status updates every 5 seconds.
- Tracks average wait time and agent utilization.

6. Customer Class
- Defines customer properties and priority comparison.

7. Agent Class
- Represents an agent that can handle tasks.

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
