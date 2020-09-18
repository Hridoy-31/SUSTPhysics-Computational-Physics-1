# Algorithm for Lagrange Interpolation:

1. Obtain the data points

2. Create a user defined function for Lagrange Interpolation
   to reduce code complexity
   
3. Run two nested for loops within the range of x data points

4. Execute the following equation:
      p = p * ((x - xi[j]) / (xi[i] - xi[j]))
   where the iterators (i & j) are not same
   
5. Execute the summation of them and return to the calling position

6. Define the interpolation range with appropriate increment in x axis

7. Plot the incremented x data points and returned results from the user
   defined function
   
8. Do the appropriate labelling
