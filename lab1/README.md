# Animated plots part 1 

## 1) Scrap some youtube video with plots e.g. https://www.youtube.com/watch?v=7DemM7UGmIg and convert it into animated gif.

Hints: 
- use web browser plugins, youtube-dl or similar tools

Prefered setup:

https://github.com/yt-dlp/yt-dlp

https://pypi.org/project/yt-dlp/

Inspect formats with option -F & dowload rather smaller than bigger (-f option)

Install yt-dlp using venv:

a) https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

b) https://docs.python.org/3/tutorial/venv.html

- convert mp4 into gif using ffpmeg and convert (ImageMagic)
- https://askubuntu.com/questions/648603/how-to-create-an-animated-gif-from-mp4-video-via-command-line

```
ffmpeg -i video.mp4  -r 5 'frames/frame-%03d.jpg'
cd frames
convert -delay 20 -loop 0 *.jpg myimage.gif
```
As you learned how to make animated gif by joining the image files ('convert' command 
from ImageMagic), now it is time for PYTHON scripting and do some serious plotting. 

## 2) Given the data from The Word Bank: https://data.worldbank.org/indicator/SP.POP.TOTL?end=2021&start=1960&view=chart do animated bar plots (gif file) for all years for:

a) 5 most populated countries (filter out groups like South Asia, OECD, etc.)

b) pick one country and year at random and then find 4 other countries that are the closest by 
population size (either + or -) in given year and do similar plot (e.g., Chile at 1985 and 4 other countries)

c) the same as (b) but this time use Poland as "the centroid"
