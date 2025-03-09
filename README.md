# File-Organiser

## Overview

File-Organiser is a Python script designed to help you organize your files efficiently. It automatically organizes your file into subdirectory based on a specific naming convention

## Features
- Auto create and Move files to specific directories by naming convention

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Ofor-David/File-Organiser.git
    ```
2. Navigate to the project directory:
    ```sh
    cd File-Organiser
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
## Usage
In the directory where this script is runing, create any file and name it in this format. `_projects-python-test-dummy.py`
.This would save the file in `source/projects/python/test/dummy.py` where `source` is the directory you put the script. You can use any directory name of your choice.

Make sure to start with an `_` and seperate each directory name by `-`, the last part would be used for the filename. You can chain as many directories as you want. if a directory doesn't exist, the script automatically creates the directory.

🚨 **NOTE!!**  The script overrides the file in the new directory if it already exists

### Running on System Boot

#### Windows
1. Create a shortcut of the `parser.py` script.
2. Press `Win + R`, type `shell:startup`, and press Enter.
3. Move the shortcut to the opened folder.

#### macOS
1. Open `Automator` and create a new `Application`.
2. Add a `Run Shell Script` action with the following command:
    ```sh
    python /path/to/file_organiser.py
    ```
3. Save the application and add it to your login items in `System Preferences` > `Users & Groups` > `Login Items`.

#### Linux
1. Open a terminal and edit your crontab:
    ```sh
    crontab -e
    ```
2. Add the following line to run the script at startup:
    ```sh
    @reboot /usr/bin/python /path/to/file_organiser.py
    ```


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

