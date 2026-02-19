''' Usage of DataFrame built-in function to arrange the 1D series with two lists and its elements with same number  to form a data with index value as default in the table format ''' 
example - 1 
import pandas as pd 
data = {
    "Districts":["Bagalkot", "Ballari", "Belagavi", "Bengaluru Rural", "Bengaluru Urban", "Bidar", "Chamarajanagar", "Chikkaballapura", "Chikkamagaluru", "Chitradurga", "Dakshina Kannada", "Davanagere", "Dharwad", "Gadag", "Hassan"," Haveri", "Kalaburagi", "Kodagu", "Kolar", "Koppal", "Mandya", "Mysuru", "Raichur", "Ramanagara", "Shivamogga", "Tumakuru", "Udupi", "Uttara Kannada", "Vijayapura", "Yadgir"],
    "Pincode":[587101, 583101, 590001, 562110, 560001, 585401, 571313, 562101, 577101, 577501, 575001, 577001, 580001, 582101, 573201, 581110, 585102, 571201, 563101, 583231, 571401, 570001, 584101, 562159, 577201, 572101, 576101, 581301, 586101, 585201]
}
dataform = pd.DataFrame(data)
print(dataform)

''' Output  
           Districts  Pincode
0           Bagalkot   587101
1            Ballari   583101
2           Belagavi   590001
3    Bengaluru Rural   562110
4    Bengaluru Urban   560001
5              Bidar   585401
6     Chamarajanagar   571313
7    Chikkaballapura   562101
8     Chikkamagaluru   577101
9        Chitradurga   577501
10  Dakshina Kannada   575001
11        Davanagere   577001
12           Dharwad   580001
13             Gadag   582101
14            Hassan   573201
15            Haveri   581110
16        Kalaburagi   585102
17            Kodagu   571201
18             Kolar   563101
19            Koppal   583231
20            Mandya   571401
21            Mysuru   570001
22           Raichur   584101
23        Ramanagara   562159
24        Shivamogga   577201
25          Tumakuru   572101
26             Udupi   576101
27    Uttara Kannada   581301
28        Vijayapura   586101
29            Yadgir   585201 '''

import pandas as ps 
student_data = {
  "regno":["U01BP24S0001","U01BP24S0002" , "U01BP24S0003" , "U01BP24S0004" ,"U01BP24S0005"],
  "section":['A', 'B' , 'C' , 'D' ]
}
student_table = ps.DataFrame(student_data)
print(student_table)

  
