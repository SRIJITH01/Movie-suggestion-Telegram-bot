

# Movie-suggestion-Telegram-bot


# Introduction
This bot will suggest you movies based on some filters like streaming platform,language,year,rating.<br>
You can use the given code to make your own bot or you can directly use my existing bot at <a href="https://telegram.me/Suggesting_movies_bot" target="_blank">here</a>.
 
## Table of contents
* [General info](#general-info)
* [Modules](#Modules)
* [Setup](#setup)
* [Example-Gif](#Example-Gif)


## General info
You are going to need some modules mentioned below.
Tested on Ubuntu 20.04 LTS<br>
	
## Modules
Code is created with:
* Ubuntu 20.04 LTS
* Selenium version : 3.141.0
* Chromedriver version :  91.0.4472.101 (Always use same version of chromredriver as of chrome)(Better to use latest version)
* Python library version : Python 3.8.5
* numpy version : 1.19.5
 
	
## Setup
### Step 1:
To run this project, install above modules locally using pip or pip3:

```
$ pip3 install selenium
$ pip3 install numpy
$ pip3 install requests
$ pip3 install urllib3
$ apt install chromium-chromedriver
```
or you can just download the latest version of chromedriver from [Website](https://chromedriver.chromium.org/downloads)<br>

and run in terminal <br>
```
$ pip3 install -r requirements.txt
```
### Step 2:
* You need to run the Database.ipynb to download posters of images for all platforms and for some other functions.
* Next you need to create a bot and use the token in moviebot.py
* That's it. 

## Example-Gif
(1) How does it work?.<br> <br> <br>
![1623398535260](https://user-images.githubusercontent.com/54314892/122077988-db14a680-ce19-11eb-93f6-621914bc2fdf.gif)


If you need any help in creating the bot or downloading the database,create a new issue [here](https://github.com/SRIJITH01/Movie-suggestion-Telegram-bot/issues/new).

