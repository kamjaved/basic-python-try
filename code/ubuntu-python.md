### Solution 1: Use a Python Virtual Environment (Best Practice)

This is the **safest and most common** way to manage Python projects. A virtual environment is an isolated folder containing a specific Python interpreter and all the libraries your project needs.

#### Step-by-Step Guide:

1. **Ensure `venv` is installed**: Most Python 3 installations include `venv`. If not, you can install it:

   ```sh
   sudo apt install python3.11-venv
   ```

2. **Create a Project Directory**: Navigate to where you want your project to live and create a new folder for it.

   ```sh
   mkdir my-python-project
   cd my-python-project
   ```

3. **Create the Virtual Environment**: Inside your project folder, run the following command. This creates a directory named `venv` (a common convention) that will house your isolated Python environment.

   ```sh
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment**: To start using the environment, you must "activate" it.

   ```sh
   source venv/bin/activate
   ```

   Your terminal prompt will change to show `(venv)` at the beginning, indicating that the virtual environment is active.

5. **Install Packages with `pip`**: Now you can use `pip` to install any package you need without `sudo` and without affecting your system's Python installation.

   ```sh
   pip install requests
   pip install matplotlib
   ```

6. **Deactivate the Environment**: When you're finished working on your project, you can exit the virtual environment by simply typing:
   ```sh
   deactivate
   ```
