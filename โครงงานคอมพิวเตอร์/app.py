
from flask import Flask, render_template, request

# Keyboard layout mappings (eng_to_thai, thai_to_eng)
eng_to_thai = {
    '1':'ๅ', '!':'+',
    '2':'/', '@':'๑',
    '3':'-', '#':'๒',
    '4':'ภ', '$':'๓',
    '5':'ถ', '%':'๔',
    '6':'ุ', '^':'ู',
    '7':'ึ', '&':'฿',
    '8':'ค', '*':'๕',
    '9':'ต', '(':'๖',
    '0':'จ', ')':'๗',
    '-':'ข', '_':'๘',
    '=':'ช', '+':'๙',
    'q':'ๆ', 'Q':'๐',
    'w':'ไ', 'W':'"',
    'e':'ำ', 'E':'ฎ',
    'r':'พ', 'R':'ฑ',
    't':'ะ', 'T':'ธ',
    'y':'ั', 'Y':'ํ',
    'u':'ี', 'U':'๊',
    'i':'ร', 'I':'ณ',
    'o':'น', 'O':'ฯ',
    'p':'ย', 'P':'ญ',
    '[':'บ', '{':'ฐ',
    ']':'ล', '}':',',
    'a':'ฟ', 'A':'ฤ',
    's':'ห', 'S':'ฆ',
    'd':'ก', 'D':'ฏ',
    'f':'ด', 'F':'โ',
    'g':'เ', 'G':'ฌ',
    'h':'้', 'H':'็',
    'j':'่', 'J':'๋',
    'k':'า', 'K':'ษ',
    'l':'ส', 'L':'ศ',
    ';':'ว', ':':'ซ',
    "'":'ง', '"':'.',
    'z':'ผ', 'Z':'(',
    'x':'ป', 'X':')',
    'c':'แ', 'C':'ฉ',
    'v':'อ', 'V':'ฮ',
    'b':'ิ', 'B':'ฺ',
    'n':'ื', 'N':'์',
    'm':'ท', 'M':'?',
    ',':'ม', '<':'ฒ',
    '.':'ใ', '>':'ฬ',
    '/':'ฝ', '?':'ฦ'
}

thai_to_eng = {thai: eng for eng, thai in eng_to_thai.items()} 

# Language detection and conversion functions (detect_language, correct_language)
def detect_language(text):
    thai_chars = set(thai_to_eng.keys())
    eng_chars = set(eng_to_thai.keys())
    thai_count = sum(char in thai_chars for char in text)
    eng_count = sum(char in eng_chars for char in text)

    if thai_count > eng_count:
        return 'thai'
    else:
        return 'english'

def correct_language(input_text):
    lang = detect_language(input_text)
    if lang == 'english':
        corrected_text = ''.join(eng_to_thai.get(char, char) for char in input_text)
    else:
        corrected_text = ''.join(thai_to_eng.get(char, char) for char in input_text)
    return corrected_text

# Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        output_text = correct_language(input_text)
        return render_template('index.html', input_text=input_text, output_text=output_text)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
