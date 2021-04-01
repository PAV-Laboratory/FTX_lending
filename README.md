# FTX_lending

## Contents
* [Prerequisites](#Prerequisites)
* [Installing](#Installing)

## Prerequisites
In this project, we will dockerize all the necessary dependencies. Therefore, here will show the steps of installing all the necessary dependencies by docker **only**. If installing the dependencies in your local or virtual environment is more preferable in your case, please feel free to go through `DockerFIle` and `docker-compose.yml` as your reference.

1. [Docker](https://www.docker.com/products/docker-desktop)
   **_Version:_**
   * 20.10.5
   <br/>
   **_Installation:_**
   * `wget -qO- https://get.docker.com/ | sed 's/lxc-docker/lxc-docker-20.10.5/' | sh`
   **_Grant Permission:_**
   * `sudo usermod -aG docker <username>`
   * example for AWS ubuntu default user `sudo usermod -aG docker ubunut`
   <br/>
2. Download [Docker Compose](https://docs.docker.com/compose/install/)
    **_Version:_**
   * 12.8.2
   <br/>
   **_Installation:_**
   * `sudo curl -L "https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
   **_Executable Permission:_**
   * `sudo chmod +x /usr/local/bin/docker-compose`
   <br/>

3. Clone the repo
    * `git clone git@github.com:cfcdavidchan/FTX_lending.git`
4. Running the container


- `./docker-compose up --build`
