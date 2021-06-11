Change directories in run_lhs.py and tsPlotting.py to appropriate/desired local directories
Set total number of run in run_lhs.py
line 509: runs = x where x is the number of runs you wish to conduct
~/student/run/LHS/python3 run_lhs.py
This will generate x amount of TS files and x namelist input files named trit_x and sample_x respectively 
The TS file will contain that time series data generated from the run
The namelist input file will contain the WRF input parameters used to generate that data
Namelist found in: ~/student/run/LHS/inputs
TS file found in: ~/student/run/LHS/tsout

There is no automated means of extracting observed data from CSV file
Data from required run duration must be copied into text file and saved as clientdata.txt

In tsPlotting.py line 12: set to length of WRF run time in hours
This is required to ensure plotting
~/student/run/LHS/python3 tsPlotting.py
This script plots that data 

If you wish to use/improve on the ML side of house
find in the zip folder XG Test.py

This will require significant modification to run correctly and as desired, primarily the changing of directories to where you store .TS files
xgboost is a required library, so if not previously installed, it will need to be

The script for the UI that was designed for the docker is uploaded on github filename wrfgui.py
the script for the UI that runs on bare machine is located in /student/run/LHS/wrfgui.py
