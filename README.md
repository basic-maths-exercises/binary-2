# Binary conversion

You should have noticed in the previous exercise that each of the 8 lists of ones and zeros that we input into the function you wrote gave a different value for `b`.   In addition, the 8 numbers that were output were the first 8 non-negative integers.  

The 8 sequences that were input are in fact the binary representations of these first 8 numbers.  In other words, the lists we wrote out are the numbers 0 through to 7 in a base 2 representation.  Notice that the mapping between these binary representations and the numbers is both injective and surjective. It thus stands to reason that we can invert this relation.  In other words, if we are given an integer between 0 and ![](https://render.githubusercontent.com/render/math?math=2^{N-1}) we can generate the corresponding binary representation coordinates.  I would like you to add lines to the program in the box on the left here in order to do this conversion.  You will notice that I have written a function called `get_binary` for you that takes the number of digits of binary, `N`, and a non-negative integer, `index`, that is less than ![](https://render.githubusercontent.com/render/math?math=2^N).  This function then returns a list called `binary` that should contain the binary digits.

To help you understand how to write the program consider what the sum in the expression above is if `N=3`.  In that case:

![](https://render.githubusercontent.com/render/math?math=b=a_0%2B2a_1%2B4a_2)

Furthermore, ![](https://render.githubusercontent.com/render/math?math=a_0), ![](https://render.githubusercontent.com/render/math?math=a_1) and ![](https://render.githubusercontent.com/render/math?math=a_2) must be equal to 0 or 1 and `b` has to be less than or equal to 7.  Notice that if take the floor of  ![](https://render.githubusercontent.com/render/math?math=\frac{b}{4}) using the command:

````
a2 = np.floor( b / 4 )
````

we get ![](https://render.githubusercontent.com/render/math?math=a_2).  We can then get ![](https://render.githubusercontent.com/render/math?math=a_1) by doing:

````
a1 = np.floor( (b - 4*a2) / 2 )
````

and ![](https://render.githubusercontent.com/render/math?math=a_0) by doing:

````
a0 = b - 4*a2 - 2*a1
````

Your task is to generalise the insight outlined above and to make the above algorithm work for arbitrary values of N.
