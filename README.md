# BDCC-Oneclick
BDCC-Oneclick is an easy-to-use updater+installer utility for the game Broken Dreams Correctional Center (BDCC)

# Which version is right for me?
If you're on Windows, I highly recommend the -E version. Otherwise, use the -P version.
There is no real difference between -E and -P other than -E not requiring python to be installed. 

# How to use (by version type)

## '-P' (python) version 
- [Download python](https://www.python.org/downloads/) and install it (if you haven't already)
- Run ``oneclick.py`` in the folder you want to install BDCC (or where you've already installed BDCC)

## '-E' (exe) version 
- Run ``oneclick.exe`` in the folder you want to install BDCC (or where you've already installed BDCC)

After running oneclick, you can modify ``oneclick.json`` to use BDCC-NSMOD instead, by setting 'nsmod' to true.
You have to rerun oneclick if you modify ``oneclick.json`` for your changes to work.
``oneclick.json`` won't appear until after you first run oneclick. You can also create ``oneclick.json`` yourself, and paste this into it and configure it to your liking:
``{"nsmod": false, "version": 0, "force_update": false, "nsmod_installed": false}``

If ``version`` inside ``oneclick.json`` is 0, or ``oneclick.json`` is not found, oneclick will automatically re-install (or install) BDCC. 
Note that ``version`` is just the version on github without the '.' (for example, "1.0.2" -> "102" or "9.8.7" -> "987"). 

Oneclick *does not* remove or modify user data (such as mods, saves, or settings), so when you do an update or switch between NSMOD and normal BDCC, it will not reset anything.
Note that BDCC-NSMOD and BDCC use different data directories, so your mods, settings, and saves will not sync between BDCC-NSMOD and BDCC.
