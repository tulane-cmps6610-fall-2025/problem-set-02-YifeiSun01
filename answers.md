  # CMPS 6610 Problem Set 02
## Answers

**Name:**_____Yifei Sun____________________


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

We prove that
$$\log(n!) \in \Theta(n \log n).$$

Asymptotic notation. We have: $\log(n!) = \sum_{k=1}^{n} \log k.$  

**Upper bound.** For every $1 \le k \le n$, $\log k \le \log n$. Hence $\log(n!) = \sum_{k=1}^{n} \log k \le \sum_{k=1}^{n} \log n = n \log n = O(n \log n).$  

**Lower bound.** At least half the terms in the sum satisfy $k \ge \frac{n}{2}$. That is, the terms for $k = \lceil n/2\rceil, \lceil n/2\rceil+1, \dots, n$ — there are at least $\frac n2$ of them — each has $\log k \ge \log(n/2) = \log n - \log 2.$  Therefore $\sum_{k=1}^{n} \log k \ge \sum_{k=\lceil n/2\rceil}^{n} \log k \ge \frac{n}{2} (\log n - \log 2) = \Omega(n \log n).$  

Combining upper and lower bounds yields: $\log(n!) \in \Theta(n \log n).$

---

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

- Leaf contribution: $n^{\log_b a} = \Theta(n^m)$.
- Internal levels sum:

  $$S(n) = \sum_{i=0}^{L-1} a^i f \left(\frac{n}{b^i}\right), \quad L \approx \log_b n.$$

Suppose $f(n)$ is a polynomial, i.e. $f(n) = \Theta(n^d)$ for some $d$.

Then the cost at level $i$ is

$$\text{cost}_i = a^i \left(\frac{n}{b^i}\right)^d = n^d \left(\frac{a}{b^d}\right)^i.$$

Thus

$$S(n) = n^d \sum_{i=0}^{\lfloor \log_b n \rfloor -1} r^i, \quad r = \frac{a}{b^d}, r \neq 1.$$

Using the geometric series sum,

$$\sum_{i=0}^{\lfloor \log_b n \rfloor -1} r^i = \frac{r^{\lfloor \log_b n \rfloor} -1}{r-1}.$$

So

$$S(n) = n^d \cdot \frac{r^{\lfloor \log_b n \rfloor} -1}{r-1}
     = n^d \cdot \frac{(a / b^d)^{\log_b n} - 1}{(a / b^d) - 1}
     = \frac{n^{\log_b a} - n^d}{(a / b^d) - 1}.$$

Putting that into $(\star)$, we get

$$T(n) = n^{\log_b a} + \frac{n^{\log_b a} - n^d}{(a / b^d) - 1}
       = \frac{a / b^d}{(a / b^d) - 1} n^{\log_b a}
         - \frac{1}{(a / b^d) - 1} n^d.$$

From this explicit expression one sees

- If $d > \log_b a$, then $n^d$ dominates, so $T(n) = \Theta(n^d)$.
- If $d < \log_b a$, then $n^{\log_b a}$ dominates, so $T(n) = \Theta\big(n^{\log_b a}\big)$.
- If $d = \log_b a$, then

  $$T(n) = n^{\log_b a} + \sum_{i=0}^{\lfloor \log_b n \rfloor -1} a^i \left(\frac{n}{b^i}\right)^{\log_b a}
         = n^{\log_b a} + \sum_{i=0}^{\lfloor \log_b n \rfloor -1} n^{\log_b a}
         = ( \log_b n + 1) n^{\log_b a}.$$

Thus in that case $T(n) = \Theta\big(n^{\log_b a} \log n\big)$.

---

1) T(n) = 2T(n/6) + 1
   a=2, b=6, m=log_6 2, f(n)=1 = Θ(n^0) with 0 < m.
   $$T(n) = \Theta\!\big(n^{\log_6 2}\big).$$

2) $$T(n) = 6T(n/4) + n$$
   a=6, b=4, m=log_4 6, f(n)=n = Θ(n^1) with 1 < m.
   $$T(n) = \Theta\!\big(n^{\log_4 6}\big).$$

3) $$T(n) = 7T(n/7) + n$$
   a=7, b=7, m=\log_7 7=1, f(n)=n with d=m (tie case).
   $$T(n) = \Theta(n\log n).$$

4) $$T(n) = 9T(n/4) + n^2$$
   a=9, b=4, m=\log_4 9 \approx 1.585, f(n)=n^2 with d=2>m.
   Regularity: a f(n/b) = 9 (n/4)^2 = (9/16) n^2 \le c n^2,\ c<1.
   $$T(n) = \Theta(n^2).$$

5) $$T(n) = 4T(n/2) + n^3$$
   a=4, b=2, m=\log_2 4=2, f(n)=n^3 with d=3>m.
   Regularity: a f(n/b) = 4 (n/2)^3 = \tfrac12 n^3 \le c n^3,\ c<1.
   $$T(n) = \Theta(n^3).$$

6) $$T(n) = 49T(n/25) + n^{3/2}\log n$$
   a=49, b=25, m=\log_{25} 49 = \frac{\ln 7}{\ln 5} \approx 1.209,
   f(n)=n^{3/2}\log n with d=1.5>m.
   Regularity: a f(n/b) = 49 (n/25)^{3/2} (\log n - \log 25)
   \le (49/125)\, n^{3/2}\log n for large n.
   $$T(n) = \Theta\!\big(n^{3/2}\log n\big).$$






2. **Algorithm Selection**






3. **More Algorithm Selection** 
 
4. **Integer Multiplication Timing Results**

5. **Black Hats and White Hats**
