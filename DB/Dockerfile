#FROM mysql:latest
#
## Expose the port for MySQL
#WORKDIR /app
## Create a volume for MySQL data
#VOLUME /var/lib/mysql
#EXPOSE 3306
#
## Set environment variables
#ENV ACCEPT_EULA=Y
##ENV MYSQL_ROOT_PASSWORD=pass1234
##ENV MYSQL_DATABASE=Animal_Shelter
#
#
#
## Copy the SQL script to the container
#COPY DB/init.sql /docker-entrypoint-initdb.d



FROM mysql:latest

# Expose the port for MySQL
WORKDIR /app
# Create a volume for MySQL data
#VOLUME /var/lib/mysql
EXPOSE 3306

# Set environment variables
ENV ACCEPT_EULA=Y
ENV MYSQL_ROOT_PASSWORD pass1234
#ENV MYSQL_DATABASE=Animal_Shelter



# Copy the SQL script to the container
COPY /init.sql /docker-entrypoint-initdb.d
