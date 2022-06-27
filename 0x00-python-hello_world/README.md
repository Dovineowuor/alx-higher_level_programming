### ALX-HOLBERTON SCHOOL PYTHON PROJECT
**0x00. Python - Hello, World**

Read or watch:
01. [The Python tutorial(only the first three chapters below)](https://docs.
python.org/3/tutorial/index.html0<br>

2. [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)<br>
3. [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)<br>
4. [An Informal Introduction to Python (Read up until “3.1.2. Strings” included)](https://[docs.python.org/3/tutorial/introduction.html)<br>
5. [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)<br>
6. [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)<br>
7. [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)<br>
8. [The Python Guru](https://thepythonguru.com/)<br>
9. [New string formatting](https://pyformat.info/)<br>
10.  [Garbage collector](https://thp.io/2012/python-gc/python_gc_final_2012-01-22.pdf)<br>
11. [Python Interpreter](http://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html)<br>

***Learning Objectives***
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
       
        Why Python programming is awesome
        Who created Python
        Who is Guido van Rossum
        Where does the name ‘Python’ come from
        What is the Zen of Python
        How to use the Python interpreter
        How to print text and variables using print
        How to use strings
        What are indexing and slicing in Python
        What is the official Python coding style and how to check your code with pycodestyle
        Requirements
        Python Scripts
        Allowed editors: vi, vim, emacs
        All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
        All your files should end with a new line
        The first line of all your files should be exactly #!/usr/bin/python3
        A README.md file at the root of the repo, containing a description of the repository
        A README.md file, at the root of the folder of this project, is mandatory
        Your code should use the pycodestyle (version 2.7.*)
        All your files must be executable
        The length of your files will be tested using wc
        Shell Scripts
        Allowed editors: vi, vim, emacs
        All your scripts will be tested on Ubuntu 20.04 LTS
        All your scripts should be exactly two lines long (wc -l file should print 2)
        All your files should end with a new line
        The first line of all your files should be exactly #!/bin/bash
        All your files must be executable
        C Scripts
        Allowed editors: vi, vim, emacs
        All your files will be compiled on *Ubuntu 20.04 LTS* using **gc*c**, using the options
        *** (-Wall -Werror -Wextra -pedantic -std=gnu89)***
        All your files should end with a new line
        Your code should use the Betty style. It will be checked using ***betty-style.pl*** and ***betty-doc.pl***
        You are not allowed to use global variables
        No more than 5 functions per file
        In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
        The prototypes of all your functions should be included in your header file called lists.h
        Don’t forget to push your header file
        All your header files should be include guarded
More Info

**Zen**
        |_________________________________________________________________________________  
        |___-`______***The Zen of Python, by Tim Peters***_________________________________|
        | Beautiful is better than ugly.                                                 |
        | Explicit is better than implicit.                                              |
        | Simple is better than complex.                                                 |
        | Complex is better than complicated.                                            |
        | Flat is better than nested.                                                    |
        | Sparse is better than dense.                                                   |
        | Readability counts.                                                            |
        | Special cases aren't special enough to break the rules.                        |
        | Although practicality beats purity.                                            |
        | Errors should never pass silently.                                             | 
        | Unless explicitly silenced.                                                    |
        | In the face of ambiguity, refuse the temptation to guess.                      |
        | There should be one-- and preferably only one --obvious way to do it.          |
        | Although that way may not be obvious at first unless you're Dutch.             |
        | Now is better than never.                                                      |
        | Although never is often better than *right* now.                               |
        | If the implementation is hard to explain, it's a bad idea.                     |
        | If the implementation is easy to explain, it may be a good idea.               |
        | Namespaces are one honking great idea -- let's do more of those!               |
        |________________________________________________________________________________| Prototype
**Pycodestyle**
Pycodestyle is now the new standard of Python style code

TASKS
#**Python - Hello, World**

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Provided by Holberton School.

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                       | Prototype                             |
| -------------------------- | ------------------------------------- |
| `10-check_cycle.c`         | `int check_cycle(listint_t *list);`   |
| `102-magic_calculation.py` | `def magic_calculation(a, b):`        |

## Tasks :page_with_curl:

* **0. Run Python File**
  * [0-run](./0-run): Bash script that runs a Python script file saved
  in the environment variable `$PYFILE`.

* **1. Run inline**
  * [1-run_inline](./1-run_inline): Bash script that runs Python code saved in the
  environment variable `$PYCODE`.

* **2. Hello, print**
  * [2-print.py](./2-print.py): Python script that prints exactly `"Programming is
  like building a multilingual puzzle`, followed by a new line using the function `print`.

* **3. Print integer**
  * [3-print_number.py](./3-print_number.py): Python script that prints the integer stored
  in the variable `number`, followed by `Battery street`, followed by a new line.
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py).

* **4. Print float**
  * [4-print_float.py](./4-print_float.py): Python script that prints the float stored
  in the variable `number` with a precision of two digits.
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py).

* **5. Print string**
  * [5-print_string.py](./5-print_string.py): Python script that prints a string stored
  in the variable `str` three times, then a new line, then the first nine characters
  contained in `str`, followed by another new line.
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py).

* **6. Play with strings**++++++
  * [6-concat.py](./6-concat.py): Python script that prints `Welcome to Holberton
  School!` using the variables `str1 = "Holberton"` and `str2 = "School"`.
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py).

* **7. Copy - Cut - Paste**
  * [7-edges.py](./7-edges.py): Python script that sets three string variables based
  on the string contained in the variable `word` as follows:
  * `word_first_3`: Contains the first three letters of the variable `word`.
  * `word_last_2`: Contains the last two letters of the variable `word`.
  * `middle_word`: Contains the value of the variable `word` without the first and last letters.
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py).

* **8. Create a new sentence**
  * [8-concat_edges.py](./8-concat_edges.py): Python script that prints `object-oriented
  programming with Python`, followed by a new line without creating new variables or
  string literals.
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py).

* **9. Easter Egg**
  * [9-easter_egg.py](./9-easter_egg.py): Python script that prints "The Zen of Python" by
  Tim Peters, followed by a new line.

* **10. Linked list cycle**
  * [10-check_cycle.c](./10-check_cycle.c): C function that checks if a linked list
  contains a cycle.
  * Returns `0` if there is no cycle and `1` if there is.
  * Helper files:
    * [linked_lists.c](./linked_lists.c): C functions handling linked lists for testing
    [10-check_cycle.c](./10-check_cycle.c) (provided by Holberton School).
    * [lists.h](./lists.h): Header file containing definitions and prototypes for
    all types and functions used in [linked_lists.c](./linked_lists.c) and
    [10-check_cycle.c](./10-check_cycle.c).

* **11. Hello, write**
  * [100-write.py](./100-write.py): Python script that prints exactly `and that piece of
  art is useful - Dora Korpar, 2015-10-19`, followed by a new line to `stderr` using
  the function `write` from the `sys` module.
  * Exits with a status code of `1`.

* **12. Compile**
  * [101-compile](./101-compile): Python script that compiles a Python script file stored
  in the environment variable `$PYFILE` and saves it to an output file
  `$PYFILEc` (ex. `export PYFILE=my_main.py` => output filename: `my_main.pyc`).

* **13. ByteCode -> Python #1**
  * [102-magic_calculation.py](./103-magic_calculation.py): Python function matching exactly
  a bytecode provided by Holberton School.

CREDITS:|<br>
 ____________________________________________________
|***[SOCIAL-MEDIA-HANDLES]*:**                       |
|____________________________________________________|
|[Dovine Owuor](https://github.com/dovineowuor)<br>  |
|[Linkedin](https://linkedin.com/in/dovine-owuor)<br>|
|[Twitter](https://www.twitter.com/dovine-owuor)<br> |
|[Email-Me_@:](owuordove@gmail.com)<br>              |
|____________________________________________________|


