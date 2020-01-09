d = {
    '1': '`',
    '2': '1',
    '3': '2',
    '4': '3',
    '5': '4',
    '6': '5',
    '7': '6',
    '8': '7',
    '9': '8',
    '0': '9',
    '-': '0',
    '=': '-',
    'W': 'Q',
    'E': 'W',
    'R': 'E',
    'T': 'R',
    'Y': 'T',
    'U': 'Y',
    'I': 'U',
    'O': 'I',
    'P': 'O',
    '[': 'P',
    ']': '[',
    '\\': ']',
    'S': 'A',
    'D': 'S',
    'F': 'D',
    'G': 'F',
    'H': 'G',
    'J': 'H',
    'K': 'J',
    'L': 'K',
    ';': 'L',
    '\'': ';',
    'X': 'Z',
    'C': 'X',
    'V': 'C',
    'B': 'V',
    'N': 'B',
    'M': 'N',
    ',': 'M',
    '.': ',',
    '/': '.',
}
def work(s):
    ans = ''
    for x in s:
        if x in d:
            ans += d[x]
        else:
            ans += x

    print(ans)


# -- author: lijw --
if __name__ == '__main__':
    while True:
        try:
            s = input()
        except EOFError:
            break
        work(s)
