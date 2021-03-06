# Name: 	produceOutput.py
# Author: 	Denis Stukal
# Date: 	April 12, 2015
# Summary:	Defines makeOutput() that merges the data sets, creates a ExploreGraphs object, 
# 			makes a boxplot and saves it. 
########################################################################################## 


import pandas as p
from assignment8Functions.exploreGraphs import *
import assignment8Functions.assignment8Exceptions as ex

def makeOutput(data, year):
    '''
    data argument is an instance of Data class from dataModule. 
    year should be an integer between 1800 and 2012.
    '''
    try:
        # Load data using merge_by_year(year) from assignment8Functions.exploreGraph
        currentData = data.mergeByYear(year)
        # Instantiates an object of ExploreGraphs class with data and graphs as attributes
        currentGraphs = ExploreGraphs(currentData, year)
        currentGraphs.makeBoxplot()
        currentGraphs.saveBoxplot()
        currentGraphs.makeHistogram()
        currentGraphs.saveHistogram()
    except ValueError: 
        raise ex.WrongInput()


