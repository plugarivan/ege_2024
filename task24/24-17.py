'''
Текстовый файл 24-241.txt состоит не более чем из 10**6 символов и содержит только латинские буквы A, B, C, D, E, F, O. Определите длину самой короткой цепочки символов, которая начинается и заканчивается буквой E, между двумя последовательными буквами E содержит ровно две буквы B, а между этими буквами B – более 5 букв A.
'''
s = open('files/24-241.txt').readline()
minLen = 10 ** 10
for pod in s.split('E')[:-1]:
    if pod.count('B') == 2:
        p1 = pod.find('B')
        p2 = pod.rfind('B')
        if pod[p1 + 1:p2].count('A') > 5:
            minLen = min(minLen, len(pod))
print(minLen + 2)
