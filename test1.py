import pynlpir
pynlpir.open()
mystring = "你汉语说的很好！"
tokenized_string = pynlpir.segment(mystring, pos_tagging=False)

print(tokenized_string)
