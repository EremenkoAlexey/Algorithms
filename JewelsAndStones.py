"""
Даны две строки строчных латинских символов: строка J и строка S. 
Символы, входящие в строку J, — «драгоценности», входящие в строку S — «камни». 
Нужно определить, какое количество символов из S одновременно являются «драгоценностями». 
Проще говоря, нужно проверить, какое количество символов из S входит в J.
"""
import sys
 
j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()
 
result = 0
for ch in s:
    if ch in j:
        result += 1
 
print(result)
