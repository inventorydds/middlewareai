FROM python:3.10-slim

RUN apt update && apt install -y build-essential cmake git curl && apt clean

WORKDIR /app

# Install llama-cpp-python (CPU-only version)
RUN pip install llama-cpp-python

# Optional: Add jupyter or chromadb client if needed
# RUN pip install jupyter chromadb

COPY . .

CMD ["python", "run_llm.py"]
