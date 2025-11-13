
# Get user input for name and Department they work in.
analyst_name = input("enter your name: ")
dept_role = input("Enter which Department you are from(e.g., Security, Management): ")

# Making a COOL TITLE so it can be EXTRA EPIC!!! :D
print("="*40)
print(" EvilCorp Cyber Defense - System Profile ")
print("="*40)


# Print the Security Analyst role, department

print(f"  Security Report for {analyst_name}")
print(f"  From the {dept_role} Department. ")


# Importing tools to call functions from windows system

import platform
import os
from datetime import datetime

# Print when the report was generated
print("-"*40)
print("Report Generated:", datetime.now())
print("-"*40)


# Print out of the system info and current user.

print("Department Role:", dept_role)
print("Hostname:", platform.node())
print("Operating System:", platform.system(), platform.release())
print("Current User:", os.getlogin())
print("-"*40)
print(" ")
print("Report generated successfully!")
print("-"*40)