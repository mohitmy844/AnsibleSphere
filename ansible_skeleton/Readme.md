# Ansible Project Skeleton Creation Scripts

This folder contains three Python scripts designed to create the basic directory structure for an Ansible project. Each script offers a different approach to structuring the project, allowing you to choose the best fit for your needs.

## 1. `create_project_skeleton_along_with_role.py`

This script creates a comprehensive Ansible project skeleton, including a `roles` directory with a `common` role. The `common` role contains subdirectories for tasks, handlers, templates, files, vars, defaults, meta, and tests. It also includes a `library`, `module_utils`, and `lookup_plugins` directory for custom Ansible components.

**Features:**

- Creates a structured `roles` directory with a `common` role.
- Includes subdirectories for tasks, handlers, templates, files, vars, defaults, meta, and tests within the `common` role.
- Provides directories for custom `library`, `module_utils`, and `lookup_plugins`.

**Usage:**

1. Replace `"your_base_directory_path"` with the desired location for your Ansible project.
2. Run the script: `python create_project_skeleton_along_with_role.py`

## 2. `create_project_skeleton_along_with_role_and_content.py`

This script creates a similar project skeleton to the first script but also includes basic content within the files. This content serves as a starting point for your Ansible playbooks and roles.

**Features:**

- Creates a structured `roles` directory with a `common` role.
- Includes subdirectories for tasks, handlers, templates, files, vars, defaults, meta, and tests within the `common` role.
- Provides directories for custom `library`, `module_utils`, and `lookup_plugins`.
- Includes basic content within the files, such as comments and placeholder code.

**Usage:**

1. Set the `root_directory` variable to the desired location for your Ansible project.
2. Run the script: `python create_project_skeleton_along_with_role_and_content.py`

## 3. `create_project_skeleton_along_without_role.py`

This script creates a more basic Ansible project skeleton, focusing on the essential directories for playbooks, inventories, and custom modules. It does not include a `roles` directory.

**Features:**

- Creates directories for `inventories`, `library`, `module_utils`, `filter_plugins`, and `playbooks`.
- Includes basic inventory files (`hosts`) for production and staging environments.
- Creates a `playbook.yml` file within the `playbooks` directory.

**Usage:**

1. Run the script: `python create_project_skeleton_along_without_role.py`

## Choosing the Right Script

- **`create_project_skeleton_along_with_role.py`:** Use this script if you want a comprehensive project structure with a `roles` directory and a `common` role.
- **`create_project_skeleton_along_with_role_and_content.py`:** Use this script if you want a comprehensive project structure with basic content within the files.
- **`create_project_skeleton_along_without_role.py`:** Use this script if you want a basic project structure without a `roles` directory.

These scripts provide a solid foundation for your Ansible projects. You can customize them further to suit your specific needs and preferences.

**Author:** Mohit Yadav
