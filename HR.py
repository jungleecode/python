
Sample input = 'AABCAAADA'
Sample output = 'AB', 'CA', 'AD'

string = 'AABCAAADA'

n = len(string)
k = 3
n_t = n // k

subs = ''
sub_strings = []
c = 0
for i in range(n_t):
    subs += ''.join(string[i+c:k+i+c])
    c = c + k-1
    ss = ''
    for ch in subs:
        if ch not in ss:
            ss += ch
    sub_strings.append(ss)
    subs = ''
    print(ss)
