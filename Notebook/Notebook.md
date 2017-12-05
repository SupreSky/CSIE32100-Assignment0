## Lossless Compression
  D -> Compression Algorithm -> DepressionAlgorithm -> D

## Lossy Compression
  + Compression Ratio = ![EQ](http://www.sciweavers.org/tex2img.php?eq=%5Cfrac%7Bsize%28D%29%7D%7Bsize%28B%29%7D%20&bc=White&fc=Black&im=png&fs=12&ff=cmbright&edit=0)

## Self-Information
  + 資訊量
  + 單位：bits(base-2), hartley(base-10), nats(base-e)
  + Random Varible S ![EQ2](http://rogercortesi.com/eqn/tempimagedir/eqn6738.png)
  + 機率均等時：![EQ3](http://rogercortesi.com/eqn/tempimagedir/eqn1666.png)


## Huffman Coding
+ The symbol can be coded with codes of different lengths
+ Variable-Length Coding (VLC)
+EX: HELLO

|       |H	  	|E	  	|L  		|O	  	|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|Count	|1	  	|1	  	|2	  	|1	  	|
|	    	|10		  |110  	|0  		|111  	|

## Extended Huffman Coding
  + Symbol Set S = { v1, v2, ..., vn }
  + Extended Symbol Set

## Information Entropy (Shanon Entropy)
  + 機率不等時：![EQ4](http://rogercortesi.com/eqn/tempimagedir/eqn4680.png)

## Entropy Coding
  + Assigns Codes (0/1 bits) to symbols so as to match code lengths with the probabilities of the symbol.

## Lossless Coding Methods
  + Run-Length Coding
  + Huffman Coding  同長度符號　不同長度碼
  + LZW Coding     不同長度符號   同長度碼
  + Arithmetic Coding
