alphabets=[chr(x) for x in range(65,91)]
sentences=["J.Q. Schwartz flung V.D. Pike my box","Two driven jocks help fax my big quiz.","New job: fix Mr Gluck's hazy TV, PD"]
for s in sentences:
    sen=s.upper()
    str_lis=[]
    for a in sen:
        if a not in str_lis:
           if a not in alphabets:
               pass
           else:
               str_lis.append(a)
        else:
            pass
    str_lis.sort()
    if alphabets==str_lis:
        print("String:'{}' is pangram".format(s))
    else:
        print("String:'{}' is not a pangram".format(s))
    
    
