import os

# Define the directory structure
directory_structure = {
    "inventories": {
        "production": {
            "hosts": "# inventory file for production servers",
            "group_vars": {
                "group1.yml": "# here we assign variables to particular groups",
                "group2.yml": "# here we assign variables to particular groups"
            },
            "host_vars": {
                "hostname1.yml": "# here we assign variables to particular systems",
                "hostname2.yml": ""
            }
        },
        "staging": {
            "hosts": "# inventory file for staging environment",
            "group_vars": {
                "group1.yml": "# here we assign variables to particular groups",
                "group2.yml": ""
            },
            "host_vars": {
                "stagehost1.yml": "# here we assign variables to particular systems",
                "stagehost2.yml": ""
            }
        }
    },
    "library": {},
    "module_utils": {},
    "filter_plugins": {},
    "playbooks":{
        "project_name1":{
            "playbook.yml": "#this is playbook"
        },
        "project_name2":{
            "playbook.yml": "#this is playbook"
        }        
    },
    "roles": {
        "common": {
            "tasks": {
                "main.yml": "# Main tasks file, can include smaller files if warranted"
            },
            "handlers": {
                "main.yml": "# Main handlers file"
            },
            "templates": {
                "ntp.conf.j2": "# Templates end in .j2"
            },
            "files": {
                "bar.txt": "# Static files for copying to hosts",
                "foo.sh": "# Script files for use with the script resource"
            },
            "vars": {
                "main.yml": "# Main variables file"
            },
            "defaults": {
                "main.yml": "# Main defaults file"
            },
            "meta": {
                "main.yml": "# Main meta file"
            },
            "library": {},
            "module_utils": {},
            "lookup_plugins": {},
            "tests": {
                "test.yml": "# Example test playbook"
            },
            "inventories": {
                "prod.yml": "# Production inventory",
                "staging.yml": "# Staging inventory"
            }
        }
    }
}

# Create the directory structure
def create_directory_structure(directory, structure):
    for item, content in structure.items():
        path = os.path.join(directory, item)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_directory_structure(path, content)
        elif isinstance(content, str):
            with open(path, "w") as file:
                file.write(content)

# Set the root directory
root_directory = "my_project"

# Create the directory structure
create_directory_structure(root_directory, directory_structure)

print(f"Directory structure created in {root_directory}")

