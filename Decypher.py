import roman

#text = "CXVIII CXVII CVII LII LII CV CII CXV L XLVIII XLIX LVII LVI LII LIV CXVIII CVI"
def  decypher(text_data):
    txt_splited = text_data.split()
    print(txt_splited)
    decyphered_text = ""
    for rd in txt_splited:
        plain_ch = chr(roman.fromRoman(rd))
        decyphered_text += plain_ch
    print(decyphered_text)
    return decyphered_text
