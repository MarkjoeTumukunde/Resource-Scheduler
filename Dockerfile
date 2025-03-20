FROM python:3.9

# Sets working directory
WORKDIR /app

# Copies requirements explicitly first for efficiency
COPY requirements.txt /app/requirements.txt

# Installs dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Copies entire project files
COPY . /app

# Exposes Flask port
EXPOSE 5000

# Runs Flask application (main.py)
CMD ["python", "app/main.py"]
