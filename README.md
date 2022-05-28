**MuSI** &mdash; Secure-Behavioral Design for Run-time Delegation of Lateral Injection Attack Security Strategies.

Description: A Secure-Behavioral design that extrapolates architectural, design, and implementation levels of abstraction to dynamically encapsulate and delegate lateral injection attack security strategies during software run-time.

Installation:
```
$ pip install -r requirements.txt
$ git clone https://github.com/biringaChi/MuSI
```

Running **MuSI**:
```
$ cd src
$ python main.py
```
Cases: Enter *input* below in the *entry field* and click *inject*

Case 1:
```
User1
``` 

Case 2:
```
User2
``` 

Case 3:
```
'; UPDATE users SET Trust = 'T2' WHERE Username = 'User1'; SELECT 1; --
``` 

Case 4:
```
User3
``` 

To cite:

```
@inproceedings{coming soon...}
```