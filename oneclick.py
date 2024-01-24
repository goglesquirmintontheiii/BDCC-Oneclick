#https://api.github.com/repos/Alexofp/BDCC/releases/latest - BDCC
#https://api.github.com/repos/NSWIP/BDCC-NSMOD/releases/latest - BDCC-NSMOD
#https://github.com/goglesquirmintontheiii/BDCC-Oneclick - Oneclick repository

platform = "auto"
# Change "auto" to "web" if you want to use web.
# You can also specify a different platform ("web", "mac", "linux", or "windows"), if the script incorrectly determines your OS.
# Will download the web version if it can't determine your OS.


# Please do not edit anything below unless you know python :]

import os
import subprocess
import sys
from pathlib import Path
import json

print("Thanks for using BDCC-Oneclick!")
print("You're using BDCC-Oneclick v1.1.0-P")


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import zipfile
except:
    install("zipfile")
    import zipfile
try:
    import requests
except:
    install("requests")
    import requests

from platform import system as sysn
def Version(_inp : str) -> int:
    off = 0
    inp = "".join([v for v in _inp if v in "1234567890.-"])

    if len(inp) != len(_inp):
        buf = ""
        _ok = True
        for v in _inp:
            if _ok:
                if v not in "1234567890.-":
                    _ok = False
            else:
                if v in "1234567890":
                    buf += v
        try:
            off=int(buf)
        except:
            off = 0
    spl = inp.split('-')[0].split('.')
    spl = [int(spl[0]),int(spl[1]),int(spl[2])+off]
    return (spl[0]*100)+(spl[1]*10)+spl[2]



if platform == 'auto':
    pn = sysn()
    if pn == "Windows":
        pn = "windows"
    elif pn == "Darwin":
        pn = "mac"
    elif pn == "Linux":
        pn = "linux"
    else:
        pn = 'web'
else:
    pn = platform

sep = os.path.sep
cwd = sep.join(__file__.split(sep)[:-1])
ver_path = os.path.join(cwd,'oneclick.json')
assets = ['BDCC.exe', 'BDCC.pck', 'BDCC.x86_64', 'index.apple-touch-icon.png',
          'index.audio.worklet.js', 'index.html', 'index.icon.png',
          'index.js','index.pck','index.png','index.wasm','BDCC.zip',
          'BDCC-NSMOD.pck', 'BDCC-NSMOD.exe', 'BDCC-NSMOD.x86_64']

det = {}

if not os.path.exists(ver_path):
    try:
        print("WARNING: oneclick.json not found, game will be updated / reinstalled regardless of current version.")
        ver = 0
        with open(ver_path,'w') as f:
            f.write(json.dumps({'nsmod': False, 'version': 0, 'force_update': False, 'nsmod_installed': False}))
        det = {'nsmod': False, 'version': 0, 'force_update': False, 'nsmod_installed': False}
    except:
        print("ERROR: Couldn't create oneclick.json. Installing BDCC anyways..")
else:
    with open(ver_path,'r') as f:
        det = json.loads(f.read())
        ver = det['version']

url = "https://api.github.com/repos/Alexofp/BDCC/releases/latest"
if det['nsmod']:
    url = "https://api.github.com/repos/NSWIP/BDCC-NSMOD/releases/latest"

info = requests.get(url).json()
new_ver = Version(info['tag_name'])
print(f"\nInstalled: v{ver}")
print(f"Latest: v{new_ver}")
print(f"BDCC platform: {platform}")
print(f"NSMOD: {['No', 'Yes'][int(det['nsmod'])]}")
print(f"Force update: {['No', 'Yes'][int(det['force_update'])]}\n")
bdccv = {"linux": "BDCC-NSMOD-Linux-x86_64.zip", "windows": "BDCC-NSMOD-Win-x86_64.zip"}
if det['nsmod']:
    if pn in bdccv.keys():
        NSname = bdccv[pn]
    else:
        print("WARNING: BDCC-NSMOD does not support your platform. Defaulting to regular BDCC..")
        det['nsmod'] = False
        info = requests.get("https://api.github.com/repos/Alexofp/BDCC/releases/latest").json()
if new_ver > ver or det['force_update'] or det['nsmod'] != det['nsmod_installed']:
    if det['force_update']:
        print("Forcing an update..")
    else:
        if det['nsmod'] != det['nsmod_installed']:
            if det['nsmod']:
                print("-- Switching to BDCC-NSMOD --")
            else:
                print("-- Switching to regular BDCC --")
        else:
            if ver == 0:
                print(f"-- Installing {['BDCC','BDCC-NSMOD'][int(det['nsmod'])]} --")
            else:
                print(f"-- Upgrading from v{ver} to v{new_ver} --")
    print("Fetching latest binaries..")
    latest = os.path.join(cwd,'latest.zip')
    with open(latest, 'wb') as f:
        for i in info['assets']:
            if det['nsmod']:
                if i['name'] == NSname:
                    f.write(requests.get(i['browser_download_url']).content)
                    break
            else:
                if i['name'] == f"bdcc-{pn}.zip":
                    f.write(requests.get(i['browser_download_url']).content)
                    break

    print("Removing old version..")
    fls = os.listdir(cwd)
    for i in fls:
        pth = os.path.join(cwd,i)
        if (i in assets) and os.path.isfile(pth):
            os.remove(pth)
    print("Unpacking latest version..")
    with zipfile.ZipFile(latest, 'r') as zip_ref:
        # Extract all the contents into the specified directory
        zip_ref.extractall(cwd)
    if det['nsmod']:
        if pn == "windows":
            src_path = Path(cwd).joinpath('Win')
            # ^ the same as /tmp/files_to_move
            #   OR //tmp//files_to_move if on windows.

            for each_file in src_path.glob('*.*'):  # grabs all files
                trg_path = src_path.parent  # gets the parent of the folder
                each_file.rename(trg_path.joinpath(each_file.name))  # moves to parent folder.
            os.rmdir(os.path.join(cwd, "Win"))
        elif pn == "linux":
            src_path = Path(cwd).joinpath('Linux')
            # ^ the same as /tmp/files_to_move
            #   OR //tmp//files_to_move if on windows.

            for each_file in src_path.glob('*.*'):  # grabs all files
                trg_path = src_path.parent  # gets the parent of the folder
                each_file.rename(trg_path.joinpath(each_file.name))  # moves to parent folder.
            os.rmdir(os.path.join(cwd, "Linux"))
    print("Removing installation files..")
    os.remove(latest)
    print("Finishing up..")
    det['version'] = new_ver
    det['nsmod_installed'] = det['nsmod']
    with open(ver_path,'w') as f:
        f.write(json.dumps(det))
    print("Installation finished succesfully!")
else:
    print(f"Your current version (v{ver}) is up-to-date!")
input("\nIf you like BDCC-Oneclick and would like more features and updates, feel free to star it on Github! \nIf you have any suggestions, feel free to DM me on Discord any time! \n\nPress enter or ctrl+c to exit..")
