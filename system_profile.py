
# Get user input for name and Department they work in.
analyst_name = input("enter your name: ")
dept_role = input("Enter which Department you are from(e.g., Security, Management): ")


# Print the Security Analyst role, department and date time of creation
print("-------------------------------")
print(f"  Security Report for {analyst_name}")
print(f"  From the {dept_role} Department. ")
print(" ")
print("Report Generated:", datetime.now())
print("-------------------------------")

# Importing tools to call functions from windows system
import platform
import os
from datetime import datetime


# Print out of the system info and current user.
print("Department Role:", dept_role)
print("Hostname:", platform.node())
print("Operating System:", platform.system(), platform.release())
print("Current User:", os.getlogin())
print("-------------------------------")
print(" ")
print("Report generated successfully!")
print("-------------------------------")