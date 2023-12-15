# robison_sentinel
## Grabs oil level from robison website and catalogs it

### Quickstart
1) clone this repo
2) create a directory in the main directory `config`
    b) create file called `set_envvars.sh`
    c) fill that file with:
    ```
    export DEBUG_MODE=false
    export ROBISON_USERNAME=<your robison username>
    export ROBISON_PASSWORD=<your robison password>
    export EMAIL=<the email you will send alerts from>
    export PWD=<the password for that email>
    ```
3) `python main.py`

