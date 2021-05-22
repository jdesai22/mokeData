# MOKE Data Analysis

### Run without Python (as .exe)
1. Extract
   1. [build](./build)
   2. [dist](./dist)
   3. [mokeMain.spec](./mokeMain.spec)
2. Move Into Correct directory and Run
   1. cd [dist\mokeMain](dist/mokeMain)

### Info Required
* path to file
    * file type .lvm
* scans from 0 to maxvoltage
* total loops

### Data Analysis Included
* plots scatterplot of all data points
* plots scatter plot of average
* denoises data with moving average
    * done with [Savitzy-Golay filter](http://www.statistics4u.com/fundstat_eng/cc_filter_savgolay.html) in scipy package
    
     