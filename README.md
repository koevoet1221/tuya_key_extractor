# Purpose
Extract local keys from tuya smartlife app dump.
[This](https://github.com/MarkWattTech/TuyaKeyExtractor/tree/main) project has the same purpose but is Windows only. This version runs where you can install python3.
# Usage 
Either run this in the same folder as your preferences_global xml file or give the path to the file whyn prompted.
```bash
python3 extract.py
```
# Obtaining the XML
Install waydroid, install smartlife version 3.6.1 in waydroid. Open the app, log in with the smartlife account that has the devices linked. 
As root move to the following folder, where $HOME is the home folder of your user account, not the root account.
```
$HOME/.local/share/waydroid/data/data/com.tuya.smartlife/shared_prefs
```
The preferences_global_key file with a bunch of numbers at is the file containing the keys.
