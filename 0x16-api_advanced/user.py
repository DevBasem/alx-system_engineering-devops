import platform

def get_user_agent():
    system_info = platform.system() + ' ' + platform.release()
    python_info = 'Python/' + platform.python_version()
    user_agent = 'Mozilla/5.0 (' + system_info + ') ' + python_info
    return user_agent

if __name__ == "__main__":
    print("Your user agent is:", get_user_agent())
