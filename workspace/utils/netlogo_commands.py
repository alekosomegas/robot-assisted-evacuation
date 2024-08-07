"""
NetLogo commands and reporters used in the simulation
"""

NETLOGO_VERSION = "5"

SEED_SIMULATION_REPORTER = "seed-simulation {}"
EVACUATION_FINISHED_REPORTER = "evacuation-finished?"

SET_SIMULATION_ID_COMMAND = 'set SIMULATION_ID "{}"'
SET_FALL_LENGTH_COMMAND = "set DEFAULT_FALL_LENGTH {}"
SET_FRAME_GENERATION_COMMAND = "set ENABLE_FRAME_GENERATION {}"
SET_FALL_LENGTH_COMMAND = "set DEFAULT_FALL_LENGTH {}"
SET_FALL_CHANCE_COMMAND = "set FALL_CHANCE {}"

SET_NUM_OF_ROBOTS_COMMAND = "set NUM_OF_ROBOTS {}"
SET_NUM_OF_PASSENGERS_COMMAND = "set NUM_OF_PASSENGERS {}"
SET_NUM_OF_STAFF_COMMAND = "set NUM_OF_STAFF {}"
SET_ROOM_ENVIRONMENT_TYPE = "set ROOM_ENVIRONMENT_INDX {}"
SET_ROBOT_PERSUASION_FACTOR = "set ROBOT_PERSUASION_FACTOR {}"

ENABLE_FRAME_GENERATION_COMMAND = SET_FRAME_GENERATION_COMMAND.format("TRUE")
