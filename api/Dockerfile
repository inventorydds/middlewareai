FROM python:3.10-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    curl && \
    rm -rf /var/lib/apt/lists/*

# Install Python libraries
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    pandas \
    llama-cpp-python --extra-index-url https://jllllll.github.io/llama-cpp-python-cuBLAS-wheels/AVX2

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
