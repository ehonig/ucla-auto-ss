import keyring
from cryptography.fernet import Fernet

def setupAutoSS():
    print("This is the setup script for `auto_symptom_survey.py`.\nIt is assumed that the default values of the inputs for `auto_survey()` are as follows:\n\nfernet_key = 'your fernet key'\nuser_key = 'your user key'\nsystem = 'your system'\n")
    loopBool = True
    while loopBool:
        Fkey = Fernet.generate_key()
        print(f"Generated Fkey: {Fkey}")
        cond = input("To generate new key, press enter after typing something.\nTo continue with current key, press enter without typing.\n")
        if cond == "":
            loopBool = False
            print("This string will be saved as the default value of `fernet_key`")

    loopBool = True
    f = Fernet(Fkey)
    while loopBool:
        system = input("Choose a name for the system variable of keyring -- this can be any string\n")
        print(f"You entered: {system}")
        cond = input("To re-enter the system variable, press enter after typing something.\nTo continue with current system variable, press enter without typing.\n")
        if cond == "":
            loopBool = False
            print("This string will be saved as the default value of `system`")

    loopBool = True
    while loopBool:
        user_key = input("Choose a name for the user key for accessing your encrypted UCLA username -- this can be any string\n")
        print(f"You entered: {user_key}")
        cond = input("To re-enter the user_key variable, press enter after typing something.\nTo continue with current user_key variable, press enter without typing.\n")
        if cond == "":
            loopBool = False
            print("This string will be saved as the default value of `user_key`")

    loopBool = True
    while loopBool:
        usr = input("Input your UCLA login username. Check if anyone is looking, as it will be visible\n")
        # cond = input("To print the string you just input, press enter after typing something\n")
        # if cond != "":
        #     print(f"You entered: {usr}")
        cond = input("To re-enter your UCLA login username, press enter after typing something.\nTo continue with current input, press enter without typing.\n")
        if cond == "":
            loopBool = False
            print("This string will be encrypted in your system's credential manager using the `system` and `user_key` variables")

    loopBool = True
    while loopBool:
        pwd = input("Input your UCLA login password. Check if anyone is looking, as it will be visible\n")
        # cond = input("To print the string you just input, press enter after typing something\n")
        # if cond != "":
        #     print(f"You entered: {pwd}")
        cond = input("To re-enter your UCLA login password, press enter after typing something.\nTo continnue with current input, press enter without typing.\n")
        if cond == "":
            loopBool = False
            print("This string will be encrypted in your system's credential manager using the `system` variable and your unencrypted UCLA login username")

    keyring.set_password(system, user_key, f.encrypt(usr.encode()))
    keyring.set_password(system, usr, f.encrypt(pwd.encode()))

    filename = 'auto_symptom_survey.py'
    text = open(filename).read()
    text = text.replace('your fernet key', Fkey)
    text = text.replace('your user key', user_key)
    text = text.replace('your system', system)
    open(filename, "w").write(text)
    # print("`fernet_key` default value replaced")
    #
    # print("`user_key` default value replaced")
    #
    # print("`system` default value replaced")
    #
    # print("`UCLA login username encrypted`")
    #
    # print("`UCLA login password encrypted`")

    print("Setup finished: default values in `auto_survey()` replaced and login info encrypted.\n\n\
If you have already downloaded `chromedriver.exe`, then run `python auto_symptom_survey.py` in a shell to see if it worked.\n\n\
Make sure the shell is opened in the same folder that contains `chromedriver.exe` and `auto_symptom_survey.py`.")


if __name__ == "__main__":
    setupAutoSS()
