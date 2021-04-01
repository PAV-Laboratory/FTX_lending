FROM continuumio/miniconda3

WORKDIR /home

# Install cron for scheduling
RUN apt-get update && apt-get -y install cron

# Copy hello-cron file to the cron.d directory
COPY main-cron /etc/cron.d/main-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/main-cron

COPY . .
RUN conda env update --name base --file environment.yml
RUN tail config.ini
# Apply cron job
RUN crontab /etc/cron.d/main-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

