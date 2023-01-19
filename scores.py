import json

# WHY CAN I NOT COMMIT?!
class Scores():
    
    def most_tests(self):
        json_file =  json.load(open('data.json', 'r', encoding='utf-8'))
        most=0
        school=""
        for x in json_file['data']:
            if(x[10]!="s" and int(x[10])>int(most)):
                most=x[10]
                school=x[9]
        return school, int(most)

    def best_score(self):
        json_file =  json.load(open('data.json', 'r', encoding='utf-8'))
        highest=0
        school=""
        for x in json_file['data']:
            if(x[11]!="s" and x[12]!="s" and x[13]!="s"):
                current=int(x[11])+int(x[12])+int(x[13])
                if(current>highest):
                    highest=current
                    school=x[9]
        return school, highest

    def best_score_small(self):
        json_file =  json.load(open('data.json', 'r', encoding='utf-8'))
        highest=0
        school=""
        for x in json_file['data']:
            if(x[10]!="s" and int(x[10])<=50 and x[11]!="s" and x[12]!="s" and x[13]!="s"):
                current=int(x[11])+int(x[12])+int(x[13])
                if(current>highest):
                    highest=current
                    school=x[9]
        return school, highest

    def x_most_tests(self, x):
        json_file =  json.load(open('data.json', 'r', encoding='utf-8'))
        schools=[]
        nums=[]
        for a in range(x):
            most=0
            school=""
            for y in json_file['data']: 
                if(y[10]!="s" and int(y[10])>most and y[9] not in schools):
                    most=int(y[10])
                    school=y[9]
            schools.append(school)
            nums.append(most)
        combine=[(schools[z], nums[z]) for z in range(x)]
        return combine

    def x_highest_scores(self, x):
        json_file =  json.load(open('data.json', 'r', encoding='utf-8'))
        schools=[]
        nums=[]
        for a in range(x):
            most=0
            school=""
            for y in json_file['data']: 
                if(y[11]!="s" and y[12]!="s" and y[13]!="s" and y[9] not in schools):
                    current=(int(y[11])+int(y[12])+int(y[13]))
                    if(current>most):
                        most=current
                        school=y[9]
            schools.append(school)
            nums.append(most)
        combine=[(schools[z], nums[z]) for z in range(x)]
        return combine
