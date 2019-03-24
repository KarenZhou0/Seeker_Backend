import csv
import random

lst_gender = ["female","male"]
lst_language = ["Spanish","Italian","English", "French", "German", "Japanese", "Korean", "Malay", "Chinese"]
lstS = ['standard','Castilian', 'Andalusian', 'Murcian', 'Canarian', 'Llanito', 'Latin American Spanish', 'Rioplatense Spanish', 'Caribbean Spanish', 'Equatoguinean Spanish', 'Coda']
lstI = ['standard','Tuscan','Neapolitan','Venetian','Sicilian','Romanesco']
lstE = ['standard','Singlish', 'General American', 'Canadian', 'Bermudian','Australian','British']
lstF = ['standard','Parisian', 'Marseillais','Meriodonal','Northern France']
lstG = ['standard','Swiss German', 'Austrian German', 'The Bavarian Dialect', 'The upper Saxon Dialect','The Berlin Dialect', 'Low German']
lstJ = ['standard', 'Hakata Ben', 'Osaka Ben', 'Hiroshima Ben', 'Kyoto Ben', 'Nagoya Ben', 'Hokkaido Ben']
lstK = ['standard','Chungcheong','Gangwon','Gyeongsang','Jeolla','Jeju']
lstM = ['standard', 'Bangka','Bangkok','Banjar','Brunei', 'Sarawak', 'Pontianak', 'Pahang','Musi']
lstC = ['Mandarin', 'Cantonese','Hakka','Wu','Min','Xiang','Jin','Hui']
lst_proficiency = ['novice','intermediate','fluent','native']
lst_country = ['Spain','Italy','US','France','Germany','Japan','South Korea','Malaysia','China']
lst_occupation = ['teacher','banker','social worker','unemployed','student','volunteer','freelancer','engineer','writer','artist']
lst_interests = [['dance','digital arts','performing arts','painting','jazz dance','typography','photography','video editing'],\
                 ['reading','literature','science fiction','fiction','novel'],\
                 ['cooking','baking'],\
                 ['cycling','gymnastics','boxing','hiking','volleyball','fishing','golfing','swimming','tennis'],\
                 ['granola','BBQ','salad','Asian Cuisine'],\
                 ['jazz','kpop','classical','r&b']]

interest_div = []


with open('data.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['user','age','language','dialect','proficiency level','language to learn','dialect to learn','proficiency level so far','country','occupation','interests'])

    for i in range(30):
        user = "user"+str(i+1)
        gender = random.choice(lst_gender)
        age = random.randint(18,50)
        proficiency_index = 0

        x = random.randint(0,len(lst_language)-1)
        language = lst_language[x]
        y = random.randint(0,len(lst_country)-1)
        country = lst_country[y]
        occupation = random.choice(lst_occupation)
        a = random.randint(0,len(lst_interests)-1)
        interest_div.append(a)
        interests = random.choice(lst_interests[a])

        if age >= 30:
            proficiency_index += 1
        if x == y:
            proficiency_index = 3
            proficiency = lst_proficiency[3]
        else:
            proficiency_index = random.randint(0,len(lst_proficiency)-1)
            proficiency = lst_proficiency[proficiency_index]

        if x == 0:
            dialect = random.choice(lstS)
        elif x == 1:
            dialect = random.choice(lstI)
        elif x == 2:
            dialect = random.choice(lstE)
        elif x == 3:
            dialect = random.choice(lstF)
        elif x == 4:
            dialect = random.choice(lstG)
        elif x == 5:
            dialect = random.choice(lstJ)
        elif x == 6:
            dialect = random.choice(lstK)
        elif x == 7:
            dialect = random.choice(lstM)
        else:
            dialect = random.choice(lstC)

        z = x
        while z == x:
            z = random.randint(0,len(lst_language)-1)
        language1 = lst_language[z]

        if z == 0:
            dialect1 = random.choice(lstS)
        elif z == 1:
            dialect1 = random.choice(lstI)
        elif z == 2:
            dialect1 = random.choice(lstE)
        elif z == 3:
            dialect1 = random.choice(lstF)
        elif z == 4:
            dialect1 = random.choice(lstG)
        elif z == 5:
            dialect1 = random.choice(lstJ)
        elif z == 6:
            dialect1 = random.choice(lstK)
        elif z == 7:
            dialect1 = random.choice(lstM)
        else:
            dialect1 = random.choice(lstC)

        proficiency1 = random.choice(lst_proficiency[:(proficiency_index + 1)])

        filewriter.writerow([user,age,language,dialect,proficiency,language1,dialect1,proficiency1,country,occupation,interests])


