import logging
from app.commands.data_command import DataCommand  # Adjust the import based on your structure

def main():
    logging.basicConfig(level=logging.INFO)  # Set up logging
    command = DataCommand()  # Create an instance of DataCommand
    command.execute()  # Execute the command

if __name__ == '__main__':
    main()