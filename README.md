Py4J Arbitrary Python code example
==================================

Simple Java and Python programs showing how arbitrary Python programs can be executed from Java.

Requirements
------------

Tested with Java 8, Python 3, and Py4J 0.8.2.


Installation
------------

1. Install py4j 0.8.2 globally or in a virtualenv (pip install py4j).
2. Configure the Python interpreter in Eclipse.
3. Import the project py4j-arbitrary-python project in Eclipse.


How to run
----------

1. Run the main method in com.infobart.arbitrarypython.Application
2. Run the python_client.py script
3. Look at the Java console (not the Python one)


How it works
------------

The Python code implements the PythonInterpreter Java interface.
It will execute arbitrary python code given as a String and return the
first local variable it finds (note that the locals are not ordered).

The Java code calls the Python interpreter and prints the return value (of
type Object). Note that the value returned by Python is represented as an
Object and Java takes care of autoboxing if necessary.

Limitations: the python code cannot return Python objects (e.g., a native
Python list)

