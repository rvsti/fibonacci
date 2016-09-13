# Nth fibonacci number

## Description:

This is a django that will display the Nth number in Fibonacci sequence. For instance, if N is 6 and the sequence starts with [1,1..] then it display ‘8’ as the 6th element in the sequence. It also print the time it took to get the results back to the user. 

The fibonacci number is generated with the help of matrix exponentiation algorithm.
Complexity of algorithm is O(logn).

The default timeout to generated nth fibonacci number is set to 1 sec. After that, the javascript returns a timeout out on the user side.

## Requirements:

    Django >= 1.10.*
    Python >= 2.7.*

## How to install:

Clone the repo.

    python manage.py runserver
This above command will run a light weight django server hosting at default 8000 port

Open browser and type:

    http://127.0.0.1:8000


