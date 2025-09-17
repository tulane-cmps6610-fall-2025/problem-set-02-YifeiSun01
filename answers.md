  # CMPS 6610 Problem Set 02
## Answers

**Name:**_____Yifei Sun____________________


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**


Asymptotic notation. We have: $\log(n!) = \sum_{k=1}^{n} \log k.$  

**Upper bound.** For every $1 \le k \le n$, $\log k \le \log n$. Hence $\log(n!) = \sum_{k=1}^{n} \log k \le \sum_{k=1}^{n} \log n = n \log n = O(n \log n).$  

**Lower bound.** At least half the terms in the sum satisfy $k \ge \frac{n}{2}$. That is, the terms for $k = \lceil n/2\rceil, \lceil n/2\rceil+1, \dots, n$ — there are at least $\frac n2$ of them — each has $\log k \ge \log(n/2) = \log n - \log 2.$  Therefore $\sum_{k=1}^{n} \log k \ge \sum_{k=\lceil n/2\rceil}^{n} \log k \ge \frac{n}{2} (\log n - \log 2) = \Omega(n \log n).$  

Combining upper and lower bounds yields: $\log(n!) \in \Theta(n \log n).$




2. **Algorithm Selection**

3. **More Algorithm Selection** 
 
4. **Integer Multiplication Timing Results**

5. **Black Hats and White Hats**
