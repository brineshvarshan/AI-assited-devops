FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent code
COPY agent/ ./agent/

# Set Python path
ENV PYTHONPATH=/app

# Run the agent
CMD ["python", "agent/main_agent.py"]
