print("Starting Flask server...")  # Debugging print
import sys
import os
from flask import Flask, request, jsonify
from scheduler import ResourceScheduler
from models import Customer

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

print("Flask module imported successfully.")  # Debugging print

app = Flask(__name__)

# Initializing scheduler with 3 agents
scheduler = ResourceScheduler(num_agents=3)
print("Scheduler initialized.")  # Debugging print

# Default homepage route to prevent 404 errors
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Resource-Scheduler API! Available endpoints: /add_customer (POST), /start_scheduler (GET)"}), 200

@app.route('/add_customer', methods=['POST'])
def add_customer():
    print("Received request to add customer.")  # Debugging print
    data = request.get_json()
    customer = Customer(data['customer_id'], data['priority'], data['service_time'])
    scheduler.assign_task(customer, method="priority")
    return jsonify({"message": "Customer added to queue", "customer_id": data['customer_id']}), 201

@app.route('/start_scheduler', methods=['GET'])
def start_scheduler():
    print("Received request to start scheduler.")  # Debugging print
    import threading
    threading.Thread(target=scheduler.process_tasks, args=("priority",), daemon=True).start()
    return jsonify({"message": "Scheduler started"}), 200

if __name__ == '__main__':
    print("Flask is running on http://0.0.0.0:5002")
    app.run(debug=True, host='0.0.0.0', port=5002)
