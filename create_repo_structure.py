import os

# Define the repository structure
structure = {
    "data": ["raw", "processed"],
    "notebooks": ["01_data_cleaning.ipynb", "02_data_exploration.ipynb", "03_feature_engineering.ipynb", "04_modeling.ipynb", "05_visualization.ipynb"],
    "app": {
        "templates": ["index.html"],
        "static": ["styles.css"],
        "files": ["app.py"]
    },
    "files": ["README.md", "requirements.txt"]
}

# Function to create directories and files
def create_structure(base_path, structure):
    for key, value in structure.items():
        path = os.path.join(base_path, key)
        if isinstance(value, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, value)
        elif isinstance(value, list):
            os.makedirs(path, exist_ok=True)
            for item in value:
                if '.' in item:
                    open(os.path.join(path, item), 'w').close()
                else:
                    os.makedirs(os.path.join(path, item), exist_ok=True)
        else:
            open(os.path.join(base_path, value), 'w').close()

# Create the repository structure
repo_name = "air-quality-analysis"
base_path = os.path.join(os.getcwd(), repo_name)
os.makedirs(base_path, exist_ok=True)
create_structure(base_path, structure)

print(f"Repository structure for '{repo_name}' created successfully!")