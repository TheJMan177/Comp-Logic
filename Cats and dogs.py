Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> <<print "Hello World"
SyntaxError: invalid syntax
>>> <print "Hello World"
SyntaxError: invalid syntax
>>> print"Hello World!"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print ("Hello World!")
Hello World!
>>> 
===================================================================== RESTART: Shell ====================================================================
>>> STRING_CATS = "cats."
... STRING_DOGS = "dogs."
... finalStatement = "It is raining " + STRING_CATS + " and " + STRING_DOGS
... print(finalStatement)
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> STRING_CATS = "cats."
... STRING_DOGS = "dogs."
... 
... finalStatement = "It is raining " + STRING_CATS + " and " + STRING_DOGS
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
===================================================================== RESTART: Shell ====================================================================
>>> STRING_CATS = "cats."
>>> STRING_DOGS = "dogs."
>>> finalStatement = "It is raining " + STRING_CATS + " and " + STRING_DOGS
>>> print(finalStatement)
It is raining cats. and dogs.
