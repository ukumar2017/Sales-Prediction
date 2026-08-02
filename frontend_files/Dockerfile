
#Use the minimal base image with Python 3.12 installed
FROM python:3.12-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy all files from the current directory to the container's / app directory
COPY . .

# Install the required dependencies mentioned in requirements.txt
RUN pip3 install -r requirements.txt

# Expose port of streamlit
EXPOSE 3000

# Define the command to run the streamlit app on port 3000 and make it accessible externally
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=3000", "--server.address=0.0.0.0", "--server.enableXsrfProtection=false"]
