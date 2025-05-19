#  Linux

1. Create a virtual environment
    ```
    python -m venv .myenv
    ```

2. Activate the virtual environment
    ```
    source .myenv/bin/activate
    ```

3. Install something into the virtual environment from outside by using pip
    ```
    /.myenv/bin/python -m pip install pyperclip
    ```

4. Install dependencies from requirements.txt from inside the virtual environment
    ```
    pip install -r requirements.txt
    ```

5. Deactivate the virtual environment
    ```
    deactivate
    ```

6. Delete the virtual environment
    ```
    rm -rf .myenv
    ```

7. Run the script
    ```
    python main.py
    ```

8. Package the app
    8.1 Without icon
        ```
        pyinstaller --onefile main.py
        ```
        This will create a dist folder with the executable file inside it.


