# BDCC-Oneclick
BDCC-Oneclick is an easy-to-use updater+installer utility for the game Broken Dreams Correctional Center (BDCC)

# Which version is right for me?
Most users who use Windows will probably only ever need the -E version. 
The -P version provides the exact same functionality

# How to use (by version type)

## '-P' (python) version 
- [Download python](https://www.python.org/downloads/) and install it (if you haven't already)
- Run ``oneclick.py`` in the folder you want to install BDCC (or where you've already installed BDCC)

## '-E' (exe) version 
- Run ``oneclick.exe`` in the folder you want to install BDCC (or where you've already installed BDCC)

## Configuration 
Note: you have to rerun oneclick if you modify ``oneclick.json`` for your changes to be applied.
``oneclick.json`` won't appear until after you first run oneclick.

After running oneclick, you can modify ``oneclick.json`` to use BDCC-NSMOD instead, by setting 'nsmod' to true.
You can also change the platform you'd like to use by changing 'platform' (Not 'installed_plat') in ``oneclick.json`` to the platform desired.
 

## Notes
Oneclick *does not* remove or modify user data (such as mods, saves, or settings), so when you do an update or switch between NSMOD and normal BDCC, it will not reset anything.
BDCC-NSMOD and BDCC use different data directories, so your mods, settings, and saves will not sync between BDCC-NSMOD and BDCC.


This utility has been well tested and has worked without errors under multiple circumstances.

## Known issues
There are no known issues at this time. If there is one, I'll put it here until I fix it
