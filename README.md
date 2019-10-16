# SimpleRSA
### Usage
#### Encryption
Use **Public Key (n, e)** and **Message (m)** to compute **Cipher-text (c)**.

Input:
One test case has only one line, which contains two integers (n, e) and one string (m).

![](https://latex.codecogs.com/gif.latex?6&space;\leq&space;n&space;\leq&space;10^{18})

![](https://latex.codecogs.com/gif.latex?1&space;\leq&space;e&space;\leq&space;10^{8})

Output:
One test case only needs one line which is a string of cipher-text (separated by comma).

#### Decryption
Use **Public Key (n, e)** and **Cipher-text (c)** to break RSA cryptography and compute **Message (m)**.

Input:
One test case has only one line, which contains two integers (n, e) and one string (c, separated by comma).

![](https://latex.codecogs.com/gif.latex?6&space;\leq&space;n&space;\leq&space;10^{18})

![](https://latex.codecogs.com/gif.latex?1&space;\leq&space;e&space;\leq&space;10^{8})


Output
One test case only needs one line which is a string of message.

#### Testdata
in `encryption_data` and `decryption_data`