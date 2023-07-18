std=[{"name":"Alfreena","place":"stk","hobbies":["Planting","Web series","Games"],"sslc":{"tamil":80,"maths":88,"english":81,"science":89,"social":80}},{"name":"Akshaya","palce":"theroor","hobbies":["Music","Web series","Games"],"sslc":{"tamil":98,"maths":91,"english":92,"science":95,"social":99}},{"name":"Barathi","place":"thovalai","hobbies":["Eating","Sleeping","Games"],"sslc":{"tamil":90,"maths":81,"english":98,"science":86,"social":87}}]

def tot(std):
    for i in range(len(std)):
        total=std[i]['sslc']['tamil']+std[i]['sslc']['maths']+std[i]['sslc']['english']+std[i]['sslc']['science']+std[i]['sslc']['social']
        per=(total/500)*100
        if per>90:
            print(f"{std[i]['name']}, you are eligible for mathsbio")
        elif per>80 and per<90:
            print(f"{std[i]['name']}, you are eligible for comp science")
        elif per>75 and per<80 and std[i]['sslc']['maths']>98:
            print(f"{std[i]['name']}, you are eligible for mathsbio")
        elif per>70 and per<75 and std[i]['sslc']['maths']>98:
            print(f"{std[i]['name']}, you are eligible for comp science")
        print(total)
#print(tot(std))  
tota=tot(std)  