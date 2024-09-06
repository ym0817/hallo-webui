# Use an official Python runtime as a parent image
FROM nvidia/cuda:12.2.0-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory in the container to /app
WORKDIR /app

# Install dependencies & python
RUN apt-get update && apt-get install -y --no-install-recommends git wget bzip2 ffmpeg gcc g++ software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa && apt update && apt install -y python3.11

RUN apt install -y python3-pip

# Clone the GitHub repository and checkout to the correct branch/tag
RUN git clone https://github.com/moda20/hallo-webui.git .

# Run install.sh to perform any setup or installations required before setting up the virtual environment

RUN chmod +x install.sh && ./install.sh

RUN pip install --upgrade pip

# Expose port 7860 for the gradio app
EXPOSE 7860

RUN ln -s /usr/bin/python3 /usr/bin/python


RUN chmod +x start_docker.sh

# Run start.sh when the container starts
CMD ["./start_docker.sh"]