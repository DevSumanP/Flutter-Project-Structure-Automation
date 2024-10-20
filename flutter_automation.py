import os
import subprocess

# Define the folder structure for the Flutter project
folder_structure = {
    "assets": {
        "images": {},
        "fonts": {},
    },
    "lib": {
        "core": {
            "config": {},
            "constants": {},
            "secrets": {},
            "service": {},
            "error": {},
            "usecases": {},
            "utils": {},
        },
        "features": {
            "feature_name": {
                "data": {
                    "datasources": {},
                    "models": {},
                    "repositories": {},
                },
                "domain": {
                    "entities": {},
                    "repositories": {},
                    "usecases": {},
                },
                "presentation": {
                    "bloc": {},
                    "pages": {},
                    "widgets": {},
                },
            }
        }
    },
}

# Packages to be added using flutter pub add
required_packages = [
    "flutter_bloc", 
    "equatable", 
    "google_fonts", 
    "iconly",
    "firebase_core",
    "firebase_cloud",
    "dio"
]

# Content of the README file
readme_content = """# 📝 Project Name

## 🛠️ Technologies

## ✨ Features

## 🚦 Running the Project

To run the project locally, follow these steps:

## 📦 Project Structure 

## How It Works

## 🎥 Photos and Videos
"""

# Function to create the folder structure
def create_folders(base_path, structure):
    for folder, subfolders in structure.items():
        path = os.path.join(base_path, folder)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created folder: {path}")
        if isinstance(subfolders, dict):
            create_folders(path, subfolders)

# Function to add required Flutter packages
def add_flutter_packages(project_path, packages):
    flutter_path = r"C:\src\flutter\bin"  # Replace with your actual Flutter SDK path
    os.environ["PATH"] += os.pathsep + flutter_path  # Update the PATH variable

    for package in packages:
        try:
            # Run flutter pub add command for each package
            command = f"flutter pub add {package}"
            result = subprocess.run(
                ["powershell", "-Command", command], 
                cwd=project_path, 
                capture_output=True, 
                text=True, 
                check=True
            )
            print(f"Successfully added package: {package}")
            print(result.stdout)  # Print output from the command
        except subprocess.CalledProcessError as e:
            print(f"Error adding package {package}: {e.stderr}")  # Print any errors

# Function to run flutter pub get
def run_flutter_pub_get(project_path):
    flutter_path = r"C:\src\flutter\bin"  # Replace with your actual Flutter SDK path
    os.environ["PATH"] += os.pathsep + flutter_path  # Update the PATH variable

    try:
        # Run flutter pub get command
        command = "flutter pub get"
        result = subprocess.run(
            ["powershell", "-Command", command], 
            cwd=project_path, 
            capture_output=True, 
            text=True, 
            check=True
        )
        print("flutter pub get executed successfully!")
        print(result.stdout)  # Print output from the command
    except subprocess.CalledProcessError as e:
        print(f"Error executing flutter pub get: {e.stderr}")  # Print any errors

# Function to display a friendly coding message
def print_happy_coding_pattern():
    print("\n😊 Happy Coding!")  # Print a message at the end

# Function to create a README.md file
def create_readme(base_path, content):
    readme_path = os.path.join(base_path, "README.md")
    with open(readme_path, 'w', encoding= "utf-8") as file:
        file.write(content)
    print(f"Created README.md file at: {readme_path}")

# Main function to generate the Flutter folder structure and add packages
def main():
    base_path = input("Enter the path to your Flutter project directory: ")
    
    if os.path.exists(base_path):
        # Create the folder structure
        create_folders(base_path, folder_structure)
        print("Clean architecture folder structure created successfully!")

        # Add required Flutter packages
        add_flutter_packages(base_path, required_packages)

        # Create a README.md file
        create_readme(base_path, readme_content)

        # Run Flutter commands
        run_flutter_pub_get(base_path)

        # Print the happy coding message
        print_happy_coding_pattern()
    else:
        print("The specified directory does not exist. Please check the path and try again.")

if __name__ == "__main__":
    main()
