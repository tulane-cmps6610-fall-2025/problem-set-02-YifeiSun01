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

## Span recurrence: closed-form via geometric series

Assume a fork-join algorithm whose span satisfies the standard form
$$S(n) = S(n/b) + f(n)$$
and let the recursion stop when $n/b^k \approx 1$, i.e., $k \approx \log_b n$. Unrolling gives
$$S(n) = S(n/b^k) + \sum_{i=0}^{k-1} f \left(\frac{n}{b^i}\right).$$
For asymptotic purposes $S(n/b^k)$ is constant, so the dominant term is
$$S(n) = \sum_{i=0}^{k-1} f \left(\frac{n}{b^i}\right).$$

Now suppose $f(n) = n^d$ with $d>0$. Then
$$S(n) = \sum_{i=0}^{k-1} \left(\frac{n}{b^i}\right)^d = n^d \sum_{i=0}^{k-1} \left(\frac{1}{b^d}\right)^i.$$
With $k = \lfloor \log_b n \rfloor$ this is a finite geometric series:
$$S(n) = n^d \cdot \frac{1 - \left(1/b^d\right)^k}{1 - 1/b^d} = n^d \cdot \frac{1 - 1/b^{dk}}{1 - 1/b^d}.$$
Since $b^{k} \approx n$, we have $b^{dk} \approx n^d$, therefore
$$S(n) = n^d \cdot \frac{1 - 1/n^d}{1 - 1/b^d} = \frac{n^d - 1}{1 - 1/b^d}.$$

Hence the closed form for the span is
$$S(n) = \frac{n^d - 1}{1 - 1/b^d} = \Theta(n^d)\quad\text{for}\ d>0.$$

## Edge cases for span recurrence with $f(n)=n^d$

Assume $S(n)=S(n/b)+f(n)$, recursion stops when $n/b^k\approx1$ so $k\approx\log_b n$.

---

### Case $d=0$

Then $f(n)=\Theta(1)$.

Unroll gives

$$S(n)=\sum_{i=0}^{k-1} \Theta(1)=\Theta(k)=\Theta(\log_b n)$$

---

### Case $d<0$

Then $f(n)=n^d$ decays as $n$ grows.

Unroll gives

$$S(n)=\sum_{i=0}^{k-1} \left(\frac{n}{b^i}\right)^d = n^d \sum_{i=0}^{k-1} \left(\frac{1}{b^d}\right)^i$$

Since $1/b^d<1$ when $d<0$, geometric series converges as $k\to\infty$ to a constant:

$$S(n)=\Theta\left(n^d \cdot \frac{1}{1-1/b^d}\right)=\Theta(1)$$

---

### Summary

- If $d>0$, then $S(n)=\Theta(n^d)$  
- If $d=0$, then $S(n)=\Theta(\log_b n)$  
- If $d<0$, then $S(n)=\Theta(1)$


## Summary table: Master Theorem (work) and Span (fork–join)

| Model | Case | Input form | Conditions | Asymptotic result |
|---|---|---|---|---|
| Work | Case 1 | $T(n)=aT(n/b)+f(n)$ | $a\ge 1$, $b>1$, let $m=\log_b a$. If $f(n)=O(n^{m-\varepsilon})$ for some $\varepsilon>0$ | $T(n)=\Theta(n^{m})$ |
| Work | Case 2 | $T(n)=aT(n/b)+f(n)$ | $a\ge 1$, $b>1$, $f(n)=\Theta(n^{m})$ with $k\ge 0$ | $T(n)=\Theta(n^{m}\log_b n)$ |
| Work | Case 3 | $T(n)=aT(n/b)+f(n)$ | $a\ge 1$, $b>1$, $f(n)=\Omega(n^{m+\varepsilon})$ for some $\varepsilon>0$ and regularity $af(n/b)\le cf(n)$ for some $c<1$ and large $n$ | $T(n)=\Theta(f(n))$ |
| Span | $d>0$ | $S(n)=S(n/b)+n^{d}$ | Fork–join, full parallelism among equal subproblems, $b>1$, base constant | $S(n)=\Theta(n^{d})$ |
| Span | $d=0$ | $S(n)=S(n/b)+\Theta(1)$ | Same as above | $S(n)=\Theta(\log_b n)$ |
| Span | $d<0$ | $S(n)=S(n/b)+n^{d}$ | Same as above, $d<0$ so per-level cost decreases geometrically | $S(n)=\Theta(1)$ |

