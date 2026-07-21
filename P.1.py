data = [
    ['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
    ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
    ['Rainy','Cold','High','Strong','Warm','Change','No'],
    ['Sunny','Warm','High','Strong','Cool','Same','Yes'],
    ['Rainy','Warm','Normal','Weak','Warm','Same','No'],
    ['Sunny','Warm','Normal','Weak','Warm','Same','Yes']
]

h = ['0'] * (len(data[0]) - 1)

for row in data:
    if row[-1] == 'Yes':
        if h[0] == '0':
            h = row[:-1]
        else:
            for i in range(len(h)):
                if h[i] != row[i]:
                    h[i] = '?'
    print(h)

print("Final Hypothesis:", h)
data = [
    ['High','Good','Permanent','Yes','Young','Yes'],
    ['High','Good','Permanent','No','Middle','Yes'],
    ['Low','Poor','Temporary','No','Young','No'],
    ['Medium','Good','Permanent','Yes','Middle','Yes'],
    ['High','Average','Temporary','Yes','Old','No'],
    ['High','Good','Permanent','Yes','Middle','Yes']
]

h = ['0'] * (len(data[0]) - 1)

for row in data:
    if row[-1] == 'Yes':
        if h[0] == '0':
            h = row[:-1]
        else:
            for i in range(len(h)):
                if h[i] != row[i]:
                    h[i] = '?'
    print(h)

print("Final Hypothesis:", h)
data = [
    ['High','Good','Yes','Good','High','Yes'],
    ['High','Excellent','Yes','Good','High','Yes'],
    ['Medium','Average','No','Average','Medium','No'],
    ['High','Good','Yes','Excellent','High','Yes'],
    ['Low','Poor','No','Average','Low','No'],
    ['High','Good','Yes','Good','Medium','Yes']
]

h = ['0'] * (len(data[0]) - 1)

for row in data:
    if row[-1] == 'Yes':
        if h[0] == '0':
            h = row[:-1]
        else:
            for i in range(len(h)):
                if h[i] != row[i]:
                    h[i] = '?'
    print(h)

print("Final Hypothesis:", h)
data = [
    ['High','Good','Yes','Good','High','Yes'],
    ['High','Excellent','Yes','Good','High','Yes'],
    ['Medium','Average','No','Average','Medium','No'],
    ['High','Good','Yes','Excellent','High','Yes'],
    ['Low','Poor','No','Average','Low','No'],
    ['High','Good','Yes','Good','Medium','Yes']
]

h = ['0'] * (len(data[0]) - 1)

for row in data:
    if row[-1] == 'Yes':
        if h[0] == '0':
            h = row[:-1]
        else:
            for i in range(len(h)):
                if h[i] != row[i]:
                    h[i] = '?'
    print(h)

print("Final Hypothesis:", h)
data = [
    ['Yes','Yes','Yes','Yes','Yes','Positive'],
    ['Yes','Yes','No','Yes','Yes','Positive'],
    ['No','Yes','Yes','No','No','Negative'],
    ['Yes','Yes','Yes','No','Yes','Positive'],
    ['No','No','Yes','Yes','No','Negative'],
    ['Yes','Yes','No','No','Yes','Positive']
]

h = ['0'] * (len(data[0]) - 1)

for row in data:
    if row[-1] == 'Positive':
        if h[0] == '0':
            h = row[:-1]
        else:
            for i in range(len(h)):
                if h[i] != row[i]:
                    h[i] = '?'
    print(h)

print("Final Hypothesis:", h)
data = [
    ['Sunny','Warm','Normal','Yes'],
    ['Sunny','Warm','High','Yes'],
    ['Rainy','Cold','High','No'],
    ['Sunny','Warm','High','Yes']
]
h = ['0'] * (len(data[0]) - 1)
for row in data:
    if row[-1] == 'Yes':
        if h[0] == '0':
            h = row[:-1]
        else:
            for i in range(len(h)):
                if h[i] != row[i]:
                    h[i] = '?'
    print(h)
print("Final Hypothesis:", h)


