README.md

# Log Rotation Python Script

This is an example programming task in Python.

## Table of Contents

- [Background](#background)
- [Sources](#sources)
- [Install](#install)
- [Usage](#usage)

## Background

### Project prompt:

Write a log rotation script in the language of your choice. For every command-line argument, it should find files whose names match the argument, 
with an optional single-digit numerical suffix (e.g. ".0"). Continue on to the next argument if there is no un-suffixed ('current') file. 
Suffixed files should each be renumbered to be one higher; the current file should then be given a .0 suffix, and a new current file 
should be created with the same file ownership and mode as the previous current file.  
Ensure that two instances of the program never accidentally process the same logfile at the same time.

Example before:
```
access_log

access_log.0

access_log.1
```

After:

```
access_log (new file)

access_log.0

access_log.1

access_log.2
```

## Sources
- This readme is based on this [README standard](https://github.com/RichardLitt/standard-readme).

## Install

This section will talk about what dependencies will be necesssary before using the code. 

```
```

## Usage

This section will talk about the relevance of log rotation and provide explainations of the code and where it would be useful.

```
```
