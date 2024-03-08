# Animated plots part 2

We use again the same file from the World Bank:
https://data.worldbank.org/indicator/SP.POP.TOTL?end=2021&start=1960&view=chart

In the previous labaratory, we already selected the data for:
a) 5 most populated countries
b) 5 randomly picked 
c) 5 with Poland* as the centroid

*you can use a different country (your homeland; if applicable)

IMPORTANT: For animation plots use as much as possible "matplotlib.animation"
https://matplotlib.org/stable/api/animation_api.html

Remember, we use English. All text used in the plots should be in English.

### I) Playing with colors and labels:
For all plots from exercise 2 (a-c) do bar plots:
a) color version (most likely you already have a good starting point)
b) black & white version

Requirements:
- on top of each bar put three letters "Country Code" e.g. CHN for China
- "Country Code" position is updated with respect to the bar size
- for the black-and-white version use shapes and/or textures to indicate the classification
- the axis indicating the population should be fixed 
  (the bar should show the increase, not the leadership)
- there is a year counter inside of the plot (make it big enough)
- the font for all elements should be visible (from a large distance)
- increase the readiness of the plot as much as possible 
(e.g. do not use 150.000.000, 150e6 on the scale; 150M is much shorter and easy to read)

Expected result: 6 animated bar plots (gif; 3 b&w and 3 colors)


### II) Play with a different representation of the data:

All of the plots so far had been "bar plots". Now, the task is to present 
the data using different plot representations. For each a-c from the previous lab do similar
 animated plots, but as:
A) line plot (so the plots start as a dot and the line moves while time progress)
B) bubble plot (x is time, y is the population, z (bubble) is a population density) 
C) any other representation

- find the data about the area related to the countries of interest and calculate 
population density (population/area).

Requirements:
- on top of each bar, line or bubble put a three-letter "Country Code" e.g. CHN for China
- "Country Code" position is updated with the respect to the line or bubble location
- there is a year counter inside of the plot (make it big enough)
- the font for all elements should be visible (from a large distance)

Expected result: three animated, color plots (gif) with line plots, three bubble plots,
and three more plots (other)


## Homework:

The report regarding whole point 2 (already started in the previous week) should be made
in HTML. 

The project folder should include:

1) raport.html,
2) the data (cleaned version), 
3) the plots*,
4) the python scripts.

* There should be 15 plots in total:
a) two plots for 5 most populated countries (b&w and color version)
b) two plots for 5 randomly picked (b&w and color version)
c) two plots for 5 with Poland as the centroid (b&w and color version)

A) three animated, color plots (gif) with line plots (rendered from a-c data)
B) three bubble plots (rendered from a-c data)
C) three other plots (rendered from a-c data) 

Remember, all plots should be good quality, and contain labels for axes, legends, 
titles, proper font size, etc.

All files should be sent until Sunday 10.03.2024 via email to lukaskoz@mimuw.edu.pl 
with the email subject: 'DAV24_lab2_hw_Surname_Name' without the email text body 
and with 'DAV24_lab2_hw_Surname_Name.7z' (without Polish letters) attachment.
