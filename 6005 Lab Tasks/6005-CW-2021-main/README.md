# Black Hat Books

This is the Coursework for the SEP-DEC 6005CEM 2021 instance

## Overview

Blackhat books is a e-commerce website that you need to perform a security audit on.

This is a *crystal-box* audit, and you have access to the full source code,
and an example version of the site.  You can use the site to test any security issues you find, if you wish to inclde screenshots or examples in the report.

The Site is written in [Flask](https://flask.palletsprojects.com/en/2.0.x/),  while you may not
be familiar with the framework, the code is standard Python, so you should be able to read, and follow
any of the logic in it.

## Code Overview

The Code is in the **app** Folder.

  - ```app.py``` main code for the program
  - ```mappingViews.py``` Code for viewing items
  - ```meta.py``` Application Globals and setup code
  - ```models.py``` Database models used
  
There is also 

 - ```objects.py``` Used to generate an example database for you.  You can **Ignore this** for the audit.
 
There are also some folders containing other resources

 - ```static```  Used to hold static items like CSS and JS
 - ```templates``` HTML Templates used to generate the site.
 
 
## Getting an Example Running

There is also a docker container with a development version of the site.
You will need both **docker** and **docker-compose** installed.


### Starting the Example

You can start the example with

```
$docker-compose up
[+] Running 1/0
 ⠿ Container 6005_cw_blackhatbooks-flask-1  Created                                   0.0s
Attaching to 6005_cw_blackhatbooks-flask-1
6005_cw_blackhatbooks-flask-1  |  * Serving Flask app '/opt/app' (lazy loading)
6005_cw_blackhatbooks-flask-1  |  * Environment: development
6005_cw_blackhatbooks-flask-1  |  * Debug mode: on
6005_cw_blackhatbooks-flask-1  | [2021-10-21 11:28:22,424] WARNING in _internal:  * Running on all addresses.
6005_cw_blackhatbooks-flask-1  |    WARNING: This is a development server. Do not use it in a production deployment.
6005_cw_blackhatbooks-flask-1  | [2021-10-21 11:28:22,424] INFO in _internal:  * Running on http://172.30.0.2:5000/ (Press CTRL+C to quit)
6005_cw_blackhatbooks-flask-1  | [2021-10-21 11:28:22,425] INFO in _internal:  * Restarting with stat
6005_cw_blackhatbooks-flask-1  |  * Debugger is active!
6005_cw_blackhatbooks-flask-1  |  * Debugger PIN: 917-773-677

```

The site will then be available on port 5000 at either the address given (172.30.0.2:5000 in this case)
or at localhost (http://127.0.0.1:5000)


> NOTE:
> 
> The First time this runs you will get a lot of output as the site is built.
> You can ignore the error messages about pip, these are non fatal.


### Testing Users

You also have the following users for testing 

| User                   | Password | Role  |
|------------------------|----------|-------|
| bernard@blackbooks.net | nipsy    | admin |
| manny@blackbooks.net   | lavender | user  |

### Logging and Databaase

The system will also create a copy of the logging and database in the ```tmp/``` folder.
