education_detail=[
    {"study":"B.Sc computerscience",
    "Institution":"Wcc",
    "sem_marks":[{"sem_name":1,
                  "sub_name":["Cloudcomputing","Big data","RDBMS"],
                  "sem_grade":"A"
                  },
                  {"sem_name":2,
                  "sub_name":["Datascience","Java","Php"],
                  "sem_grade":"A"
                  },
                  {"sem_name":3,
                  "sub_name":["Digital image","Python","Mysql"],
                  "sem_grade":"B"
                  },
                  {"sem_name":4,
                  "sub_name":["project","javascript","ML"],
                  "sem_grade":"B+"
                  }]
     },
    {"study":"M.Sc computerscience",
    "Institution":"C.S.I",
    "sem_marks":[{"sem_name":1,
                  "sub_name":["Data structure","","RDBMS"],
                  "sem_grade":"A+"
                  },
                  {"sem_name":2,
                  "sub_name":["Datascience","Java","Php"],
                  "sem_grade":"B+"
                  },
                  {"sem_name":3,
                  "sub_name":["Digital image","Python","Mysql"],
                  "sem_grade":"B"
                  },
                  {"sem_name":4,
                  "sub_name":["project","javascript","ML"],
                  "sem_grade":"A"
                  }]
     }
]
for item in education_detail:
    print(item['study'])
    for item in 