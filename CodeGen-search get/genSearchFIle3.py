import  simi
nl_list = []
code_list = []
# filePath = 'HS-B/test66/'


with open(r'ATIS/train_trans.txt','r') as file:
# with open(r'HS-B/train_trans.txt','r') as file:
    lines = file.readlines()
    count = 0

    for i in range(len(lines)):
        # if(count > 65):
        #     break
        if(i % 9 == 0):
            nl_list.append(lines[i])
        if (i % 9 == 6):
            code_list.append(lines[i])

test_nl_list = []
with open(r'ATIS/input.txt','r') as file:        
# with open(r'HS-B/input.txt','r') as file:          
    lines = file.readlines()
    count = 0
    for i in range(len(lines)):
        # if (i % 9 == 0):
        test_nl_list.append(lines[i])


for i, sentence in enumerate(test_nl_list):
    score, re_sententce, index = simi.my_ranker(sentence, nl_list, False)
    f = open(filePath + str(i) + '-testInfoMin.txt', 'w')
    # f = open(filePath + str(i) + '-similar.txt', 'w')
    f.write(nl_list[index])
    f.close()
    f = open(filePath + str(i) + '-rule.txt', 'w')
    f.write(code_list[index])
    f.close()
    # print(sentence)
    # print(re_sententce)
    # print(score)
    # break

