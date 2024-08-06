import os
import shutil

# Define the base structure as a dictionary
directory_structure = {
    'inventories': {
        'production': {
            'hosts': None,
            'group_vars': {
                'group1.yml': None,
                'group2.yml': None
            },
            'host_vars': {
                'hostname1.yml': None,
                'hostname2.yml': None
            }
        },
        'staging': {
            'hosts': None,
            'group_vars': {
                'group1.yml': None,
                'group2.yml': None
            },
            'host_vars': {
                'stagehost1.yml': None,
                'stagehost2.yml': None
            }
        }
    },
    'library': None,
    'module_utils': None,
    'filter_plugins': None,
    'site.yml': None,
    'webservers.yml': None,
    'dbservers.yml': None,
    'roles': {
        'common': {
            'tasks': {
                'main.yml': None
            },
            'handlers': {
                'main.yml': None
            },
            'templates': {
                'ntp.conf.j2': None
            },
            'files': {
                'bar.txt': None,
                'foo.sh': None
            },
            'vars': {
                'main.yml': None
            },
            'defaults': {
                'main.yml': None
            },
            'meta': {
                'main.yml': None
            },
            'library': None,
            'module_utils': None,
            'lookup_plugins': None,
            'tests': {
                'test.yml': None
            },
            'inventories': {
                'prod.yml': None,
                'staging.yml': None
            }
        }
    }
}

def create_structure(base_path, structure):
    """
    Recursively creates directories and files from the nested dictionary.
    """
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif content is None:
            if '.' in name:
                # It's a file
                with open(path, 'w') as f:
                    pass
            else:
                # It's a directory
                os.makedirs(path, exist_ok=True)

# Starting path - adjust to your needs
base_path = 'your_base_directory_path'

# Create the directory structure
create_structure(base_path, directory_structure)

print("Directory structure created successfully.")
