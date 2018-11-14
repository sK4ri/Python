months_dict = {}

months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
days_in_months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

# for m, d in zip(months, days_in_months):
#     months_dict[m] = d

# print(months_dict)

# itt is hibás volt a példa megoldás

########################

months_dict = dict(zip(months, days_in_months))
print(months_dict)
