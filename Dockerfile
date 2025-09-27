FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential software-properties-common curl wget git unzip nano vim \
    python3 python3-pip python3-venv python3-dev ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /

COPY requirements-audio.txt .

# Install Python packages including visualization libraries
RUN pip install --upgrade pip && \
    pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu && \
    pip install librosa soundfile numpy pandas matplotlib seaborn scikit-learn && \
    pip install jupyter transformers datasets && \
    pip install -r requirements-audio.txt --ignore-errors || true

COPY README.md .
COPY sample.ipynb .

# Expose Jupyter port
EXPOSE 8888

# Default command: start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]