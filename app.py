from flask import Flask
import os
import platform
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    user_name = os.getenv("USER", "codespace")  # Default to "codespace" if USER environment variable isn't available

    # Get server time in IST
    server_time = datetime.datetime.now().astimezone(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    # Check operating system and adjust top command accordingly
    if platform.system() == "Linux":
        top_command = "top -b -n 1"
    else:  # For macOS and others
        top_command = "top -l 1"  # `-l 1` is for a single iteration on macOS

    # Run the `top` command and capture the output
    top_output = subprocess.getoutput(top_command)

    # Prepare the response
    response = f"""
    <html>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> Debojyoti Chanda</p>
        <p><strong>User:</strong> {user_name}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <pre><strong>Top output:</strong>\n{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == '__main__':
    # Run Flask on port 5001 instead of 5000
    app.run(host='0.0.0.0', port=5001)
