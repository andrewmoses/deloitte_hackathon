import sys
import pandas as pd

file_path = sys.argv[1]
f = open(file_path,'r')
raw = f.read()
line_blocks = raw.split("\n\n")
name = []
email = []
c_lines = []
for each in line_blocks[:-2]:
    chunk = each.strip()
    b_ch = chunk.split("\n")
    a_line = b_ch[0].strip()
    a_l_list = a_line.split("<")
    print('name: ',a_l_list[0].strip())
    name.append(a_l_list[0].strip())
    emailpart = a_l_list[1].strip()
    emailalone = emailpart.replace('>:','')
    print('email: ',emailalone)
    email.append(emailalone)
    
#     print("author: ", )
    f_line = b_ch[5].strip()
    f_lines_list = f_line.split(" ")
#     print(f_lines_list)
    print("number of lines: ", f_lines_list[2].strip())
    c_lines.append(f_lines_list[2].strip())
    
    print("\n")

new_dict = {}
new_dict['author'] = name
new_dict['email'] = email
new_dict['lines_changed'] = c_lines


df = pd.DataFrame.from_dict(new_dict)
df.to_csv("../outputs/git_test.csv", index=False)