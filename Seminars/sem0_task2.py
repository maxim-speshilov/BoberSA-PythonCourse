s = 'Это очень просто. Ножницы режут бумагу, бумага накрывает камень, камень давит ящерицу, ящерица травит Спока, Спок ломает ножницы, ножницы отрезают голову ящерице, ящерица ест бумагу, бумага ложится под Спока, Спок испаряет камень, и, как обычно, камень разбивает ножницы.'
key = ['бумаг', 'камен', 'ножниц', 'ящериц', 'спок']

d = {w[1]: (w[0], w[-1]) for w in [t.split() for t in s.lower().replace('.', ',').split(',')][:-1] if w[-1][:-1] in key}

print(d)