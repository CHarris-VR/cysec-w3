
# Get user input for name and Department they work in.
analyst_name = input("enter your name: ")
dept_role = input("Enter which Department you are from(e.g., Security, Management): ")


# Printing the Security Analyst role, department, and system information.
print(f"  Security Report for {dept_role}")
print("-------------------------------")
print("System Role:", system_role)
print("Hostname:", platform.node())
print("Operating System:", platform.system(), platform.release())
print("Current User:", os.getlogin())