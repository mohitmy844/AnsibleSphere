import os

# Define the directory structure
directories = [
    "inventories/production/group_vars",
    "inventories/production/host_vars",
    "inventories/staging/group_vars",
    "inventories/staging/host_vars",
    "library",
    "module_utils",
    "filter_plugins",
    "playbooks",
    "playbooks/project_name"
]

# Create the directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create the inventory files
with open("inventories/production/hosts", "w") as f:
    f.write("# inventory file for production servers\n")
with open("inventories/staging/hosts", "w") as f:
    f.write("# inventory file for staging environment\n")
with open("playbooks/project_name/playbook.yml", "w") as f:
    f.write("# This is main playbook\n")
# Print a success message
print("Directory structure created successfully.")
