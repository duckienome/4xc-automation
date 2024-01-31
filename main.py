from lib import *
from scripts import *
from styles import *

#------Begin Installation----#

#---show splash----# 
splash()


#--- detects system package installer ---#
system_package_manager = detect_package_manager()

#--- Installers ----#
installers = ["abort","system_installer","flatpak"]


#--- display installers ---#
display_installers(installers_list=installers)

#--- Ask user to choose which installer should be used for installing apps ---#
user_installer = get_int(f"[{colors["input"]}] Choose any[*]: ")

#TODO add description till line 36
while True:
    if user_installer == 0:
        console.print(abort_msg)
        exit(1)
    try:
        console.print(f"[{colors["success"]}]  Continuing with [{user_installer}].{installers[user_installer]}...\n")
        user_installer = installers[user_installer]
        break
    except IndexError:
        console.print(f"[{colors["warn"]}]Input out of Range.")
        user_installer = get_int(f"[{colors["input"]}] Choose any[*]: ")


#---  ask user for app list that is file ---#

#--- Print warning
console.print(f"[{colors["warn"]}]\tMake sure to provide correct apps file\n\tIf not specified correctly, [{colors["error"]} u i]wrong apps[/] will be dowlaoded or [/][{colors["error"]} i u]script will break\n")

# get file
app_file = get_file("Specify file(use full path if neccessary): ")
while True:
    if len(app_file)==0:
        console.print(f"[{colors["error"]}]File is empty...")
        app_file = get_file("Specify file(use full path if neccessary):")
    else:
        break

if user_installer != "flatpak":
    app_installation(system_package_manager,app_file,installer_options="-y -q",root=True)
else:
    app_installation("flatpak",app_file,installer_options="--assumeyes --noninteractive",root=False)