# Lossless Compression
  D -> Compression Algorithm -> DepressionAlgorithm -> D

# Lossy Compression
  + Compression Ratio = ![EQ](http://www.sciweavers.org/tex2img.php?eq=%5Cfrac%7Bsize%28D%29%7D%7Bsize%28B%29%7D%20&bc=White&fc=Black&im=png&fs=12&ff=cmbright&edit=0)

# Self-Information
  + 資訊量
  + 單位：bits(base-2), hartley(base-10), nats(base-e)
  + Random Varible S Pr(S=U)
  - ![EQ1](http://www.sciweavers.org/tex2img.php?eq=%20-log_%7Bn%7DPr%28S%3DU%29%20%20%3D%20log_%7Bn%7D%20%5Cfrac%7B1%7D%7BPr%28S%3DU%29%7D%20&bc=White&fc=Black&im=png&fs=12&ff=cmbright&edit=0)


# Huffman Coding
+ The symbol can be coded with codes of different lengths
+ Variable-Length Coding (VLC)
+EX: HELLO

|       |H	  	|E	  	|L  		|O	  	|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|Count	|1	  	|1	  	|2	  	|1	  	|
|	    	|10		  |110  	|0  		|111  	|

# Extended Huffman Coding
+ Symbol Set S = { v1, v2, ..., vn }
+ Extended Symbol Set
