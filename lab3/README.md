# Animated plots part 3

## Exercise 3

We use again the same file from the World Bank:
https://data.worldbank.org/indicator/SP.POP.TOTL?end=2021&start=1960&view=chart

In the previous exercise, we selected the data for:

a) 5 most populated countries
b) 5 randomly picked 
c) 5 with Poland as the centroid


IMPORTANT: For animation plots use as much as possible "matplotlib.animation"
https://matplotlib.org/stable/api/animation_api.html

Remember, we use English. All text used in the plots should be in English.


## III) Exploration of the data. Select a group of 4-8 countries that:
- at least one shows some strange behavior e.g. strong increase, decrease or 
stability of the population size in some particular period of time
(thus it is up to you to find those in the data)
- mark this event on the plot

For instance, you could pick one or a few countries in some war zone and few 
other outside of it (e.g. Rwanda in the 90s) and show how the population changed 
(to highlight the difference try to use neighbors or/and countries with similar 
population size). To mark the event stop/freeze (or decrease speed) 
the animation for ~4s in order to allow people to read the information 
(imagine that you are having a speech and you want to emphasize the fact) 
- thus you need to put some additional text for those ~4s in some part 
of the plot ('e.g. "WAR") explaining the observed fact. If the selected 
event is related to a given period e.g. 5 years, than you show the text
on all related years (e.g. 1992-1995).  


Expected result: 1 animated, bar plot (gif) 
Example plot: https://www.mimuw.edu.pl/~lukaskoz/teaching/dav/labs/lab3/lab3_1.gif

## IV) Generate Gantt plot from the data presented on the 3&4th pages of 
https://www.uw.edu.pl/wp-content/uploads/2024/02/m.2024.42.post_.1.pdf 
or
https://www.mimuw.edu.pl/~lukaskoz/teaching/dav/labs/lab3/m.2024.42.post_.1.pdf

More about Gantt's plot:
https://www.mimuw.edu.pl/~lukaskoz/teaching/dav/labs/lab3/Gantt_Extra_Slides.pdf

Requirements:
- the labels must be in English
- the labels should be placed inside of the bar or next to it, but
  cannot overlap
- do color and black&white version (2 plots)
- if needed, introduce abbreviations and explain them below the plot
- each plot should be presented as a separate pdf file of A4 size
(the plot should take the whole A4 page and be as much readable as
possible - think about printing it and putting it on the wall)

Expected result: 2 static, Gantt plots (2 separate single-page A4 pdf files). 

Additionally, convert the plots into images for report purposes.


## Homework:

Extend the homework from previous laboratories. 

It should contain:
- the main report file in HTML (with all the plots embedded so far) 
- the plots (both GIFs and PDFs from IV thus lab1, lab 2, and lab3 together) as separate files
- the python scripts generating plots
- the data for each plot (csv format) - each time you need to filter out relevant data

All files should be organized as the project folder and sent until 17.03.2024
via email to lukaskoz@mimuw.edu.pl with the email subject:
'DAV24_lab3_hw_Surname_Name' without email text body and with 
'DAV24_lab3_hw_Surname_Name.7z' (ASCII letters only) attachment.

(thus no 'DAV24_lab3_hw_ÅÃ³Å¼yÅ„ska_MaÅ‚gorzata', should be 'DAV24_lab3_hw_Luzynska_Malgorzata')
