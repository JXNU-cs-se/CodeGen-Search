import  simi
nl_list = []
code_list = []
# filePath = 'HS-B/train529/'


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

for i, sentence in enumerate(nl_list):
    score, _, index = simi.my_ranker(sentence, nl_list, False)
    f = open(filePath + str(i) + '-testInfoMin.txt', 'w') # 相似NL自然语言
    f.write(nl_list[index])
    f.close()
    f = open(filePath + str(i) + '-rule.txt', 'w')  #相似code(AST规则序列形式)
    f.write(code_list[index])
    f.close()
    # break

