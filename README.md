
# Flutter Project Structure Automation Script

This Python script automates the creation of a Flutter project folder structure and the installation of required packages. It follows a clean architecture pattern and sets up the necessary directories for features, data, domain, and presentation layers.

## Features

- Creates a predefined folder structure for Flutter projects.
- Adds required Flutter packages using `flutter pub add`.
- Generates a `README.md` filte structure.
- Runs `flutter pub get` to fetch the dependencies.
- Displays a friendly coding message at the end.

## Prerequisites

- Python 3.x
- Flutter SDK installed on your machine
- PowerShell (for Windows users)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required Python packages (if needed):

   ```bash
   pip install subprocess
   ```

## Configuration

Before running the script, ensure that you have:

1. The path to your Flutter project directory.
2. The path to your Flutter SDK should be placed in the `flutter_path = r"C:\....." `

## Usage

To run the script:

1. Navigate to your Flutter project directory
2. Run the script using Python:

   ```bash
   python flutter_automation.py
   ```

3. When prompted, enter the path to your Flutter project directory and the Flutter SDK path.

## Example

```plaintext
Enter the path to your Flutter project directory: C:\path\to\your\flutter\project
```

## Notes

- Make sure to run the script in an environment where Python and Flutter are properly configured.
- The script will create the folder structure, add the necessary packages, and run `flutter pub get` to install dependencies.
- In case of errors during package installation, the error messages will be displayed in the terminal.

## Happy Coding!

😊 Enjoy building your Flutter applications with the generated structure!
