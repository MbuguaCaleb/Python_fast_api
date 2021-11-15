**Why Virtual Environments**

```
(a)It is an isolated environment that will not affect any other environment.

(b)In this virtual environement we can install any python packages that we want
   completely isolated to the specific project.


N/B

This threfore means that our projects will not step into each others toes

It is very important to select the python interpreter path.


Creating Virtual Environment

(a)Unix System- python3 -m venv <name>

(b)Windows System- py -3 -m venv <name>


Activating My Virtual Environment

(a)Unix System - source venv/bin/activate

(b) Windows System - venv\Scripts\activate.bat

Always ensure that your virtual environment has been selected at the interpreter level
and is active at the commandline level.

```

**Installing Fast API**

```
pip install fastapi[all]

Will install the Fast API together with all its depeendencies

Running APP

uvicorn main:app

main--name of file
app-name of fast api instance

```

**Notes By**

```
Mbugua Caleb

```
