#daydayup version 2
dayfactor=0.005
dayup=(1+dayfactor)**365
daydown=(1-dayfactor)**365
print("每天多努力{:.3f}向上{:.3f},少努力{:.3f}向下{:.3f}".format(dayfactor,dayup,dayfactor,daydown))