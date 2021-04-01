FROM continuumio/miniconda3

WORKDIR /home

# Install cron for scheduling
RUN apt-get update && apt-get -y install cron

# Copy hello-cron file to the cron.d directory
COPY main-cron /etc/cron.d/main-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/main-cron

COPY . .
#RUN conda env create -f environment.yml
#SHELL ["conda", "run", "-n", "FTX_lending", "/bin/bash", "-c"]
RUN conda env update --name base --file environment.yml
RUN python telegram_bot/add_id.py &&python main.py
RUN python main.py
# Apply cron job
RUN crontab /etc/cron.d/main-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

CMD ["cron", "-f"]
