def time(years,weeks,days):
    d=years*365+weeks*7+days
    h=d*24
    m=h*60
    s=m*60
    return (d,h,m,s)

q= time(15,7,5)
print(q)
