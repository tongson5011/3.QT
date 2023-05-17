with open('VietPhrase.txt', 'a', encoding='utf-8') as f:
    for i in range(15, 1500):
        f.write('\n')
        f.write(f'第{i}章=Chương {i}')
