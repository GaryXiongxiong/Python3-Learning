#daydayup version 3
dayfactor = 0.01
dayup = 1
for i in range(365):
    if i % 7 < 5:
        dayup = dayup*(1+dayfactor)
    else:
        dayup = dayup*(1-dayfactor)
print("工作日多努力{:.3f}向上{:.3f}".format(dayfactor,dayup))