FROM mysql:latest

# Expose the port for MySQL
WORKDIR /app
# Create a volume for MySQL data
VOLUME /var/lib/mysql

# Set environment variables
ENV ACCEPT_EULA=Y
ENV MYSQL_ROOT_PASSWORD=pass1234
ENV MSSQL_TCP_PORT=3307


# Copy the SQL script to the container
COPY init.sql /docker-entrypoint-initdb.d