---

1) $$T(n) = 2T(n/6) + 1$$

   $$a=2, b=6, m=log_6 2$$, $$f(n)=1 = Θ(n^0)$$ with $$0 < m$$.

   $$T(n) = \Theta\big(n^{\log_6 2}\big).$$

   $$S(n) = \Theta(\log n)$$

2) $$T(n) = 6T(n/4) + n$$

   $$a=6, b=4, m=log_4 6, f(n)=n = Θ(n^1)$$ with $$1 < m$$.

   $$T(n) = \Theta\big(n^{\log_4 6}\big).$$

   $$S(n) = \Theta(n)$$

3) $$T(n) = 7T(n/7) + n$$

   $$a=7, b=7, m=\log_7 7=1, f(n)=n$$ with $$d=m$$ (tie case).

   $$T(n) = \Theta(n\log n).$$

   $$S(n) = \Theta(n)$$

4) $$T(n) = 9T(n/4) + n^2$$

   $$a=9, b=4, m=\log_4 9 \approx 1.585$$, $$f(n)=n^2$$ with $$d=2>m$$.

   Regularity: $$a f(n/b) = 9 (n/4)^2 = (9/16) n^2 \le c n^2,\ c<1$$.

    $$T(n) = \Theta(n^2).$$

   $$S(n) = \Theta(n^2)$$

5) $$T(n) = 4T(n/2) + n^3$$

   $$a=4, b=2, m=\log_2 4=2$$, $$f(n)=n^3$$ with $$d=3>m$$.

    Regularity: $$a f(n/b) = 4 (n/2)^3 = \tfrac12 n^3 \le c n^3,\ c<1$$.

   $$T(n) = \Theta(n^3).$$

   $$S(n) = \Theta(n^3)$$

6) $$T(n) = 49T(n/25) + n^{3/2}\log n$$
 
   $$a=49, b=25, m=\log_{25} 49 = \frac{\ln 7}{\ln 5} \approx 1.209$$,

    $$f(n)=n^{3/2}\log n$$ with $$d=1.5>m$$.

    Regularity: $$a f(n/b) = 49 (n/25)^{3/2} (\log n - \log 25) \le (49/125) n^{3/2}\log n$$ for large $$n$$.

    $$T(n) = \Theta\big(n^{3/2}\log n\big).$$

    $$S(n) = \Theta\big(n^{3/2}\log n\big).$$

7) $$T(n) = T(n - 1) + 2$$

We solve the recurrence

$$T(n) = T(n - 1) + 2$$

Assume the base case is

$$T(1) = C$$

where \(C\) is a constant, for all \(n \ge 2\).

Then

$$T(n) = T(n - 1) + 2$$

$$= (T(n - 2) + 2) + 2$$

$$= T(n - 2) + 2 \cdot 2$$

$$= (T(n - 3) + 2) + 2 \cdot 2$$

$$= T(n - 3) + 3 \cdot 2$$

$$\vdots$$

$$= T(1) + (n - 1) \cdot 2$$

$$= C + 2(n - 1)$$

Therefore

$$T(n) = 2n - 2 + C$$

Using asymptotic notation, since \(C\) is constant:

$$T(n) = \Theta(n)$$

$$S(n) = \Theta(n)$$

8) $$T(n) = T(n-1) + n^c,  c \gt 1$$

Suppose we have the recurrence

$$T(n) = T(n-1) + n^c$$

with some constant $\(c \gt 1\)$. Assume base case $\(T(0) = C\)$ (or $\(T(1)=C\)$, differs by constant). Then

$$T(n) = C + \sum_{k=1}^n k^c$$

This is the sum of the first \(n\) integers each raised to the \(c\)-th power. For integer \(c\), there is a closed-form given by Faulhaber’s Formula: it is a polynomial in \(n\) of degree \(c+1\). The leading term is

$$\sum_{k=1}^n k^c = \frac{n^{c+1}}{c+1} + \frac12 n^c + O(n^{c-1})$$

