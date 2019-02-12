import logging
import sys
import os
import datetime


class Simulation:
    name = ""
    base_path = ""
    parameters = {}
    data_files = []
    simulation_parameters_logfile = ""
    simulation_start_time = 0
    simulation_script = ""
    simulation_function = None
    simulation_code_type = None

    def __init__(self, name, base_path, simulation_function=None, simulation_script=None):

        self.base_path = base_path
        self.name = name
        self.simulation_parameters_logfile = os.path.join(base_path, "simulation_parameters.txt")

        logging.info("Creating a simulation '{}' with base path: {}".format(name, base_path))

        if simulation_function is not None:
            self.set_simulation_function(simulation_function)
        elif simulation_script is not None:
            if not os.path.exists(simulation_script):
                raise ValueError("The specified simulation script does not exist.")
            self.set_simulation_script(simulation_script)

    def run(self):
        logging.info("Running the simulation")

        if os.path.exists(self.base_path):
            print("The path {} already exists. Aborting.".format(self.base_path))

        os.makedirs(self.base_path)
        self.simulation_start_time = datetime.datetime.now()

        self.write_simulation_parameters_logfile()

        if self.simulation_code_type == "function":
            logging.info("Running a function")


    def write_simulation_parameters_logfile(self):
        fh = open(self.simulation_parameters_logfile, "w")
        fh.write("Simulation: {}\n".format(self.name))
        fh.write("Start timestamp: {}\n".format(str(self.simulation_start_time)))
        fh.write("\n")
        fh.write("Parameters\n")
        for parameter_name, parameter_value in self.parameters:
            fh.write("{}={}".format(parameter_name, parameter_value))
        fh.close()

    def set_simulation_function(self, simulation_function):
        self.simulation_function = simulation_function
        self.simulation_code_type = "function"

    def set_simulation_script(self, simulation_script):
        self.simulation_script = simulation_script
        self.simulation_code_type = "script"
