import os
import pkgutil
import importlib
import sys
from app.commands import CommandHandler, Command
from dotenv import load_dotenv
import logging
import logging.config

class App:
    def __init__(self):  # Constructor
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()  # Loads the .env file contents
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def load_plugins(self):
        # Dynamically load all plugins in the commands directory
        commands_package = 'app.commands'
        for _, command_name, is_pkg in pkgutil.iter_modules([commands_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                command_module = importlib.import_module(f'{commands_package}.{command_name}')
                for item_name in dir(command_module):
                    item = getattr(command_module, item_name)
                    try:
                        if issubclass(item, Command):  # Ensure it's a Command subclass
                            self.command_handler.register_command(command_name, item())
                    except TypeError:
                        continue  # Ignore if it's not a Command class

        #Load commands from plugins
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command):  # Ensure it's a Command subclass
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # Ignore if it's not a Command class
    def start(self):
        # Register commands here
        self.load_plugins()  # Ensure commands are loaded
        logging.info("Application started.")
        print("Type 'exit' to exit.")
        while True:
            command_input = input(">>> ").strip()
            if command_input.lower() == 'exit':
                sys.exit("Exiting...")
            self.command_handler.execute_command(command_input)
