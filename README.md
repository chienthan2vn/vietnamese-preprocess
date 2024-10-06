# Method
Apply to remove urls, brackets; standardize unicode, teencode, punctuation; lower text, word segmentation ,... in Vietnamese text.
# Easy to use
## Install
```
pip install git+https://github.com/chienthan2vn/vietnamese-preprocess.git
```

## Use
```
from vnpreprocess.utils.process import preprocessing

line = "T thik cks đá bóng vào mỗi buổi chiều (6h45) vs bb:>>>."
hand = preprocessing(line)
print(hand)
```
output of example
```
tao thích chơi đá bóng vào mỗi buổi chiều với bạn_bè
```

### Copyright ©️ Thuan Luong
