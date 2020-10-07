# Data Skills 2
# Autumn 2020
#
# Homework 1
#
# Due Tuesday October 13th before midnight on GitHub classroom.  Please read the academic integrity
# section of the syllabus for guidelines on how to collaborate and cite sources, and the grading
# rubric posted on Canvas (under announcements or files).
#
# Be sure to clean up your code, removing unnecessary elements like intermediate output that were
# only used in debugging.  Write this as if it were something you were doing for your work as a
# research assistant.
#
# #################################################

# 1. The two datasets included in the assignment repo are downloaded directly from the BEA.  The file
# labeled "total" has the total employment per state for the years 2000 and 2017.  The file labeled
# "by industry" has employment per industry in each of 10 industries per state for the same years.
#
# Load and merge the data into a panel dataframe, with the columns: "state", "year", and one for each
# of the 10 industries.  Every state-year combination should uniquely identify a row.  No more and no
# less than 12 columns should remain.  Do any necessary cleaning for the data to be easily usable.
#
# The values should be given as the share of the total employment in that place and time, e.g. if
# total employment in a place and time was 100, and the employment in one industry was 10, then the
# value shown for that state-year industry should be 0.1.
#
# Output this dataframe to a csv document named "data.csv" and sync it to your homework repo with
# your code.



# 2. Using the dataset you created, answer the following questions:
#
# a. Find the states with the top five share of manufacturing employment in the year 2000, then show
# how their share of employment in manufacturing changed between 2000 and 2017.  Use a basic plot to
# display the information.
#
# b. Show which five states have the highest concentration of employment in a single industry in each
# of 2000 and 2017, and what those industries are.
