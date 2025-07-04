a = int(input())
for i in range(a):
    s = input()
    if s.isspace():
        print(f'{i + 1}: COMMENT SHOULD BE DELETED')
    else:
        print(f'{i + 1}: {s}')

