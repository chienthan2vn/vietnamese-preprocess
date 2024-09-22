import unicodedata
import re
import vnpreprocess as p

class Process():
    def __init__(self):
        self.bang_nguyen_am = [['a', 'à', 'á', 'ả', 'ã', 'ạ', 'a'],
                  ['ă', 'ằ', 'ắ', 'ẳ', 'ẵ', 'ặ', 'aw'],
                  ['â', 'ầ', 'ấ', 'ẩ', 'ẫ', 'ậ', 'aa'],
                  ['e', 'è', 'é', 'ẻ', 'ẽ', 'ẹ', 'e'],
                  ['ê', 'ề', 'ế', 'ể', 'ễ', 'ệ', 'ee'],
                  ['i', 'ì', 'í', 'ỉ', 'ĩ', 'ị', 'i'],
                  ['o', 'ò', 'ó', 'ỏ', 'õ', 'ọ', 'o'],
                  ['ô', 'ồ', 'ố', 'ổ', 'ỗ', 'ộ', 'oo'],
                  ['ơ', 'ờ', 'ớ', 'ở', 'ỡ', 'ợ', 'ow'],
                  ['u', 'ù', 'ú', 'ủ', 'ũ', 'ụ', 'u'],
                  ['ư', 'ừ', 'ứ', 'ử', 'ữ', 'ự', 'uw'],
                  ['y', 'ỳ', 'ý', 'ỷ', 'ỹ', 'ỵ', 'y']]
        self.bang_ky_tu_dau = ['', 'f', 's', 'r', 'x', 'j']
        self.nguyen_am_to_ids = {}

        for i in range(len(self.bang_nguyen_am)):
            for j in range(len(self.bang_nguyen_am[i]) - 1):
                self.nguyen_am_to_ids[self.bang_nguyen_am[i][j]] = (i, j)

    """
    Chuẩn hóa unicode 
    Có 2 loại unicode : unicode tổ hơp và unicode dựng sẵn, điêu này dẫn tới việc 2 từ giống nhau sẽ bị coi là khác nhau 
    Chuẩn hóa tất cả về 1 loại là unicode dựng sẵn
    """
    def chuan_hoa_unicode(self, text):
        text = unicodedata.normalize('NFC', text)
        return text


    """
    Có 2 kiểu gõ dấu ở Tiếng Việt, ví dụ như là : òa hoặc oà (ta gọi lần lượt là chuẩn 1 và 2). Mặc dù kiểu gõ chữ sau ít 
    phổ biến hơn tuy nhiên vẫn cần phải chuẩn hóa tránh việc một số văn bản vẫn sử dụng kiểu gõ dấu thứ 2.
    
    Hàm này xử lý chuẩn hóa từng từ một, sau khi chuẩn hóa từng từ thì ta sẽ đi chuân hóa từng câu sau 
    """ 
    def chuan_hoa_dau_tu_tieng_viet(self, word):
        if not self.is_valid_vietnam_word(word):
            return word
    
        chars = list(word)
        dau_cau = 0
        nguyen_am_index = []
        qu_or_gi = False
        for index, char in enumerate(chars):
            x, y = self.nguyen_am_to_ids.get(char, (-1, -1))
            if x == -1:
                continue
            elif x == 9:  # check qu
                if index != 0 and chars[index - 1] == 'q':
                    chars[index] = 'u'
                    qu_or_gi = True
            elif x == 5:  # check gi
                if index != 0 and chars[index - 1] == 'g':
                    chars[index] = 'i'
                    qu_or_gi = True
            if y != 0:
                dau_cau = y
                chars[index] = self.bang_nguyen_am[x][0]
            if not qu_or_gi or index != 1:
                nguyen_am_index.append(index)
        if len(nguyen_am_index) < 2:
            if qu_or_gi:
                if len(chars) == 2:
                    x, y = self.nguyen_am_to_ids.get(chars[1])
                    chars[1] = self.bang_nguyen_am[x][dau_cau]
                else:
                    x, y = self.nguyen_am_to_ids.get(chars[2], (-1, -1))
                    if x != -1:
                        chars[2] = self.bang_nguyen_am[x][dau_cau]
                    else:
                        chars[1] = self.bang_nguyen_am[5][dau_cau] if chars[1] == 'i' else self.bang_nguyen_am[9][dau_cau]
                return ''.join(chars)
            return word
    
        for index in nguyen_am_index:
            x, y = self.nguyen_am_to_ids[chars[index]]
            if x == 4 or x == 8:  # ê, ơ
                chars[index] = self.bang_nguyen_am[x][dau_cau]
                return ''.join(chars)
    
        if len(nguyen_am_index) == 2:
            if nguyen_am_index[-1] == len(chars) - 1:
                x, y = self.nguyen_am_to_ids[chars[nguyen_am_index[0]]]
                chars[nguyen_am_index[0]] = self.bang_nguyen_am[x][dau_cau]
            else:
                x, y = self.nguyen_am_to_ids[chars[nguyen_am_index[1]]]
                chars[nguyen_am_index[1]] = self.bang_nguyen_am[x][dau_cau]
        else:
            x, y = self.nguyen_am_to_ids[chars[nguyen_am_index[1]]]
            chars[nguyen_am_index[1]] = self.bang_nguyen_am[x][dau_cau]
        return ''.join(chars)
    

    def is_valid_vietnam_word(self, word):
        chars = list(word)
        nguyen_am_index = -1
        for index, char in enumerate(chars):
            x, y = self.nguyen_am_to_ids.get(char, (-1, -1))
            if x != -1:
                if nguyen_am_index == -1:
                    nguyen_am_index = index
                else:
                    if index - nguyen_am_index != 1:
                        return False
                    nguyen_am_index = index
        return True
    

    """
    Chuyển câu tiếng việt về chuẩn gõ dấu kiểu cũ.
    :param sentence:
    :return:
    """
    def chuan_hoa_dau_cau_tieng_viet(self, sentence):
        sentence = self.chuyen_chu_thuong(sentence)
        words = sentence.split()
        for index, word in enumerate(words):
            cw = re.sub(r'(^\p{P}*)([p{L}.]*\p{L}+)(\p{P}*$)', r'\1/\2/\3', word).split('/')
            # print(cw)
            if len(cw) == 3:
                cw[1] = self.chuan_hoa_dau_tu_tieng_viet(cw[1])
            words[index] = ''.join(cw)
        return ' '.join(words).strip()
    

    # Đưa về chữ viết thường 
    def chuyen_chu_thuong(self, text):
        return text.lower()
    

    #Xóa html
    def xoa_url(self, text):
        return re.sub(r"\S*https?:\S*", "", text)
    

    #Xoa ngoac va noi dung trong ngoac
    def xoa_ngoac(self, text):
        return re.sub(r'\[.*?\]|\(.*?\)|<.*?>|\{.*?\}', '', text)

    # Xóa đi các dấu cách thừa các từ không cần thiết cho việc phân loại vẳn bản 
    def chuan_hoa_cau(self, text):
        text = re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_]',' ',text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    

    # chuan hoa teencode: vn -> Việt Nam
    def de_teencode(self, text):
        nText = ""
        for word in text.split():
            nText += ''.join(p.teencode_list.get(word, word)+ " ")
        return nText

    def tien_xu_li(self, text):
        text = self.chuan_hoa_unicode(text)
        text = self.chuyen_chu_thuong(text)
        text = self.xoa_url(text)
        text = self.xoa_ngoac(text)
        text = self.chuan_hoa_cau(text)
        text = self.de_teencode(text)
        text = self.chuan_hoa_dau_cau_tieng_viet(text)
        return text