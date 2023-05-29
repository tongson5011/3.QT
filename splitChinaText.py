with open('Names.txt', 'r', encoding='utf-8') as f:
    names = f.read()

names_dict = {}
for name_line in names.split('\n'):
    if name_line:
        name_line = name_line.split('=')
        if len(name_line) >= 2:
            names_dict[name_line[0]] = name_line[1]

with open('VietPhrase.txt', 'r', encoding='utf-8') as f:
    vietPhrases = f.read()

vietPhrase_dict = {}
for name_line in vietPhrases.split('\n'):
    if name_line:
        name_line = name_line.split('=')
        if len(name_line) >= 2:
            vietPhrase_dict[name_line[0]] = name_line[1]

def find_dict(default_text =''):
    # default_text = '一艘小木舟正沿着河道的一条狭窄支流缓缓前行'
    current_text = default_text
    start = 0
    result = []
    while True:
        if len(current_text) == 0:
            break
        if names_dict.get(current_text) is not None:
            result.append([current_text, names_dict.get(current_text)])
            start = start + len(current_text)
            current_text = default_text[start:]
        elif vietPhrase_dict.get(current_text) is not None:
            result.append([current_text, vietPhrase_dict.get(current_text)])
            start = start + len(current_text)
            current_text = default_text[start:]
        else:
            if len(current_text) == 1:
                # if not current_text.isspace():
                #     result.append([current_text,''])
                start = start + 1
                current_text = default_text[start:]
            else:
                current_text = current_text[:len(current_text)-1]

    return result


# result = find_dict('第1章 声入桃源')
# print(result)