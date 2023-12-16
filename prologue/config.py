from addict import Dict
import toml


with open("config.toml", "r") as file:
    CFG = Dict(toml.load(file))
