# This is my first Python script!

print('Hello Analyst!')
print('Welcome to Pyhton for Cybersecurity!')

# Week 1 - Python Basics
# Author: Curtis Harris
# Purpose: Print some basic info about the system

analyst_name = input("enter your name: ")
system_role = input("Enter this system's role (e.g., web server, workstation): ")

# Code for the systems Platform and os to be printed with current user.

import platform
import os
print ("n--- System Information ---")
print ("Hostname:", platform.node())
print ("Operating System:", platform.system(), platform.release())
print ("Current User:", os.getlogin())

# Added code to display the information of the entered analyst name and role.

print(f"\nSecurity Report for {analyst_name}")
print("-------------------------------")
print("System Role:", system_role)
print("Hostname:", platform.node())
print("Operating System:", platform.system(), platform.release())
print("Current User:", os.getlogin())
