# Method
Apply to remove urls, brackets; standardize unicode, teencode, punctuation; lower text,... in Vietnamese text.
# Easy to use
## Install
```
pip install git+https://github.com/chienthan2vn/vietnamese-preprocess.git
```
For windows, copy&run the following command:
```
requirements.exe
```
For linux, copy&run the following command:
```
bash requirements.sh
```
## Use
```
from vnpreprocess.utils import process

line = "t thích m!!!"
hand = process.Process()
hand = hand.tien_xu_li(line)
print(line)
```
output of example
```
tao thích mày
```

## Copyright ©️ Thuan Luong
