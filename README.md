bpvitals blood pressure database using sqlite

These forms now use both databases:

[postgresql](http://flatboy/adminer/adminerstart.php?pgsql=flatboy&username=rfile&db=rfile&ns=public&select=vsigns_bp)

and sqlite:

[sqlite file](file:///data/sqlite/vitals.db)

Stashing forms and execution code in ~/python3/bpvitals/forms

For use in desktop shortcuts. Will try and keep up to date but unbroken.

Script in bpvitals called rsync_forms

Wednesday, November 24, 2021 9:04:47 PM EST
should be able to pull/clone datautil from here (flatboy) to suse and have current setup

Tuesday, March 15, 2022 11:32:11 AM EDT
Starting to use pycharm to do some cleanup on sqlsimple branch before trying to simplify sql stuff

Thursday, July 7, 2022 8:22:14 PM EDT
merged sqlsimple into master

**Friday, July 8, 2022 1:20:41 PM EDT**

had branches in this remote that I had deleted but still showed up in local (remote ref does not exist error)
Note that problem above can be resolved with a **git pull --prune**
renamed bpvitals to bpvitals.orig and did new clone under python3

use git pull --prune to get branches synced between local remote

[youtube git prune](https://youtu.be/8aV5AxJrHDg?t=6817)

 https://youtu.be/8aV5AxJrHDg

 **Sunday, July 31, 2022 5:23:33 PM EDT**

 Just merged menuedit into main. Will continue to work on meuedit and add more features.

**Monday, August 8, 2022 12:45:30 PM EDT**

branch now called edit 

moving forms into /forms subdirectory 

last merge to main:

673d5ee247507527f45c1f9b3c2abb1fb603133a

Thursday, September 8, 2022 8:32:41 PM EDT

Use **weight_lite.py for csv import**

qfatty regular table and fatty test table

**Feb 14 2024** 
last comit:
added headers to model for show bp hide col 0
added requirements.txt

**Monday, March 11, 2024 1:16:19 PM EDT**
changed default ketone entry to 0.01


