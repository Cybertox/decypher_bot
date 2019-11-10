import roman

#text1 = "CXVIII CXVII CVII LII LII CV CII CXV L XLVIII XLIX LVII LVI LII LIV CXVIII CVI"
#text2 = "-.../..../..-./..././...-/./-./-./../-././../..-./.../-/.--/---/--.././.-./---/---/-././-./../-././-/..../.-././././../--./..../-/-/..../.-./././-../-"
def  roman2arabic(text_data):
    txt_splited = text_data.split()
    print(txt_splited)
    decyphered_text = ""
    for rd in txt_splited:
        plain_ch = chr(roman.fromRoman(rd))
        decyphered_text += plain_ch
    print(decyphered_text)
    return decyphered_text
def morze2arabic(text_data):
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}
    separator = '/'
    txt_splited = text_data.split(separator)
    print(txt_splited)
    decyphered_text = ""
    for rd in txt_splited:
        for i in MORSE_CODE_DICT:
            if rd == MORSE_CODE_DICT[i]:
                decyphered_text += i
    print(decyphered_text)
    return decyphered_text