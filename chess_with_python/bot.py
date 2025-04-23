import os
import time
import schedule
from git import Repo

# Path to your code directory (the folder you want to monitor)
CODE_DIR = "C:\Users\abrah\Desktop\chess_with_python\chess_pieces"
# Path to your log repository
LOG_REPO_DIR = '/path/to/your/log/repo'

def resume_code():
    # Logic to resume your code
    print("Resuming code...")  # Replace with actual code execution logic

    # Log the activity
    log_activity()

def log_activity():
    # Initialize a summary of changes
    changes_summary = ""

    # Use git to get the changes made in the last 30 minutes
    try:
        repo = Repo(CODE_DIR)
        # Get the list of changed files in the last 30 minutes
        changed_files = repo.git.diff('--name-only', '--since="30 minutes ago"').splitlines()
        
        if changed_files:
            changes_summary += "Changes made in the last 30 minutes:\n"
            for file in changed_files:
                changes_summary += f"- {file}\n"
        else:
            changes_summary = "No changes made in the last 30 minutes.\n"

    except Exception as e:
        changes_summary = f"Error retrieving changes: {e}\n"

    # Create a log entry with a short message and the changes summary
    log_entry = f"Code resumed at {time.strftime('%Y-%m-%d %H:%M:%S')} - {changes_summary}\n"
    
    # Write the log entry to a file
    log_file_path = os.path.join(LOG_REPO_DIR, 'activity_log.txt')
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_entry)

    # Commit and push the log to GitHub
    try:
        repo.index.add([log_file_path])
        repo.index.commit("Log activity: Code resumed with changes summary")
        origin = repo.remote(name='origin')
        origin.push()
        print("Log pushed to GitHub.")
    except Exception as e:
        print(f"Error pushing to GitHub: {e}")

# Schedule the resume_code function to run every 30 minutes
schedule.every(30).minutes.do(resume_code)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)