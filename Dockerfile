# Use the official NGINX image as the base
FROM nginx:latest

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install MySQL connector for Python
# Use --break-system-packages to allow pip installation in externally-managed environment
RUN pip3 install mysql-connector-python --break-system-packages

# Copy the Python script to the container
COPY app.py /app.py

# Set the environment variables for MySQL (these will be overridden by Docker run)
ENV MYSQL_HOST=mysql_db
ENV MYSQL_PORT=3306
ENV MYSQL_PASSWORD=rootpassword
ENV MYSQL_DATABASE=mydb

# Run the Python script to connect to MySQL
CMD ["python3", "/app.py"]
