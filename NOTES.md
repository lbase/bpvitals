
## Notes for bpvitals project

Going to move some of the notes from README to here.

---

**Feb 14 2024** 
last comit:
added headers to model for show bp hide col 0
added requirements.txt

**Monday, March 11, 2024 1:16:19 PM EDT**
changed default ketone entry to 0.01

**Friday, April 5, 2024 3:32:09 PM EDT**
merged report_work into main after adding values to ketone combo boxes.
created new branch more_rep from main   Onward
also deleted tables in database that were no longer in use.


**Tuesday, May 7, 2024 10:29:49 AM EDT**
made new branch called dataclass base off of more_rep branch. Will try 
using dataclases and sqlalchemy orms classes to access database
can always go back to more_rep

**Tuesday, May 7, 2024 8:21:16 PM EDT**
merged more_rep branch to main branch then pushed main 
could probably delete more_rep branch
```
{showtabs_code.py:27 MainWindow.fillTables
    QSqlDatabase.connectionNames(): 
    [
        'dbshowqry',
        'sugcode',
    ] (list) len=2
    
showtabs_code.py:73 MainWindow.fillTables

    self.dbt.lastError().text(): '' (str) len=0
    
ic| self.model.lastError().text(): 'database is locked Unable to fetch row'

vitals_code.py:91 Main.recinsert

    self.model.submit(): True (bool)
}
```
**Thursday, May 9, 2024 5:01:19 PM EDT**
started making database table setup with sql alchemy in lcl_utils

spent a fair amount of time playin with the database to get the default value for ketone changed

