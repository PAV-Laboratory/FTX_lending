# FTX_lending

## Contents
* [Prerequisites](#Prerequisites)
* [Installing](#Installing)

## Prerequisites
In this project, we will dockerize all the necessary dependencies. Therefore, here will show the steps of installing all the necessary dependencies by docker **only**. If installing the dependencies in your local or virtual environment is more preferable in your case, please feel free to go through `DockerFIle` and `docker-compose.yml` as your reference.

1. [Docker](https://www.docker.com/products/docker-desktop)

   Version:
   * 20.10.5
   
   Installation:
   * `wget -qO- https://get.docker.com/ | sed 's/lxc-docker/lxc-docker-20.10.5/' | sh`
   
   Grant Permission:
   * `sudo usermod -aG docker <username>`
   * example for AWS ubuntu default user `sudo usermod -aG docker ubunut`
   <br/>
2. [Docker Compose](https://docs.docker.com/compose/install/)

   Version:
   * 12.8.2
   
   Installation:
   * `sudo curl -L "https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
   
   Executable Permission:
   * `sudo chmod +x /usr/local/bin/docker-compose`

3. Clone the repo and get into the repo

   * `git clone git@github.com:cfcdavidchan/FTX_lending.git`
   * `cd FTX_lending`

4. Create the config file

* cp ./config.ini.sample ./config.ini
   * Input all the input and the belows steps will show how to obtain all the necessary API key or explain what the config means.

5. FTX config

   API KEY & API SECRET
   * Browsing [FTX Profit page](https://ftx.com/profile) and create API KEY and API SECRET. Please remember to save the API SECRET which will never be showed after you close it
   
   coins
   * The target coins the you are willing to update
   * e.g. `coins = USD,BTC` remember that there is only comma without space between

   coins_hold
   * The amount of a currecy that you want to hold on hand and not lend it out.
   * e.g. `USD,0;BTC,100` means you want to lend out all the USD and you want to hold 100 units BTC on hand.
6. Telegram config
   
   Add BotFather in telegram
   * search `@BotFather` in telegram
   
   Create your own telgram bot
   * type `/newbot` and follow the step to type the name of the bot and the username of the bot
   
   Obtain the API
   * In the reply message from BotFather you will find the api of your bot and you could start chat with your bot by clicking `t.me/<bot name>`
   
   Send a message to your bot
   * click start and send a message to your bot
   * Sending a message is very important step because we need this message to get your telegram id

   Add to config
   * add Telegram API to config.ini
   * add your telegram id, which you sent the message to the bot in the previos step, to config.ini


7. Running the container

   Execute the application
   * `./docker-compose up --build`
