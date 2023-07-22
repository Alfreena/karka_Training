#Cricket Player Statistics
player=[{"name":"dhoni","centuries":16,"half_centuries":20,"wicket":26,"hat_trick":6,"top_batting":[125,118,150]},{"name":"maliga","centuries":13,"half_centuries":19,"wicket":19,"hat_trick":4,"top_batting":[123,101,108]},{"name":"warner","centuries":9,"half_centuries":21,"wicket":20,"hat_trick":6,"top_batting":[120,117,103]},{"name":"smith","centuries":8,"half_centuries":13,"wicket":24,"hat_trick":4,"top_batting":128},{"name":"bravo","centuries":13,"half_centuries":17,"wicket":25,"hat_trick":7,"top_batting":[102,90,110]}]
i=0
for i in player:
    if (i['centuries'])>=10:
        print(f"{i['name']}")   
    if (i['hat_trick'])>=5:
            print(f"{i['name']}")   
# centu=cent(player)
# trick=hat(player)

def cent(player):
    for i in range(len(player)):
        if (player[i]['centuries'])>=10:
            print(f"{player[i]['name']}")   
centu=cent(player)
print("Player with more than 5 hat trick")
def hat(player):
    for i in range(len(player)):
        if (player[i]['hat_trick'])>=5:
            print(f"{player[i]['name']}")   
trick=hat(player)
#batting=0
#def top(player,batting):
#    for i in range(len(player)):
#        if(player[i]['top_batting'])>=batting:
#            batting=(player[i]['top_batting'])
#    print(batting)
#score=top(player,batting)
#def 
high_score=[0]
for i in range(len(player)):
    if(player[i]['top_batting'])>=high_score:
        high_score=player[i]['top_batting']
        print(high_score)
def score(player):
    for i in range(len(player)):
        return max(player[i]['top_batting'])
top=score(player)        
print(score(player))

