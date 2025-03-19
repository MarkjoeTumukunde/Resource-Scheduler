FROM python:3.9

# Set working directory clearly
WORKDIR /app

# Copy requirements explicitly first for efficiency
COPY requirements.txt /app/requirements.txt

# Install dependencies clearly
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project files
COPY . /app

# Expose Flask port clearly
EXPOSE 5000

# Run your Flask application (main.py) clearly
CMD ["python", "app/main.py"]
