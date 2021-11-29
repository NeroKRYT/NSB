a = input('Type numbers: ')
a = list(a.split(' '))
a = [int(x) for x in a]
a.sort(reverse=True)

m = {'1': 0, '2': 0, '3': 0}

s = 0  # Площадь
p = 0  # Периметр

for i in range(2, len(a)):
    if a[i - 1] + a[i] > a[i - 2] and a[i - 2] + a[i] > a[i - 1] and a[i - 2] + a[i - 1] > a[i]:
        p = (a[i] + a[i - 1] + a[i - 2]) / 2
        s = (p * (p - a[i]) * (p - a[i - 1]) * (p - a[i - 2])) ** 0.5

        m['1'] = a[i]
        m['2'] = a[i - 1]
        m['3'] = a[i - 2]
        break

if s > 0:
    print("Maximum area: ", a)
    print("Sides: ", m)
else:
    print("No way")