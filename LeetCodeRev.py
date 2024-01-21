import random

# data = {'Arrays_Hashing' : [217, 242, 1929, 1299, 392, 58,1,14,49,118,27,929,205,605,169,496,724,303,448,1189,290,705,706,912,347,238,36,128,],
#          'Two_Pointer' : [],
#          'Sliding_Window' : [],
#          'Stack' : [20,682,225,2390,946,735,739,901,853,71,396,402,1047,1209,456,895,84,22,],
#          'Binary_Search' : [704,35,374,441,977,367,69,540,1011,162,2300,74]}

# Listing all solved questions based on Topics
data = {'Arrays_Hashing' : [217, 242, 1929, 1299, 392, 58,1,14,49,118,27,929,205,605,169,496,724,303,448,1189,290,705,706,912,347,238,36,128,],
         'Two_Pointer' : [],
         'Sliding_Window' : [],
         'Stack' : [20,682,225,2390,946,735,739,901,853,71,396,402,1047,1209,456,895,84,22,],
         'Binary_Search' : [704,35,374,441,977,367,69,540,1011,162,2300,74,]}

topics = list(data.keys())

# hold the questions selected for revision 
que = {}

# Number of Questions you want to Revise
questions = 3
while questions != 0:
    topic = random.choice(topics)
    if len(data[topic]) == 0:
        # if the topic has no more questions
        topics.remove(topic)
        continue
    else:
        if topic not in que:
            que[topic] = []
        selected = random.choice(data[topic])
        que[topic].append(selected)
        # once Selected remove from data to avoid getting duplicate question
        data[topic].remove(selected)
        questions -= 1

print("Solve the Below questions")
print("*************************")
print(que)
