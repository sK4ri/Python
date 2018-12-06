numbers = ", ".join(str(n) for n in range(1, 11))
print(numbers)

################

calendar = []
(Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec) = range(12)
(W1, W2, W3, W4) = range(4)

for months in range(12):
    month = []

    for weeks in range(4):
        month.append([])

    calendar.append(month)

calendar[Jul][W2].append("Get a degree!")
print(calendar[Jul][W2])

# gave up here