Hence

$$T(n) = \Theta(n^{c+1})$$

$$S(n) = \Theta(n^{c+1})$$

Faulhaber’s formula (with Bernoulli numbers \(B_r\)) gives

$$\sum_{k=1}^n k^c = \frac{1}{c+1} \sum_{r=0}^c \binom{c+1}{r} B_r n^{ c+1-r}$$

Therefore the sum is a \((c+1)\)-degree polynomial in \(n\); the first few terms are

$$\sum_{k=1}^n k^c = \frac{n^{c+1}}{c+1} + \frac12 n^c + (\text{lower-order terms})$$

9) $$T(n) = T(\sqrt{n}) + 1$$

We consider the recurrence

$$T(n) = T(\sqrt{n}) + 1$$

Assume some base case $\(T(n_0) = C\)$, where $\(C\)$ is constant.

Let $\(n = 2^m\)$, and define

$$S(m) = T(2^m)$$

Then $\(\sqrt{n} = 2^{m/2}\)$. Substituting,

$$T(2^m) = T\bigl((2^m)^{1/2}\bigr) + 1 = T(2^{m/2}) + 1$$

This gives

$$S(m) = S\left(\frac{m}{2}\right) + 1$$

The recurrence $\(S(m) = S(m/2) + 1\)$ is a “halve every time + constant” type. Its solution is

$$S(m) = \Theta(\log m)$$

Since $\(m = \log_2 n\)$, we have

$$T(n) = S(\log_2 n) = \Theta\bigl(\log(\log n)\bigr)$$

$$S(n) = \Theta\bigl(\log(\log n)\bigr)$$

2. **Algorithm Selection**

## Recurrence 1:  
$$W(n) = 2 W(n/5) + \Theta(n^2)$$

**Use the Master Theorem**

- Let  
  $a = 2, b = 5, f(n) = \Theta(n^2)$  
- Compute  
  $$n^{\log_b a} = n^{\log_5 2} \approx n^{0.43}$$  
- Compare $f(n)$ with $n^{\log_b a}$:  
  $f(n) = n^2$ is polynomially larger than $n^{0.43}$, i.e.  
  $f(n) = \Omega(n^{\log_5 2 + \varepsilon})$ for some $\varepsilon > 0$.  

- Check regularity condition (smoothness):  
  $$a f(n/b) = 2 \cdot \Theta((n/5)^2) = \Theta(n^2/25) = \Theta(n^2) \cdot \frac{2}{25} < c \cdot \Theta(n^2)$$  
  for some constant $c < 1$. So condition holds.

- By **Case 3** of Master Theorem:

  $$W(n) = \Theta(f(n)) = \Theta(n^2)$$

- Span with full parallelism:  
  $$S(n) = S(n/5) + \Theta(n^2) \implies S(n) = \Theta(n^2)$$

---

## Recurrence 2:  
$$W(n) = W(n-1) + \Theta(\log n)$$

**Use summation + Stirling’s approximation**

- Unroll the recurrence:

  $$W(n) = W(1) + \sum_{k=2}^n \Theta(\log k) = \Theta\left(\sum_{k=1}^n \log k\right)$$

- Recognize:

  $$\sum_{k=1}^n \log k = \log(n!)$$

- By Stirling’s approximation:

  $$\log(n!) = n \log n - n + O(\log n) = \Theta(n \log n)$$

- Thus:

  $$W(n) = \Theta(n \log n)$$

- Since only one recursive branch (no parallelism), span $S(n)$ has the same order:

  $$S(n) = \Theta(n \log n)$$

  We also proved this in the first question.

## Recurrence 3:  

Proof of $T(n)=T(n/3)+T(2n/3)+\Theta(n^{1.1})$ via recursion tree including leaf cost

Setup: assume combine cost is $\Theta(m^{1.1})$ base case $T(1)=\Theta(1)$

Level 0:  
$T(n)=c n^{1.1}+T(n/3)+T(2n/3)$

Level 1:  
$T(n)=c n^{1.1}(1+(1/3)^{1.1}+(2/3)^{1.1})+[T(n/9)+2T(2n/9)+T(4n/9)]$

