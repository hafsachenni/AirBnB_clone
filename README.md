# AirBnB CLONE - THE CONSOLE:

The AirBnB-clone is the first step towards building our full web appliction designed to replicate the functionality of the widely recognized AirBnB platform

## Table of contents

- [Description](#description)
- [How to start it](#How-to-start-it)
- [How to use it](#How-to-use-it)
- [Console commands](#console-commands)
- [Examples](#examples)


## DESCRIPTION:

### The console:

    - Create our data model

    - Manage (create, update, destroy, etc) objects via a console or command interpreter

    - Store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

## HOW TO START IT:

1. First clone this repository

2. Locate the "console.py" file and run it using the following command:
``` /AirBnB_clone$ ./console.py ```

3. when it is run with success, the following prompt should appear:
```(hbnb)```

4. This prompt indicates you are in the "HBNB" console.

## HOW TO USE IT:

- The shell work in interactive mode:

```
./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
```
- In the non-interactive mode:

```
echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```

## CONSOLE COMMANDS:

```
* create - Creates an instance based on a given class
* destry - Destroys an instance based on class and UUID
* show - Shows an object based on class and UUID
* all - Shows all objects on a given class
* update - Updates existing attributes
* quit - Exit the program (EOF)
```

## EXAMPLES:

- Create:
Usage: create <class name>

```
(hbnb) create BaseModel
0fb277e8-547b-4db6-a004-377809099387
(hbnb) 
```

- show:
Usage: show <class name> <_id>

```
(hbnb) show BaseModel 0fb277e8-547b-4db6-a004-377809099387
[BaseModel] (0fb277e8-547b-4db6-a004-377809099387) {'id': '0fb277e8-547b-4db6-a004-377809099387', 'created_at': datetime.datetime(2023, 12, 9, 17, 44, 53, 477707), 'updated_at': datetime.datetime(2023, 12, 9, 17, 44, 53, 495929)}
(hbnb) 
```
