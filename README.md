# Method
Apply to remove urls, brackets; standardize unicode, teencode, punctuation; lower text,... in Vietnamese text.
# Easy to use
## Install
```
pip install git+https://github.com/chienthan2vn/vietnamese-preprocess.git
```

## Use
```
from vnpreprocess.utils import process

line = "T thik cks đá bóng vào mỗi buổi chiều (6h45) vs bb:>>>."
hand = process.Process()
hand = hand.tien_xu_li(line)
print(hand)
```
output of example
```
tao thích chơi đá bóng vào mỗi buổi chiều với bạn bè
```

### Copyright ©️ Thuan Luong
