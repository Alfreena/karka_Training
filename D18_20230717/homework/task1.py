my_resume={"name":"Alfreena","e-mail":"alfreenaj@gmail.com","mobile-no":9360074731,"soft_skill":["time management","problem solving"],"hard_skills":["writing","reading"],"educational_qualification":[{"course":"10","institution":"good shepherd matric hr sec.school","per_mark":"75","pass_out":2018},{"course":"12","institution":"evans matric hr sec","per_mark":"71","pass_out":2020},{"course":"B.Sc computersci","institution":"wcc","per_mark":"70","pass_out":"2023"}],"project":[{"project_name":"podcast","project_description":"A Redux-Inspired podcast app with dynamic themes in android"}],"experience":[{"company_name":"flow","position":"team management","years":1.5},{"company_name":"inbox","position":"team management","years":1.2},{"company_name":"color","position":"team management","years":2.1}],"hobbies":["games","gardening","handcraft"],"personal_detail":{"f_name":"joseph","m_name":"reeta","language_known":["tamil","english"],"dob":"june-19","gender":"female","martial_status":"single","address":{"door_no":"15b","place":"stk","dist":"kk"}}}
for i in my_resume['educational_qualification']:
    print(f"Course:{i['course']}\nSchool:{i['institution']}\nmark:{i['per_mark']}")
    print(f"Course=>{i['course']} and you passed out in {i['pass_out']}")

for i in my_resume['personal_detail']:
    print(f"{i}:{my_resume['personal_detail'][i]}")
for i in my_resume['personal_detail']['address']:
    print(f"{i}:{my_resume['personal_detail']['address'][i]}")
#for i in my_resume['experience']:
