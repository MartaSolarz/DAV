# Exploring global temperatures since 1750 (part 1)

## Exercise 4

During this exercise we will plot some data about the temperatures. 
We will move from the simplest to more complicated plots.


The data: https://www.mimuw.edu.pl/~lukaskoz/teaching/dav/labs/lab4/temperature.csv


### Task 1: Data cleaning and preparing for plotting

a) there are missing values for City and Country in some records, remove those

b) there are NA's in AverageTemperatureFahr and AverageTemperatureUncertaintyFahr, 
remove rows with missing values in those fields

c) remove empty 'City' and 'Country' fields

d) 'day' field has no other values besides 1, thus you can remove it from the data

e) convert AverageTemperatureFahr and AverageTemperatureUncertaintyFahr into 
AverageTemperatureCelsius and AverageTemperatureUncertaintyCelsius 
(you can drop '*Fahr' columns)

f) save new csv file with cleaned data (e.g. temperatures_clean.csv)



### Task 2: Scatter plot
a) first plot all AverageTemperatureCelsius vs. year
The result should look like:
https://www.mimuw.edu.pl/~lukaskoz/teaching/dav/labs/lab4/fig1.png

Summary: the plot is quite unreadable (we used to big 'circles' for data point)

b) recreate the plot using 'points' instead 'circles', add grid
The result should look like:
https://www.mimuw.edu.pl/~lukaskoz/teaching/dav/labs/lab4/fig2.png

Summary: better, but still not very informative

c) add transparency
The result should look like:
https://www.mimuw.edu.pl/~lukaskoz/teaching/dav/labs/lab4/fig3.png

Summary: you start to see anything

d) add color
The result should look like:
https://www.mimuw.edu.pl/~lukaskoz/teaching/dav/labs/lab4/fig4.png

Summary: this did not help to much, we move to another plot type and look more deeply 


### Task 3: Box plots
a) visualising the distribution of temperatures within each country

The result should look like:
https://www.mimuw.edu.pl/~lukaskoz/teaching/dav/labs/lab4/fig5.png

Summary: we start to see some interesting facts

b) add jitter to boxplot

You will need to play with the parameters e.g. transparency
https://stackoverflow.com/questions/29779079/adding-a-scatter-of-points-to-a-boxplot-using-matplotlib

The result should look like:
https://www.mimuw.edu.pl/~lukaskoz/teaching/dav/labs/lab4/fig6.png

c) change boxplot to violin plot (sometimes known as a beanplot)
Boxplots are useful summaries, but they hide the shape of the distribution. 
For instance, if there is a bimodal distribution, this would not be observed
with a boxplot. An alternative is a violin plot, where the shape 
(of the density of points) is drawn.

After the exercise you should have:
- temperatures_clean.csv
- 7 python scripts
- (at least) 7 plots in png files produced by python scripts

Note: you need to use python, but you do not need limit yourself to matplotlib

# Exploring global temperatures since 1750 (part 2)

The continuation of temperature plots. Thus you should already have 
the dataset, scripts and plots from Tasks 1-3

The data: ../lab4/temperatures.csv

## Task 4: Time series
a) calculate average temperature per year per each country 
- in this part, you need to group data by year and country 
- then calculate mean for each group
- do line plot with years on x axis and temperature on y axis

The result should look like: fig7.png

Summary: the plot is quite unreadable

b) to avoid too much of information split graphed data by Country

The result should look like: fig8.png

Summary: better

c) and add color

The result should look like: fig9.png

Summary: you start to see anything


## Task 5: Grouping multiple subplots
a) make one (!) plot containing multiple subplots

The result should look like: fig10.png


b) split line in each subplot by city of each country

The result should look like: fig11.png

c) clean background 

Frequently, plotting libraries by default adds a grey grid. While
it may look nice at first glance, but, for print and better 
clarity, it is wise to reverse the grid coloring

The result should look like: fig12.png


d) divide into cities

As we gain some space by dividing the data into subplots, we can
use it to show more data. For each subplot/country add lines for 
individual data. You can have one legend or multiple legends 
(separate for each subplot). Mark the cities in different colors.

The result should look like: fig13.png

e) change labels, add title, customize fonts, rotate elements, etc.

The result should look like: fig14.png, fig15.png

Note: you need to use python, but you do not need limit yourself to 
matplotlib (seabonr is nice alternative plotting library)


## Homework (the raport will be partly done in labs next week):

Prepare the homework as a project directory with lab4 & lab5 exercises. 

It should contain:
- the main report file in PDF (with all the plots embedded)* 
- the python scripts generating plots (one script per one plot)**
- the separate plots as image files

*  no python code in the report file
** plain python plots (*.py)- thus no jupyter notebooks

For instance: task2a.py, task2b.py, ...
Additionally, the script should one parameter [0/1] for showing or saving the plot.
For instance typing in the terminal: 
python task2a.py 0      [will show the plot in interactive mode, plt.show()]
python task2a.py 1      [will store the plot in the file and print the path to the file]

Requred scripts/plots: 
task2a, task2b, task2c, task2d, 
task3a, task3b, task3c,
task4a, task4b, task4c,
task5a, task5b, task5c, task5d, task5e (one final plot)

As you can see there will be (at least) 15 scripts and 15 plots. Many scripts will 
share code, thus it might be worth moving some redundant code to separate *.py 
module (e.g. utils.py).

As usual, organise the project directory into subdirectories
e.g. ./images ./scripts ./data, etc.

All files should be sent until 07.04.2024 (!) via Email
'DAV24_lab5_hw_Surname_Name.7z' (ASCII letters only) attachment.

Using non-English labels, legends, descriptions, etc. will be scored -10%

Additionally, all problems with the structure of the plot e.g. the plot size,  
labels font size, etc. will also affect the grading. You need to follow advice 
included in the lectures or/and learned during the exercises.
