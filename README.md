# PugBot

### Requirements
* Docker 18.06.1-ce or newer
* Docker-Compose (latest available version)
* Python 3.6.5 or newer (python 3.7.x not supported)
* Pip (latest available version)
* pyenv (latest available version)
* Homebrew (optional)
* Discord bot application and token (see [here](https://discordapp.com/developers/applications/))

### Local Development Setup
0. Install pyenv via Homebrew:

    `brew install pyenv`

1. Clone this repository

2. Install and set the local python version with pyenv:

    `pyenv install 3.6.8`
    
    `pyenv local 3.6.8`

    (Recommended) Verify python version with `python --version`:

    ```
     ~ > which python
    python is /Users/sboynton/.pyenv/shims/python
     ~ > python --version
    Python 3.6.8
    ```

2. Install virtualenv and create a new virtual environment:

    `python -m pip install virtualenv`

    `python -m virtualenv pugbot`

3. Activate the virtual environment:

    `source ./pugbot/bin/activate`

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