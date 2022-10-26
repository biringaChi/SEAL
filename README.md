### SEAL
Official Implementation of [A Secure Design Pattern Approach Toward Tackling Lateral-Injection Attacks](https://arxiv.org/pdf/2210.12877.pdf). The 15th IEEE International Conference on Security of Information and Networks (SIN'22).

Abstract
> A Secure-Behavioral design that extrapolates architectural, design, and implementation levels of abstraction to dynamically encapsulate and delegate lateral injection attack security strategies during software run-time.

To cite
```
@inproceedings{
	IEEE BibTex coming soon...
}
```

Disclaimer: Attack vectors employed in this work are strictly for educational and research purposes. Ergo, don't be a dick.

Installation
```
$ pip install -r requirements.txt
$ git clone https://github.com/biringaChi/SEAL
```

Running **SEAL**:
```
$ cd src
$ python main.py
```
Cases: Enter *input* below in the *entry field* and click *inject*

Case 1
```
User1
``` 

Case 2
```
User2
``` 

Case 3
```
'; UPDATE users SET Trust = 'T2' WHERE Username = 'User1'; SELECT 1; --
``` 

Case 4
```
User3
``` 

To cite

```
@inproceedings{coming soon...}
```

LICENSE:
[GNU GENERAL PUBLIC LICENSE](./LICENSE).