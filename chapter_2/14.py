import os

command = "dir" if os.name == "nt" else "ls"
output = os.popen(command).read()
print(f"Result of command {command}:\n{output}")