# PugBot

### Requirements
* Docker 18.06.1-ce or newer
* Docker-Compose (latest available version)
* Python 3.6.5 or newer (python 3.7.x not supported)
* Pip (latest available version)
* pyenv-virtualenv (optional; latest available version)
* Discord bot application and token (see [here](https://discordapp.com/developers/applications/))

### Local Development Setup
1. Clone this repository

2. Create a new virtual environment
    * Using standard virtualenv (e.g. if system python is 3.6.x):

        `python -m virtualenv pugbot`

    * Using pyenv-virtualenv (e.g. if system python is >3.6.x<):

        `pyenv virtualenv 3.6.5 pugbot`
3. Activate the virtual environment:

    * Using standard virtualenv (e.g. if system python is 3.6.x):
    
        `source ./pugbot/bin/activate`

    * Using pyenv-virtualenv (e.g. if system python is >3.6.x<):

        `pyenv activate pugbot`
4. Install the pip requirements:

    `pip install -r requirements.txt`
5. Create pugbot.cfg:

    ```
    [DEFAULT]
    BOT_TOKEN = your.token.here
    ```
6. Run the bot locally:

    `python main.py`

### Docker setup
1. Clone this repository
2. Build the image:

    `docker-compose build`
3. Run the image:

    `docker-compose up -d`