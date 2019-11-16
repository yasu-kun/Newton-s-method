# Newton's-method
This code implements Newton's method in Python.
You can approximately find x where f(x) = 0.

*** Note that the function f(x) of the value to be calculated must be a convex function, and its error handling is not implemented.  

*** This code is just a practice code.  

*** The Newton method of this code only supports one dimension, not multiple dimensions.  

## Download & Setup
Download the source code, by running in the terminal:
```
git clone https://github.com/yasu-kun/Newton-s-method
```

## Preparation
This code uses sympy.
Install it with the following command if necessary.


```pip install sympy```  
         or  
```conda install simply```


## Using Newton's-method
### The `Newton`-constructor takes the following parameters:
* `function`: The function you want to find f(x) = 0

### The `Newton.solve`-constructor takes the following parameters:

* `Iteration`: number of calculations (for approximation) (default = 10)
* `Seed`: This is the initial value setting. (default isn't definded)
* `Verbose`: whether to display the calculation process (0: do not display, 1: display), (default = 0)
