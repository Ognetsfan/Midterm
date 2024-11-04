Strategy Pattern:
The Strategy pattern allows the selection of an algorithm's behavior at runtime. In my calculator application, this pattern is utilized to enable users to choose various arithmetic operations (add, subtract, multiply, divide) dynamically. Each operation is encapsulated in its own class, allowing for easy extension of new operations without modifying existing code.
https://github.com/Ognetsfan/Midterm/blob/main/Calculator/__init__.py


Command Pattern:
The Command pattern encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations. In this application, the Command pattern is implemented to handle various commands (like greet, exit, and arithmetic operations) through a unified interface. This provides flexibility to add new commands without changing the existing command handler's structure.
https://github.com/Ognetsfan/Midterm/blob/main/app/commands/__init__.py

Use of Environment Variables:
I used environment variables to manage configuration settings securely and flexibly. By utilizing the dotenv library, I can load configuration options from a .env file, which keeps sensitive information (like database credentials) out of the source code. This approach allows me to change configurations without modifying the codebase and makes it easier to manage different environments (development, testing, production).
https://github.com/Ognetsfan/Midterm/blob/main/app/__init__.py

Use of Logging:
 I implemented a logging system to monitor the application's behavior and capture important events. By using Python's built-in logging module, I can log messages at different severity levels (INFO, WARNING, ERROR, CRITICAL) throughout the application. This not only helps with debugging during development but also provides insights into the application's operation when it's running in production.
 https://github.com/Ognetsfan/Midterm/blob/main/app/__init__.py
 https://github.com/Ognetsfan/Midterm/blob/main/logging.conf

 Use of Try/Catch and Exception Handling:
 LBYL: In my arithmetic classes, I check whether parameters provided to the execute method meet the necessary conditions before performing the arithmetic operation. For example, the parameter length as well as converting the parameters to floats.
 https://github.com/Ognetsfan/Midterm/blob/main/app/commands/divide/__init__.py
 https://github.com/Ognetsfan/Midterm/blob/main/app/commands/add/__init__.py
 https://github.com/Ognetsfan/Midterm/blob/main/app/commands/multiply/__init__.py
 https://github.com/Ognetsfan/Midterm/blob/main/app/commands/subtract/__init__.py
 EAFP: In my command class, I attempt to execute a command based on the user input. If the command does not exist, I catch the KeyError and inform the user, allowing the program to continue running instead of crashing.
 https://github.com/Ognetsfan/Midterm/blob/main/app/commands/__init__.py

Video: https://drive.google.com/file/d/1c314MOy843RHDhMvTG_Vm02WrsBS8Lrm/view?usp=sharing&t=1
