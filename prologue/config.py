from addict import Dict

import toml

# Load the TOML file into a dictionary
with open("config.toml", "r") as file:
    cfg_data = toml.load(file)


frames = Dict(cfg_data["frames"])
