# Use the official Ubuntu base image
FROM ubuntu:latest

# Set environment variables to prevent prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install Python
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Verify installation by printing Python version
RUN python3 --version

# Set the working directory to "/home/data"
RUN mkdir -p /home/data
WORKDIR /home/data

# Create virtual environment
RUN python3 -m venv /home/data/venv

# Activate the virtual environment
RUN . /home/data/venv/bin/activate && pip install contractions

# Copy the text Files to "/home/data"
COPY IF.txt /home/data
COPY AlwaysRememberUsThisWay.txt /home/data

# Copy the Python scripts to "/home/data"
COPY *.py /home/data

# Run the Python scripts
CMD ["/bin/bash", "-c", ". venv/bin/activate && python3 main.py && cat result.txt"]