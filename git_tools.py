import subprocess

def git_commit_and_push_if_needed(message="Änderungen durch Bot"):
    try:
        status = subprocess.check_output(["git", "status", "--porcelain"]).decode().strip()
        if status:
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", message], check=True)
            subprocess.run(["git", "push"], check=True)
            print("Änderungen gepusht.")
        else:
            print("Keine Änderungen zum Pushen.")
    except subprocess.CalledProcessError as e:
        print(f"Git-Fehler: {e}")
