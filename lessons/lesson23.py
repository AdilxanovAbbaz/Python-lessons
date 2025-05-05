#   Sirqi bibliotekalar (pip install )
from googletrans import Translator

def translate1(text):
    o=Translator()
    awdarma=o.tranlate(text=text, src="uz", dest="ru")
    return awdarma.text
text1=input("chahsdh;kjags;dkjhalksdh kjashdkjahsd;kjahs;dk: ")
a=translate1(text1)
print(f"maksldmlak;sdm;akl:{a}")