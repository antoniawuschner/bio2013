===========
Bio2013
===========

A software project for FHS interns.


### Ideas ###

Check out cool ideas on 
[this wiki page](https://github.com/antoniawuschner/bio2013/wiki/FourierTransform-Aspects).


### Syntax ###
- %s (word) will replace %s with that word

### To make a method ###
- start with def
- parameters are the same as java
- end with a colon
- anything in the method has to be indented

Example

    def method1(parameter1):
    
To load from the terminal, reload, and call methods

    import bio2013.first as f
    reload(f)
    f.sum1(list1)
    
### Important functions ###

    dir(method, class,ect) #gives what that class can do
    help(f.list1.index) #tells what that method does
    

### Boilerplate ###

 - easy_install
 - ... shell stuff ...
 - ... etc. ...

### Markdown tips ###

Github displays markdown files in a special, neat way.  Files ending in `.md` get this magic
treatment.  

It's easy to do *italics*, **bold text**, and inline code like `y = x + 4`.

Testing

-in order for tests to run they have to start with test in the module

