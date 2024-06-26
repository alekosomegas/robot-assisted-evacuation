"""
This module defines the file and folder structure for the project.
"""

from datetime import datetime

# Base workspace folder, copy of this workspace in the container
WORKSPACE_FOLDER = "/home/workspace/"
# Contains Netlogo installation files
NETLOGO_HOME = "/home/netlogo_installation/"

# Contains the core logic of the project
CORE_FOLDER = WORKSPACE_FOLDER + "core/"
# Core subdirectories
# Coontains the model and config files
NETLOGO_FOLDER = CORE_FOLDER + "netlogo/"
# Contains the logic for running the simulations
SIMULATIONS_FOLDER = CORE_FOLDER + "simulations/"
# Contains the utility functions
UTILS_FOLDER = CORE_FOLDER + "utils/"

# Contains the logs
LOGS_FOLDER = WORKSPACE_FOLDER + "logs/"

# Contains the output of the simulations
RESULTS_FOLDER = WORKSPACE_FOLDER + "results/"
# Results subdirectories
DATA_FOLDER = RESULTS_FOLDER + "data/"
FRAMES_FOLDER = RESULTS_FOLDER + "frames/"
IMAGE_FOLDER = RESULTS_FOLDER + "img/"
VIDEO_FOLDER = RESULTS_FOLDER + "video/"
RESULTS_CSV_FILE = DATA_FOLDER + "experiments.csv"

# Contains the adaptation strategies
STRATEGIES_FOLDER = WORKSPACE_FOLDER + "strategies/"

CONFIG_FILE = WORKSPACE_FOLDER + 'config.json'
# Temporary file to store and retrieve active scenarios during execution
SCENARIOS_TEMP_FILE_NAME = 'scenarios_temp.json'
ROBOTS_ACTIONS_FILE_NAME = 'robots_actions_temp.csv'

EXPERIMENT_FOLDER_NAME = None


def get_experiment_folder():
    """
    Returns the name of folder for the current experiment.

    The folder name is generated using the current date and time in the format "yymmdd_HHMMSS".
    It is unique for each experiment and is used to store the results of the simulation.

    Returns:
        str: The name of the folder for the current experiment.
    """
    global EXPERIMENT_FOLDER_NAME
    if EXPERIMENT_FOLDER_NAME is None:
        EXPERIMENT_FOLDER_NAME = datetime.now().strftime("%y%m%d_%H%M%S")
    return EXPERIMENT_FOLDER_NAME
