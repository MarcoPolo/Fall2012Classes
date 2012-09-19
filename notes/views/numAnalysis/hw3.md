
<script src='https://c328740.ssl.cf1.rackcdn.com/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'>
</script>

<pre>
<script>
MathJax.Hub.Config({
  tex2jax: {
    skipTags: ["script","noscript","style","textarea"]
    , inlineMath: [['$','$'], ['\\(','\\)']]
    , processEscapes: true
  }
});
</script>
</pre>

<p style='float:right'>Marco Munizaga</p>


                                              
##Homework 3 - Numerical Analysis##

###Section 2.3: 6c, 8, 10, 29cd###

#### Question 6c####
* Use Newton’s method to find solutions accurate to within $10^{ −5 }$ for the following problems.
* $ 2x cos(2x) − (x − 2)^2 = 0 \ \ for \ \  2 ≤ x ≤ 3 \  and \ 3 ≤ x ≤ 4 $
* for 2 ≤ x ≤ 3 

<pre>
    n   p
    -------------------
    1   1.54550969947
    2   -0.805445266775
    3   2.57151592254
    4   2.37012255853
    5   2.37068701658
    6   2.37068691766
    Done
</pre>

* for 3 ≤ x ≤ 4 

<pre>

    n   p
    -----------------
    1   3.74334928436
    2   3.72238954333
    3   3.72211282287
    4   3.7221127731
        Done
</pre> 


#### Question 8####

<pre>

2.35448991666
2.37314878343
2.37067411572
2.37068690797
Done
3.47969885855
3.68023250204
3.73192046128
3.72183380672
3.72211101707
3.72211277342
Done

</pre>

#### Question 10####

<pre>
1       2.35448991666
2       2.37314878343
3       2.37067411572
4       2.37068690797
Done
1       3.47969885855
2       3.68023250204
3       3.71664800443
4       3.72143690409
5       3.72202977757
6       3.72210259041
Done

</pre>


       
#### Question 29cd####

* Let $ f(x)=3^{ 3x+1 }−7*5^{ 2x } $
* Newtons Method:
* Only 10 iterations starting at -10. It does not converge, as expected
<pre>
1       -10.3125181429
2       -10.6249814176
3       -10.9373917712
4       -11.2497510633
5       -11.5620610709
6       -11.8743234931
7       -12.1865399553
8       -12.4987120134
9       -12.8108411579
10      -13.1229288166
</pre>





###Section 2.4: 6a, 9a###


#### Question 6a ####
* $ 5*10^{-2} = 1/20 $
* $ 1/4 - 1/5 = 5/20 - 4/20 = 1/20 $
* After 5 iterations It converges

#### Question 9a ####
* $ p_n = 10^{-3^n} $


