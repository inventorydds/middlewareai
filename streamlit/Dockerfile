FROM python:3.10-slim

WORKDIR /app

# Install system dependencies (optional but useful)
RUN apt-get update && apt-get install -y curl && apt-get clean

# Copy your app files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir streamlit chromadb

# Expose default Streamlit port
EXPOSE 8501

# Launch the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
