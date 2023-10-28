# Habit Tracker

## Table of content
- [Introduction](#Introduction)
- [Features](#Installation)
- [Installation](#Features)
- [Usage](#Usage)
- [Packages and modules](#Packages_and_modules)
- [Test suite](#Test_suite)

## Introduction

Welcome to my habit tracker.

This *habit tracker* is a project I have done as a student for the IU International University of Applied Sciences. Here you can create, delete, check, and analyse your habits. One of the hardest things when trying to establish good habit is, is having enough motivation to keep going. Thats why the habit tracker has a system set in place with whom you can track how many times in a row you have completed the habit and how much money you have saved, when for example you want to stop smoking.

## Features
With the habit tracker you are able too:

- Create new habits and define parameters:
  - Name
  - Period: daily or weekly
  - Cost 
- Delete existing habits
- Edit existing habits
- Check habits
- Analyse habits and showing them in a table:
  - Sort by:
    - All
    - Period
    - Longest current streak
    - Longest all time streak
    - Cost
    - Money saved
- Call for help if you forgot the function of the habit tracker



## Installation

1. Open your Terminal/Command window
2. Check if Python 3.8 or later is installed
    Check the current version by typing:
    
    ```
   python --version
   ```

3. Check if you have the latest pip version installed:

    Upgrade pip by typing in:

   ```
   python -m pip install --upgrade pip
   ```

4. Download the habit tracker folder and open him using your Terminal
5. Now you must install the requirements:

    Install them by typing in:
    ```
    pip3 install -r requirements.txt
    ```

## Usage

After the Installation, the program can be run by typing 

```
python3 cli.py  
```
in the terminal.

After that a menu should appear, you can then interact with the habit tracker by typing in the numbers of the functions you want to execute. The App comes with five predefined habits that are stored in the habit_data.json file.

## Packages and modules

- Datetime: Used for checking the habit off.
- Json: Saving habits in a file for later use between sessions.
- Pandas: Displaying data in tables.
- Unittest: Testing the Habit tracker.

## Tests suite



Testing is important when using the Habit tracker, it ensures that every function is running like it should be. To run a test, you must type in:

```
python3 -m pytest .
```


