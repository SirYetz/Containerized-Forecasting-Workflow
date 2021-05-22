# Latin Hypercube Sampling

Scripts in this directory are used to generate output from hypercube sampling. **This is not functional but serves as a skeleton as to the methodology to use**.

## Setup and Usage

1. Place this folder into the directory containing wrf.exe
2. Run the script with all the same input parameters as run_simulation.py and the additional --lhs n, where n is the number of samples desired
3. netCDF4 files from each run are placed in the 'nc' folder with file names of the format sample<n> and input parameters used are in the 'input' folder with the naming convention sample<n>.input
4. Use the plotting.py file to generate visual plots of the output generate by each sample (or incorporate direct into the run_simulation.py file)

## Theory

The script will use the input parameters alongside the variables to be altered for sampling, create an appropriate namelist.input file, run the simulation and move resulting files into respective directories for furher processing (plotting data points to visualise variance between samples)
