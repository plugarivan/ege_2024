'''
Универсальное решение 13 задания ЕГЭ
'''
graf = {
    'А': "БДЕ",
    'Б': "В",
    'В': "ЖЗГ",
    'Г': "АБ",
    'Д': "И",
    'Е': "ДЗ",
    'Ж': "ЗЛ",
    'З': "ГЛ",
    'И': "ЕЗК",
    'К': "З",
    'Л': "К",
}
count = 0
def f(start, end ):
   global count
   last_city = start[-1]
   if last_city == end and len(start) > 1:
      count += 1
      return
   for town in graf[last_city]:
      if not town in start or town == end:
        f(start+town, end)

f('Г', 'Г')
print(count)
