consumer_data={
    "consumer_name":"alfee",
    "eb_reading":[1100,1200,1350,1650,2050]
}
eb_detail=[]
def cal_eb(consumer_data):
    reading=consumer_data['eb_reading']
    for i in range(0,len(reading)-1):
        calculate=reading[i+1]-reading[i]
        detail=print(f"Month:{i+1}\nUnits consumed:{calculate}")
        if calculate<100:
            cal=calculate
            bill=print(f"Bill amount:{cal}")
        elif calculate<=200 and calculate>=100:
            cal=2*(calculate)
            bill=print(f"Bill amount:{cal}")
        elif calculate<=500 and calculate>200:
            cal=5*(calculate)
            bill=print(f"Bill amount:{cal}")
        elif calculate<=1000 and calculate>500:
            cal=10*(calculate)
            bill=print(f"Bill amount:{cal}")
        elif calculate>1000:
            cal=14*(calculate)
            bill=print(f"Bill amount:{cal}")
        eb={'month':i+1,
            'unit_consumed':calculate,
            'bill_amount':cal}
        eb_detail.append(eb)
cal_eb(consumer_data)
listtostring=str(eb_detail)
print(listtostring)
print(type(listtostring))
name=consumer_data['consumer_name']
file=open(f"/home/alfee/karka/D21_20230720/practice/{name}",'w')
file.write(listtostring)
file.close()
file=open(f"/home/alfee/karka/D21_20230720/practice/{name}",'r')