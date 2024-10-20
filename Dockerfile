# Use the official Ubuntu base image
FROM alpine:latest

# Update the package list and install Python
RUN apk add --no-cache bash python3 py3-pip py3-virtualenv

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