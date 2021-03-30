FROM continuumio/miniconda3

WORKDIR /home
COPY . .
#RUN conda env create -f environment.yml
#SHELL ["conda", "run", "-n", "FTX_lending", "/bin/bash", "-c"]
RUN conda env update --name base --file environment.yml