General level t: the cost of level t is  
$\Sigma_{t}=\sum_{k=0}^{t}\binom{t}{k}c (n\cdot2^{k}/3^{t})^{1.1}=c n^{1.1}3^{-1.1t}\sum_{k=0}^{t}\binom{t}{k}(2^{1.1})^{k}=c n^{1.1}((1+2^{1.1})/3^{1.1})^{t}=c n^{1.1} \theta^{t}$ where $\theta=(1/3)^{1.1}+(2/3)^{1.1}<1$

Internal cost non-leaf levels:  
$\sum_{t=0}^{\infty}\Sigma_{t}=c n^{1.1}\sum_{t=0}^{\infty}\theta^{t}=\frac{c}{1-\theta}n^{1.1}=\Theta(n^{1.1})$

Leaf cost: there are $O(n)$ leaves each of cost $\Theta(1)$ so leaf total cost $O(n)=o(n^{1.1})$

Conclusion: $T(n)=\Theta(n^{1.1})$

Here because the leaf node total cost is neglegible compared to the extra work, the span is the same as the work which is $T(n)=\Theta(n^{1.1})$. The total work of all nodes on the same level are the same. Because $n/3+2n/3=n$, and this equal relationship continues to the last level which is the leaf node. But the extra work on each level is $n^{1.1}$ and this extra work shrinks by $(1/3)^{1.1}+(2/3)^{1.1}<1$ every layer so the sum is bounded by an upper bound which is $n^{1.1}$

---

## Summary table: Work and Span (three recurrences)

| Recurrence | Work recurrence | Work Θ-result | Span recurrence | Span Θ-result |
|---|---|---|---|---|
| Recurrence 1: $W(n)=2 W(n/5)+\Theta(n^2)$ | $W(n)=2 W(n/5)+\Theta(n^2)$ | $\Theta(n^2)$ | $S(n)=S(n/5)+\Theta(n^2)$ | $\Theta(n^2)$ |
| Recurrence 2: $W(n)=W(n-1)+\Theta(\log n)$ | $W(n)=W(n-1)+\Theta(\log n)$ | $\Theta(n\log n)$ | $S(n)=S(n-1)+\Theta(\log n)$ | $\Theta(n\log n)$ |
| Recurrence 3: $T(n)=T(n/3)+T(2n/3)+\Theta(n^{1.1})$ | $T(n)=T(n/3)+T(2n/3)+\Theta(n^{1.1})$ | $\Theta(n^{1.1})$ | $S(n)=\max(S(n/3),S(2n/3))+\Theta(n^{1.1})$ | $\Theta(n^{1.1})$ |



I will choose the second one, because we have $\Theta(n^2)$, $\Theta(n \log n)$, $\Theta(n^{1.1})$, if divide by $n$, it is $\Theta(n^1)$, $\Theta(\log n)$, $\Theta(n^{0.1})$. $logn$ is quicker than polynomial.


3. **More Algorithm Selection** 

## Algorithm A: Work / Span Proof

Algorithm A: divide a problem of size $n$ into 5 subproblems each of size $n/2$, solve recursively, then combine in linear time.

---

### Work Proof

Let work be $W(n)$. Combine step takes $\Theta(n)$. Then

$$W(n) = 5 W\left(\frac{n}{2}\right) + \Theta(n)$$

By Master Theorem let $a = 5$, $b = 2$, $f(n) = \Theta(n)$. Compute $\log_b a = \log_2 5 \approx 2.3219$. Since $f(n) = \Theta(n) = O\big(n^c\big)$ with $c = 1 < \log_2 5$, this is Case 1 of the theorem.

Then

$$W(n) = \Theta\left(n^{\log_2 5}\right)$$

Alternate recursion-tree argument: recursion depth $k \approx \log_2 n$. On level $i$ there are $5^i$ subproblems each of size $n/2^i$. Work of combine at level $i$ is

$$5^i \cdot \Theta\left(\frac{n}{2^i}\right) = \Theta\left(n \cdot \left(\frac{5}{2}\right)^i\right)$$

Summing over $i = 0$ to $\log_2 n$ yields $\Theta\left(n^{\log_2 5}\right)$. Leaves contribute same order. So

