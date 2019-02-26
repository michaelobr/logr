# logr
Python module that logs events during the development life cycle to help with testing.


### Functions

```
init_log(log_name, log_folder_dir=default)
```
Creates a directory named /logs (if it doesn't exist already) and creates a log with the name of log_name at the specific directory. If no log_folder_dir variable is passed, /logs directory will default to the local directory. 

```
log_event(log_name, event_name, message, status, directory="default")
```
Records an event in the specified log of log_name with the time stamp of execution. 

```
analyze_log(log_name, directory="default")
```
This function is currently under development. It reads logs into panda dataframes. More features will be available in the future.
