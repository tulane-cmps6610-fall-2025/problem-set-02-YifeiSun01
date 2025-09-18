  # CMPS 6610 Problem Set 02
## Answers

**Name:**_____Yifei Sun____________________


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**


Asymptotic notation. We have: $\log(n!) = \sum_{k=1}^{n} \log k.$  

**Upper bound.** For every $1 \le k \le n$, $\log k \le \log n$. Hence $\log(n!) = \sum_{k=1}^{n} \log k \le \sum_{k=1}^{n} \log n = n \log n = O(n \log n).$  

**Lower bound.** At least half the terms in the sum satisfy $k \ge \frac{n}{2}$. That is, the terms for $k = \lceil n/2\rceil, \lceil n/2\rceil+1, \dots, n$ — there are at least $\frac n2$ of them — each has $\log k \ge \log(n/2) = \log n - \log 2.$  Therefore $\sum_{k=1}^{n} \log k \ge \sum_{k=\lceil n/2\rceil}^{n} \log k \ge \frac{n}{2} (\log n - \log 2) = \Omega(n \log n).$  

Combining upper and lower bounds yields: $\log(n!) \in \Theta(n \log n).$



proof of master theorem

We consider the recurrence

$$T(n) = a \ T(n/b) + f(n), \quad a \ge 1, b \ge 1.$$

By iterating the recurrence $k$ times we get

$$T(n) = a^k \ T\left(\frac{n}{b^k}\right) + \sum_{i=0}^{k-1} a^i f\left(\frac{n}{b^i}\right).$$

When we recurse until subproblem size is about constant, i.e. $n / b^k \approx 1$, this means $k \approx \log_b n$. Thus

$$T(n) = a^{\log_b n} \ T(1) + \sum_{i=0}^{\lfloor \log_b n \rfloor -1} a^i \ f\left(\frac{n}{b^i}\right).$$

Since

$$a^{\log_b n} = n^{\log_b a},$$

we can write

$$ T(n)=c  n^{\log_b a}+\sum_{i=0}^{\lfloor\log_b n\rfloor-1} a^i f \left(\frac{n}{b^i}\right) (\star) $$

Here $c  n^{\log_b a}$ is the total work at the leaves (the base‐cases), and the sum is all the “extra work” from the non‐recursive parts at each level from the root down to just above the leaves.

Let $m = \log_b a$, and compare $n^m$ with $f(n)$.

- Leaf contribution: $ n^{log_b a} = \Theta(n^m)$.
- Internal levels sum:

  $$S(n) = \sum_{i=0}^{L-1} a^i f \left(\frac{n}{b^i}\right), \quad L \approx \log_b n.$$

Suppose $f(n)$ is a polynomial, i.e. $f(n) = \Theta(n^d)$ for some $d$.

Then the cost at level $i$ is

$$\text{cost}_i = a^i \left(\frac{n}{b^i}\right)^d = n^d \left(\frac{a}{b^d}\right)^i.$$

Thus

$$S(n) = n^d \sum_{i=0}^{\lfloor \log_b n \rfloor -1} r^i, \quad r = \frac{a}{b^d}, \; r \neq 1.$$

Using the geometric series sum,

$$\sum_{i=0}^{\lfloor \log_b n \rfloor -1} r^i = \frac{r^{\lfloor \log_b n \rfloor} -1}{r-1}.$$

So

$$S(n) = n^d \cdot \frac{r^{\lfloor \log_b n \rfloor} -1}{r-1}
     = n^d \cdot \frac{(a / b^d)^{\log_b n} - 1}{(a / b^d) - 1}
     = \frac{n^{\log_b a} - n^d}{(a / b^d) - 1}.$$

Putting that into $(\star)$, we get

$$T(n) = n^{\log_b a} + \frac{n^{\log_b a} - n^d}{(a / b^d) - 1}
       = \frac{a / b^d}{(a / b^d) - 1}\;n^{\log_b a}
         - \frac{1}{(a / b^d) - 1}\;n^d.$$

From this explicit expression one sees

- If $d > \log_b a$, then $n^d$ dominates, so $T(n) = \Theta(n^d)$.
- If $d < \log_b a$, then $n^{\log_b a}$ dominates, so $T(n) = \Theta\big(n^{\log_b a}\big)$.
- If $d = \log_b a$, then

  $$T(n) = n^{\log_b a} + \sum_{i=0}^{\lfloor \log_b n \rfloor -1} a^i \left(\frac{n}{b^i}\right)^{\log_b a}
         = n^{\log_b a} + \sum_{i=0}^{\lfloor \log_b n \rfloor -1} n^{\log_b a}
         = ( \log_b n + 1)\;n^{\log_b a}.$$

Thus in that case $T(n) = \Theta\big(n^{\log_b a} \; \log n\big)$.

---




2. **Algorithm Selection**






3. **More Algorithm Selection** 
 
4. **Integer Multiplication Timing Results**

5. **Black Hats and White Hats**
