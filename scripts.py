import subprocess
from getpass import getpass

from styles import colors,spinner

from rich.console import Console
console = Console()

def splash():
    '''splash screen with 4cx0-Automation \n @0x5b3a'''
    console.rule("[red b]4cx0-Automation")
    console.rule("[yellow i]@0x5b3a")




def display_installers(installers_list:list):
    '''
    Print the given list in a format like:
    [index of list].content of list
    '''
    len_installers = len(installers_list)
    for installer in range(len_installers):
        console.print(f"[{colors["neutral"]}][{installer}].{installers_list[installer]}")





def detect_package_manager():
    """Detects the package manager used by the Linux distribution."""

    package_managers = [
        "apt-get",
        "dnf",
        "yum",
        "pacman",
        "emerge",
        "pkg",
        "apk",
        "swupd",
        "eopkg"
        
    ]

    for manager in package_managers:
        try:
            subprocess.check_output(["which", manager], stderr=subprocess.STDOUT)
            return manager
        except subprocess.CalledProcessError:
            pass

    return None





def app_installation(installer,apps:list,installer_options:str,root:bool,root_options="-S"):
    '''
    start installation with the given insaller and insall given apps
    '''
    if root == True:
        console.print(f"[{colors["warn"]}]Require Sudo password:",end="")
        password = getpass(" ")
        for app in apps:
            command = f"sudo {root_options} {installer} {installer_options} install {app}"
            try:
                with console.status(f"[{colors["neutral"]}]Installing... {app}",spinner=spinner["style"]):
                    subprocess.run(command,input=password.encode('utf-8'),shell=True,check=True)
                    console.print(f"[{colors["success"]}]{app} installed Successfully.")
            except subprocess.CalledProcessError:
                console.print(f"[{colors["error"]}]Failed to install {app}")
    else:
        for app in apps:
            command = f"{installer} {installer_options} install {app}"
            try:
                subprocess.run(command,shell=True,check=True)
                console.print(f"[{colors["success"]}]{app} installed successfully.")
            except subprocess.CalledProcessError:
                console.print(f"[{colors["error"]}]Failed to install {app}")