How to read the file data under api automation in case the configuration file and execution file is on another folder under project;
If your folder structure is as below:
  project/
  │
  ├── config/
  │   └── config.ini
  │
  ├── scripts/
  │   └── read_config.py
How you can read this:
  import configparser
  import os

  config = configparser.ConfigParser()

  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  config_path = os.path.join(BASE_DIR, "config", "config.ini")

  config.read(config_path)

  print(config["database"]["host"])
> Why this works?
  __file__ → location of the running script

  Works regardless of where PyCharm runs the file from

  Safe for automation frameworks (pytest, FastAPI, Selenium, API tests)
