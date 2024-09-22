# from py_vncorenlp import VnCoreNLP

class Tokenizer:
    def __init__(self) -> None:
        # self.rdrsegmenter = VnCoreNLP("vnpreprocess/package/vncorenlp/VnCoreNLP-1.2.jar", annotators="wseg")
        pass

    def word_segment(self, text):
        line = self.rdrsegmenter.word_segment(text)
        return ' '.join(line)