# TopsisPy


TopsisPy is a Python Package implementing [Topsis](https://en.wikipedia.org/wiki/TOPSIS) method used for multi-criteria decision analysis.
Topsis stands for 'Technique for Order of Preference by Similarity to Ideal Solution'.

TopsisPy intends to make the process of TOPSIS simple in python. Key features of the package are -

  - Easy to use
  - Numpy based
  - Ideal for Students

And off course, PyTopsis code is Open Source.

### How to use?
Install the Package using the command - 
```s
$ pip install topsispy
```
And using this Package in python as - 
```s
>>> import topsispy as tp
>>> a =[
...     [250, 16, 12, 5],
...     [200, 16, 8, 3],
...     [300, 32, 16, 4],
...     [275, 32, 8, 4],
...     [225, 16, 16, 2]
... ]
>>> w = [0.25, 0.25, 0.25, 0.25]
>>> sign = [-1, 1, 1, 1]
>>> tp.topsis(a, w, sign)
```

#### Or
 You may use the Package via commandline as -
 ```s
$ python [package name] [path of csv as string] [list of weights as string] [list of sign as string]
```
*Here, as string means using " "*


This will return a tuple with
1. the index of winning data point
2. array containing scores of all data points
As for above -
```s
(2, array([0.53427686, 0.30836777, 0.69163223, 0.53473658, 0.40104612]))
```

### Development

Want to contribute? Great!
Use your Python skills and creativity for easy decision making for the world.

License
----

MIT

**Free Software, Hell Yeah!**
