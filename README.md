# SmallWorldNetCA

**1D Cellular Automata (CA) for any rule in the range of 0 to 255 can be drawn using this code.**

### Prameters
* `p` - probability of CA-world to follow given CA rule
* `q` - probability of choosing **_on_** or **_off_** state of the cell randomly when `p>0`
* `f` - fraction of cells in CA-world which will choose neighbors randomly
* `config` - _random_ or _uniform_

## Along with well known 1d cellular automata rules, there are implementations of few interesting variations described below

### Introduction of NOISE in 1D Cellular Automata
One can analyze the effect of noise in the CA-world. It is interesting to observe how a simple rule starting in a uniform CA-world can also result in a chaotic behavior with beautiful patterns.

I have shown **Rule 129** and **Rule 161** as an example. Both the rules show same fractal pattern of **_Sierpinski triangle_** but both result in completely different result when noise is inserted.

### Small World Network
For this to be implemented, a small change in neighborhood of CA-cell in each rule is made. The fraction `f` of cells are selected randomly and neighbors are assigned randomly to these selected cells. Based on neighborhood changes, if one uses a deterministic CA rule (without any noise `p=0`), the results show variation of patterns. Even with small value of `f`, huge changes can be observed.

# Sample Results
![RULE 126](Results/RULE126.png)
![RULE 126 - SMALL WORLD NETWORK](Results/RULE126_SMALLWORLD.png)

![RULE 129](Results/RULE129.png)
![RULE 129 - SMALL WORLD NETWORK](Results/RULE126_SMALLWORLD.png)

![RULE 129 - PARAMETER VARIATIONS](Results/Variation_RULE129.png)
![RULE 129 - PARAMETER VARIATIONS](Results/Variation_RULE129_2.png)
![RULE 129 SMALL WORLD NETWORK - PARAMETER VARIATIONS](Results/Variation_RULE129_SMALLWORLD.png)

![RULE 109 - PARAMETER VARIATIONS](Results/Variation_RULE109_1.png)
![RULE 109 - PARAMETER VARIATIONS](Results/Variation_RULE109_2.png)
![RULE 109 SMALL WORLD NETWORK - PARAMETER VARIATIONS](Results/Variation_RULE109_SMALLWORLD.png)