$$\boxed{W(n) = \Theta\left(n^{\log_2 5}\right)}$$

---

### Span Proof

Let span (critical path length) be $S(n)$. Assume combine step is sequential and costs $\Theta(n)$. Then

$$S(n) = S\left(\frac{n}{2}\right) + \Theta(n)$$

Unroll recursion until size is constant, depth $k \approx \log_2 n$. Then

$$S(n) = \Theta(n) + \Theta\left(\frac{n}{2}\right) + \Theta\left(\frac{n}{4}\right) + \cdots + \Theta(1)$$

That is

$$S(n) = \Theta\left(\sum_{i=0}^{\log_2 n - 1} \frac{n}{2^i}\right)$$

Geometric series with ratio $1/2$ so sum is $\Theta(n)$. Thus

$$\boxed{S(n) = \Theta(n)}$$

---

### Final Comparison

$$W(n) = \Theta\left(n^{\log_2 5}\right),\quad S(n) = \Theta(n)$$

## Algorithm B: Work and Span

**Setup.** The algorithm solves two subproblems of size $n-1$ and combines in constant time.

### Work
Recurrence:
$$W(n)=2 W(n-1)+\Theta(1).$$
Unroll:
$$W(n)=2^k W(n-k)+\Theta \left(\sum_{i=0}^{k-1}2^i\right).$$
Set $k=n$ (base case at constant size), then $\sum_{i=0}^{n-1}2^i=\Theta(2^n)$, hence
$$W(n)=\Theta(2^n).$$

### Span
With both subproblems executed in parallel, span takes the longest branch plus constant combine time:
$$S(n)=S(n-1)+\Theta(1).$$
Unroll to the base case through $n$ levels:
$$S(n)=\Theta \left(\sum_{i=0}^{n-1}1\right)=\Theta(n).$$

### Conclusion
$$W(n)=\Theta(2^n),\quad S(n)=\Theta(n).$$


## Algorithm C: Work and Span Proof

**Setup.** The algorithm divides a size $n$ problem into $a=9$ subproblems of size $n/b=n/3$, solves them recursively, and combines in $f(n)=\Theta(n^2)$ time.

---

### Work

The work satisfies
$$W(n)=9 W(n/3)+\Theta(n^2).$$

Compute $\log_b a=\log_3 9=2$, so $f(n)=\Theta \big(n^{\log_b a}\big)$. By the Master Theorem (case 2),
$$W(n)=\Theta \big(n^{\log_b a}\log n\big)=\Theta \big(n^2\log n\big).$$

---

### Span

All 9 subproblems run in parallel, so the span satisfies
$$S(n)=S(n/3)+\Theta(n^2).$$

Unrolling to depth $k\approx\log_3 n$,
$$S(n)=\Theta(n^2)\sum_{i=0}^{k-1}\left(\frac{1}{3^2}\right)^i
=\Theta(n^2)\cdot\frac{1-(1/9)^k}{1-1/9}
=\Theta(n^2).$$

---

### Conclusion

$$W(n)=\Theta \big(n^2\log n\big),\quad S(n)=\Theta \big(n^2\big).$$

## Summary table: Work and Span

| Algorithm | Work recurrence | Work Θ-result | Span recurrence | Span Θ-result |
|---|---|---|---|---|
| A (5 subproblems of size n/2, linear combine) | $W(n)=5 W(n/2)+\Theta(n)$ | $\Theta\big(n^{\log_2 5}\big)$ | $S(n)=S(n/2)+\Theta(n)$ | $\Theta(n)$ |
| B (two subproblems of size n−1, constant combine) | $W(n)=2 W(n-1)+\Theta(1)$ | $\Theta(2^n)$ | $S(n)=S(n-1)+\Theta(1)$ | $\Theta(n)$ |
| C (9 subproblems of size n/3, $O(n^2)$ combine) | $W(n)=9 W(n/3)+\Theta(n^2)$ | $\Theta(n^2\log n)$ | $S(n)=S(n/3)+\Theta(n^2)$ | $\Theta(n^2)$ |

I will choose A. Though A has larger work than C, but the span is smaller. It can be parallized in faster time.

 
4. **Integer Multiplication Timing Results**

5. **Black Hats and White Hats**
