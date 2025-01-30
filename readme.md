Benchmark Processor
===================

A Python script to parse .hml files containing performance metrics and generate PDF reports with time-series plots (e.g. for CPU usage, GPU usage, Framerate, etc.).

Overview
--------

This script extracts performance data from an HML file, splits it into multiple benchmarks (if the file has multiple test sections), processes timestamps, and produces PDF reports with relevant plots.

Features
--------

*   **Parsing**: Reads an .hml file line by line, looking for specific markers indicating new benchmarks, header rows, and data rows.
    
*   **DataFrame**: Organizes data into pandas DataFrames for each benchmark (test).
    
*   **Timestamp Conversion**: Converts timestamp strings to a relative time in seconds from the earliest recorded timestamp.
    
*   **Plot Generation**: Uses matplotlib and seaborn to create line plots for various metrics over time.
    
*   **PDF Reports**: Each benchmark is saved as a separate PDF file (e.g., benchmark\_1.pdf, benchmark\_2.pdf, etc.), containing charts of CPU usage, GPU usage, Framerate, RAM usage, and more.
    

Requirements
------------

*   Python 3.8+
    
*   pandas
    
*   matplotlib
    
*   seaborn
    

To install the dependencies, run:

` pip install -r requirements.txt `

(Alternatively, install the libraries individually: pip install pandas matplotlib seaborn.)

Usage
-----

1.  Place the .hml file (containing the raw benchmark data) in the same directory as the script or specify its absolute path.
    
2.  ` python run.py ` You may need to edit the script to point to your input file.
    
3.  After the script finishes, you should find one or more benchmark\_X.pdf files in the same directory. Each file corresponds to one benchmark/test in the HML data.
    

How It Works
------------

*   **Markers in the HML File**
    
    *   00, lines: Indicate the start of a new benchmark or test section.
        
    *   02, lines: Contain column headers.
        
    *   80, lines: Contain the actual measurement data for each timestamp.
        
*   **Data Extraction**
    
    *   The script collects rows for each benchmark until it encounters the next 00,.
        
    *   It then stores the resulting data in a pandas DataFrame, cleans up extra spaces, and converts timestamps to a numerical format (seconds since the earliest timestamp).
        
*   **Plotting**
    
    *   For each benchmark, the script generates line plots of chosen metrics over time (e.g., CPU usage, GPU usage, Framerate, etc.).
        
    *   It saves the plots into a PDF file (one PDF per benchmark).