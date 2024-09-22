# Method
Apply to remove urls, brackets; standardize unicode, teencode, punctuation; lower text,... in Vietnamese text.
# Easy to use
## Install
```
pip install git+https://github.com/chienthan2vn/vietnamese-preprocess.git
```
For windows, run the following command:
```
requirements.exe
```
For linux, run the following command:
```
bash requirements.sh
```
## Use
```
from vnpreprocess.utils.process import Process

line = "t thích m!!!"
hand = Process()
hand = hand.tien_xu_li(line)
print(line)
```
output of example
```
tao thích mày
```

## Copyright ©️ Thuan Luong
