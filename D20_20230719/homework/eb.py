consumer_data={
    "consumer_name":"alfee",
    "eb_reading":[1100,1200,1350,1650,2050]
}
def cal_eb():
    reading=consumer_data['eb_reading']
    total=0
    for i in range(0,len(reading)-1):
        calculate=reading[i+1]-reading[i]
        print(f"Month:{i+1}\nUnits consumed:{calculate}")
        if calculate<100:
            cal=calculate
            print(f"Bill amount:{cal}")
            total+=cal
        elif calculate<=200 and calculate>=100:
            cal=2*(calculate)
            print(f"Bill amount:{cal}")
            total+=cal
        elif calculate<=500 and calculate>200:
            cal=5*(calculate)
            print(f"Bill amount:{cal}")
            total+=cal
        elif calculate<=1000 and calculate>500:
            cal=10*(calculate)
            print(f"Bill amount:{cal}")
            total+=cal
        elif calculate>1000:
            cal=14*(calculate)
            print(f"Bill amount:{cal}")
            total+=cal
        print(f"Total amount:{total}")
cal_eb()