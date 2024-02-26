# DAV
Data analysis and visualization class - MIMUW 2023/24

## Table of Contents
- [Lab1 - 26.02.2024](#lab1)

## Lab1

Animated plots part 1

Download video from youtube:

```bash
yt-dlp -f 597 'https://www.youtube.com/watch?v=7DemM7UGmIg'
```

Convert mp4 into gif using ffmpeg and convert (ImageMagic):

```bash
ffmpeg -i video.mp4  -r 5 'frames/frame-%03d.jpg'
```
```bash
cd frames
```
```bash
convert -delay 20 -loop 0 *.jpg myimage.gif
```