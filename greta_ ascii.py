def gen_ascii():
    height = 33
    width  = 45

    for row in range(height):
        for column in range (width):
            char = " "
            if row ==0:
                if column == 17:
                    char = "="
                elif column ==18:
                    char = "*"
                elif column in (19,20):
                    char = "%"
                elif column ==21:
                    char = "#" 
                elif 22<= column <= 25:
                    char = "%" 
                elif column == 26:
                    char = "#" 
                elif column == 27:
                    char = "="
                elif column == 28:
                    char = "-"
                elif column == 29:
                    char = ":"
                elif column == 30:
                    char = ":"
            if row == 1:
                if column == 16:
                    char = "*"  
                elif column in (17,18):
                    char = "#"
                elif column in (19,20):
                    char = "%"
                elif column == 21:
                    char = "#"
                elif 22<= column <= 29:
                    char = "*"
            if row == 2:
                if column == 10:
                    char = "*"
                elif 11<= column <=14:
                    char = "%"
                elif column in (15,16):
                    char = "#"
                elif column == 17:
                    char = "*"
                elif column == 18:
                    char = "+"
                elif column == 19:
                    char = "*"
                elif 20<= column <= 22:
                    char = "+"
                elif column in (23,24):
                    char = "*"
                elif column in (25,26):
                    char = "+"
                elif column == 27:
                    char = "*"
                elif column in (28,29):
                    char = "#"
                elif column in  (30,31):
                    char = "%"
                elif 32 <= column <= 34:
                    char = "#"
            if row == 3:
                if 10<= column <=15:
                    char = "%"
                elif column in (16,17):
                    char = "#"
                elif column == 18:
                    char = "*"
                elif 19<= column <= 21:
                    char = "+"
                elif column == 22:
                    char = "="
                elif column == 23:
                    char = "+"
                elif column in (24,25):
                    char = "*"
                elif 26<= column <= 28:
                    char = "+"
                elif column == 29:
                    char = "*"
                elif 30<= column <=35:
                    char = "#"
            if row == 4:
                if column == 8:
                    char = "*"
                elif column in (9,10):
                    char = "%"
                elif column == 11:
                    char = "#"
                elif 12<= column <= 14 :
                    char = "%"
                elif column == 15:
                    char = "#"
                elif column == 16:
                    char = "*"
                elif column == 17:
                    char = "+"
                elif column in (18,19):
                    char = "="
                elif column == 20:
                    char = "-"
                elif column == 21:
                    char = "="
                elif column == 22:
                    char = "+"
                elif column in (23,24):
                    char = "*"
                elif column == 25:
                    char = "+"
                elif column == 26:
                    char = "*"
                elif column in (27,28):
                    char = "+"
                elif 29<= column <= 31:
                    char = "*"
                elif 32<= column <= 35:
                    char = "#"
                elif column == 36:
                    char = "%" 
            if row == 5:
                if column == 7:
                    char = "*"
                elif column in (8,9):
                    char = "#"
                elif 10<= column <= 12:
                    char = "*"                                                                                                                                 
                elif column == 13:
                    char = "#"
                elif column == 14:
                    char = "*"
                elif column == 15:
                    char = "+"
                elif column == 16 :
                    char = "="
                elif 17<= column <=19:
                    char = "-"
                elif column == 20:
                    char = ":"
                elif 21<= column <=23:
                    char = "-"
                elif column == 24:
                    char = "="
                elif column in (25,26):
                    char = "+"
                elif column in (27,28):
                    char = "="
                elif column in (29,30):
                    char = "+"
                elif 31<= column <=34:
                    char = "#"
                elif column in (35,36):
                    char = "%"
                elif column == 37:
                    char = "#"
                elif column == 38:
                    char = "%"
            if row == 6:
                if column in (7,8):
                    char = "*"
                elif column == 9:
                    char = "+"
                elif  10<= column <= 12:
                    char = "*"
                elif  column == 13:
                    char = "+"    
                elif column in (14,15):
                    char = "="
                elif  16<= column <= 19:
                    char = "-"
                elif  20<= column <=25:
                    char = ":"
                elif column == 26:
                    char = "-"
                elif column in (27,28):
                    char = "="
                elif column == 29:
                    char = "+"
                elif column in (30,31):
                    char = "*"
                elif 32<= column <=34:
                    char = "#"
                elif 35<= column <=37:
                    char = "%"
                elif column in (38,39):
                    char = "#"
            if row == 7:
                if column == 7 :
                    char = "+"
                elif column == 8:
                    char = "*"
                elif column in (9,10):
                    char = "#"
                elif column == 11:
                    char = "*"
                elif 12<= column <=15:
                    char = "="
                elif 16<= column <=19:
                    char = "-"                             
                elif 20<= column <=29:
                    char = ":"
                elif column == 30:
                    char = "="
                elif column in (31,32):
                    char = "*"
                elif column in (33,34):
                    char = "#"
                elif 35<= column <=37:
                    char = "%"
                elif column in (38,39):
                    char = "#"
                elif column == 40:
                    char = "+"
            if row == 8:
                if column == 7:
                    char = "="
                elif column == 8:
                    char = "#"
                elif column == 9:
                    char =  "%"
                elif column == 10:
                    char = "*"
                elif column in (11,12):
                    char = "+"
                elif column in (13,14):
                    char = "="
                elif 15<= column <=19:
                    char = "-"
                elif 20<= column <=31:
                    char = ":"
                elif column == 32:
                    char = "-"
                elif column == 33:
                    char = "*"
                elif column in (34,35):
                    char = "#"
                elif 36<= column <=39:
                    char = "%"
                elif column == 40:
                    char = "*" 
            if row == 9:
                if column == 7:
                    char = "+"
                elif column == 8:
                    char = "%"
                elif column == 9:
                    char = '#'
                elif column ==10:
                    char = "*"
                elif column in (11,12):
                    char = "+"
                elif column in (13,14):
                    char = "="
                elif 15<= column <=19:
                    char = "-"
                elif 20<= column <=32:
                    char = ":"
                elif column in (33,34):
                    char = "-"
                elif column ==35:
                    char = "*"
                elif column in (36,37):
                    char = "#"
                elif column in (38,39):
                    char = "%"
                elif column == 40:
                    char = "#"
            if row == 10:
                if column == 6:
                    char = "*"
                elif column == 7:
                    char = "="
                elif column == 8:
                    char = "#"
                elif column in (9,10):
                    char = "*"
                elif column in (11,12):
                    char = "+"
                elif column ==13:
                    char = "="
                elif 14<= column <=18:
                    char = "-"
                elif 19<= column <=33:
                    char = ":"
                elif column in (34,35):
                    char = "-"
                elif column == 36:
                    char = "="
                elif column == 37:
                    char = "*"
                elif column == 38:
                    char = "#"
                elif column in (39,40):
                    char = "%"
                elif column == 41:
                    char = "+"
            if row == 11:
                if column == 5:
                    char = "+"
                elif column == 6:
                    char = "#"
                elif column == 7:
                    char = "="
                elif 8<= column <=11:
                    char = "*"
                elif column == 12:
                    char = "+"
                elif column in (13,14):
                    char = "*"
                elif column == 15:
                    char = "+"
                elif column == 16:
                    char = "*"
                elif column == 17:
                    char = "="
                elif column == 18:
                    char = "-"
                elif column in (19,20):
                    char = ":"
                elif 21<= column <=24:
                    char = "-"
                elif 25<= column <=33:
                    char = ":" 
                elif 34<= column <=36:
                    char = "-"
                elif column == 37:
                    char = "+"
                elif column == 38:
                    char = "#"
                elif column == 39:
                    char = "*"
                elif column == 40:
                    char = "#"
                elif column == 41:
                    char = "+"
            if row == 12:
                if column in (4,5):
                    char = "*"
                elif column == 6:
                    char = "="
                elif 7<= column <=9:
                    char = "+"
                elif 10<= column <=12:
                    char = "*"
                elif column == 13:
                    char = "+"
                elif column in (14,15):
                    char = "="
                elif column == 16:
                    char = "+"
                elif column in (17,18):
                    char = "*"
                elif column == 19:
                    char = "+"
                elif column == 20:
                    char = "="
                elif 21<= column <=27:
                    char = "-"
                elif 28<= column <=31:
                    char = "="
                elif 32<= column <=35:
                    char = "-"
                elif column == 36:
                    char = "*"
                elif column == 37:
                    char = "#"
                elif column == 38:
                    char = "*"
                elif column == 39:
                    char = "="
                elif 40<= column <=42:
                    char = ":"
            if row == 13:
                if column == 3:
                    char = "*"
                elif column in (4,5):
                    char = "#"
                elif column == 6:
                    char = "*"
                elif column == 7:
                    char = "="
                elif column == 8:
                    char = "+"
                elif column in (9,10):
                    char ="="
                elif column == 11:
                    char = "+" 
                elif column == 12:
                    char = "*"
                elif column in (13,14):
                    char = "="
                elif column == 15:
                    char = "-"
                elif column == 16:
                    char = "="
                elif 17<= column <=19:
                    char = "+"
                elif column == 20:
                    char = "="
                elif column == 21:
                    char = "-"
                elif column == 22:
                    char = ":"
                elif column == 23:
                    char = "-"
                elif column in (24,25):
                    char = "="
                elif column == 26:
                    char = "*"
                elif column == 27:
                    char = "+"
                elif column == 28:
                    char = "*"
                elif 29<= column <=31:
                    char = "="
                elif 32<= column <=35:
                    char = "-"
                elif column in (36,37):
                    char = "+"
                elif column == 38:
                    char = "="
                elif column in (39,40):
                    char = "-"
                elif column in (41,42):
                    char = ":"
            if row == 14:
                if column in (2,3):
                    char = "+"
                elif 4<= column <=7:
                    char = "*"
                elif column in (8,9):
                    char = "="
                elif 10<= column <=12:
                    char = "-"
                elif column == 13:
                    char = "="
                elif column == 14:
                    char = "+"
                elif 15<= column <=17:
                    char = "="
                elif column in (18,19):
                    char = "-"
                elif column == 20 :
                    char = "="
                elif column in (21,22):
                    char = ":"
                elif column == 23:
                    char = "-"
                elif column == 24:
                    char = ":"
                elif column == 25:
                    char = "-"
                elif column in (26,27):
                    char = "="
                elif 28<= column <=30:
                    char = "-"
                elif column in (31,32):
                    char = "="
                elif 33<= column <=35:
                    char = "-"
                elif column == 36:
                    char = "+"
                elif column in (37,38):
                    char = "="
                elif 39<= column <=42:
                    char = "-"
            if row == 15:
                if column in (3,4):
                    char = "+"
                elif 5<= column <=7:
                    char = "*"
                elif column == 8:
                    char = "+"
                elif 9<= column <=11:
                    char = "-"
                elif 12<= column <=16:
                    char = ":"
                elif 17<= column <=20:
                    char = "-"
                elif 21<= column <=26:
                    char = ":"
                elif 27<= column <=29:
                    char = "-"
                elif column == 30:
                    char = ":"
                elif 31<= column <=34:
                    char = "-"
                elif column == 35:
                    char = "="
                elif 36<= column <= 38:
                    char = "-"
                elif column in (39,40):
                    char = "="
            if row == 16:
                if column == 4:
                    char = "+"
                elif column == 5:
                    char = "="
                elif column == 6:
                    char = "+"
                elif column == 7:
                    char = "*"
                elif column == 8:
                    char = "+"
                elif column == 9:
                    char = "="
                elif column in (10,11):
                    char = "-"
                elif 12<= column <=16:
                    char = ":"
                elif column == 17:
                    char = "-"
                elif column == 18:
                    char = "="
                elif column in (19,20):
                    char = "-"
                elif 21<= column <=31:
                    char = ":"
                elif 32<= column <=37:
                    char = "-"
                elif column in (38,39):
                    char = ":"
            if row == 17:
                if  column == 6:
                    char = "+"
                elif column in (7,8):
                    char = "*"
                elif column == 9:
                    char = "+"
                elif column == 10:
                    char = "="
                elif column in (11,12):
                    char = "-"
                elif 13<= column <=15:
                    char = ":"
                elif column == 16:
                    char = "-"
                elif column in (17,18):
                    char = "="
                elif column in (19,20):
                    char = "-"
                elif 21<= column <=24:
                    char = ":"
                elif column == 25:
                    char = "-"
                elif 26<= column <=31:
                    char = ":"
                elif column in (32,33):
                    char = "-"
                elif column == 34:
                    char = "="
                elif column in (35,36):
                    char = "-"
                elif column in (37,38):
                    char = ":"
            if row == 18:
                if 7<= column <=9:
                    char = "*"
                elif column == 10:
                    char = "+"
                elif column == 11:
                    char = "="
                elif 12<= column <=15:
                    char = "-"
                elif column == 16:
                    char = "="
                elif column == 17:
                    char = "#"
                elif column == 18:
                    char = "%"
                elif column == 19:
                    char = "#"
                elif column == 20:
                    char = "+"
                elif column == 21:
                    char = "="
                elif column in (22,23):
                    char = "+"
                elif column == 24:
                    char = "-"
                elif column == 25:
                    char = ":"
                elif column in (26,27):
                    char = "-"
                elif column == 28:
                    char = ":"
                elif 29<= column <=32:
                    char = "-"
                elif column == 33:
                    char = "="
                elif 34<= column <=37:
                    char = "-"
            if row == 19:
                if column == 8:
                    char = "*"
                elif 9<= column <=11:
                    char = "+"
                elif 12<= column <=16:
                    char = "="
                elif 17<= column <=19:
                    char = "-"
                elif column in (20,21):
                    char = "="
                elif column == 22:
                    char = "-"
                elif 23<= column <=26:
                    char = ":"
                elif column in (27,28):
                    char = "-"
                elif column == 29:
                    char = "=" 
                elif 30<= column <=34:
                    char = "-"
                elif column == 35:
                    char = ":" 
            if row == 20:
                if column == 9:
                    char = "+"
                elif column in (10,11):
                    char = "="
                elif column in (12,13):
                    char = "-"
                elif column == 14:
                    char = "+"
                elif column == 15:
                    char = "#"
                elif column == 16:
                    char = "*"
                elif column == 17:
                    char = "+"
                elif column == 18:
                    char = "="
                elif column in (19,20):
                    char = "-"
                elif 21<= column <=23:
                    char = ":"
                elif column in (24,25):
                    char = "-"
                elif column == 26:
                    char = "+"
                elif column == 27:
                    char = "="
                elif 28<= column <=33:
                    char = "-"
                elif column == 34:
                    char = ":"
            if row == 21:
                if column == 10:
                    char = "*"
                elif column in (11,12):
                    char = "+"
                elif column == 13:
                    char = "="
                elif column in (14,15):
                    char = "-"
                elif 16<= column <=18:
                    char = "="
                elif 19<= column <=25:
                    char = "-"
                elif column in (26,27):
                    char = ":"
                elif 28<= column <=32:
                    char = "-"
                elif column in (33,34):
                    char = "=" 
            if row == 22:
                if column == 10:
                    char = "*"     
                elif column == 11:
                    char = "+"
                elif column == 12:
                    char = "="
                elif 13<= column <=16:
                    char = "-"
                elif 17<= column <=20:
                    char = "="
                elif 21<= column <=23:
                    char = "-"
                elif column == 24:
                    char = ":"
                elif 25<= column <=28:
                    char = "-"
                elif column == 29:
                    char = "="
                elif column == 30:
                    char = "+"
                elif column == 31:
                    char = "%"
                elif column == 32:
                    char = "#"
                elif column == 33:
                    char = "+"
                elif column == 34:
                    char = "="
                elif 35<= column <=37:
                    char = "-"
                elif 38<= column <=41:
                    char = ":"
            if row == 23:
                if column == 11:
                    char = "*"
                elif column in (12,13):
                    char = "+"
                elif column in (14,15):
                    char = "="
                elif column in (16,17):
                    char = "-"
                elif  18<= column <=24:
                    char = ":"
                elif 25<= column <=27:
                    char = "-"
                elif column == 28:
                    char = "="
                elif column == 29:
                    char = "+"
                elif column == 30:
                    char = "#"
                elif column in (31,32):
                    char = "%"
                elif column == 33:
                    char = "@"
                elif column == 34:
                    char = "%"
                elif column == 35:
                    char = "#"
                elif column == 36:
                    char = "+"
                elif 37<= column <=42:
                    char = "-"
            if row == 24:
                if 11<= column <=15:
                    char =  "*"
                elif  column in (16,17):
                    char = "+"
                elif column == 18:
                    char = "="
                elif 19<= column <=21:
                    char = "-"
                elif 22<= column <=24:
                    char = ":"
                elif column in (25,26):
                    char = "-"
                elif column in (27,28):
                    char = "="
                elif column == 29:
                    char = "+"
                elif column == 30:
                    char = "="
                elif column == 31:
                    char = "-"
                elif column == 32:
                    char = "*"
                elif column == 33:
                    char = "#"
                elif column in (34,35):
                    char = "%"
                elif column in (36,37):
                    char = "@"
                elif column == 38:
                    char = "#"
                elif column == 39:
                    char = "="
                elif 40<= column <=43:
                    char = "-"
                elif column == 44:
                    char = ":" 
            if row == 25:
                if  13<= column <=17:
                    char = "*"
                elif 18<= column <= 20:
                    char = "+"
                elif 21<= column <=25:
                    char = "="
                elif column in (26,27):
                    char = "+"
                elif 28<= column <=31:
                    char = "-"
                elif column == 32:
                    char = "*"
                elif column == 33:
                    char = "#"
                elif column == 34:
                    char = "*"
                elif column == 35:
                    char = "#"
                elif column in (36,37):
                    char = "%"
                elif column == 38:
                    char = "*"
                elif 39<= column <=41:
                    char = "-"
                elif 42<= column <=44:
                    char = ":"
            if row == 26:
                if 13<= column <=20:
                    char = "*"
                elif 21<= column <=24:
                    char = "+"
                elif column == 25:
                    char = "-"
                elif 26<= column <=30:
                    char = ":"
                elif column in (31,32):
                    char = "-"
                elif column == 33:
                    char = "+"
                elif 34<= column <=36:
                    char = "%"
                elif column == 37:
                    char = "@"
                elif column == 38:
                    char = "%"
                elif column == 39:
                    char = "*"
                elif column == 40:
                    char = "="
                elif column == 41:
                    char = "+"
                elif 42<= column <=44:
                    char = "-"
            if row == 27:
                if 12<= column <=19:
                    char = "*"
                elif column == 20:
                    char = "+"
                elif column == 21:
                    char = "="
                elif 22<= column <=29:
                    char = ":"
                elif column in (30,31):
                    char = "-"
                elif column == 32:
                    char = "="
                elif column == 33:
                    char = "#"
                elif column in (34,35):
                    char = "%"
                elif 36<= column <=38:
                    char = "@"
                elif column in (39,40):
                    char = "%"
                elif column == 41:
                    char = "#"
                elif column in (42,43):
                    char = "*"
            if row == 28:
                if  12<= column <=19:
                    char = "*"
                elif column == 20:
                    char = "+"
                elif column == 21:
                    char = "-"
                elif 22<= column <=32:
                    char = ":"
                elif column == 33:
                    char = "-"
                elif column == 34:
                    char = "+"
                elif column == 35:
                    char = "#"
                elif 36<= column <=42:
                    char = "%"
                elif column == 43:
                    char = "*"
                elif column == 44:
                    char = "+"
            if row == 29:
                if 11<= column <=18:
                    char = "-"
                elif  19<= column <=34:
                    char = ":"
                elif  column == 35:
                    char = "="
                elif column == 36:
                    char = "*"
                elif column == 37:
                    char = "#"
                elif column in (38,39):
                    char = "%"
                elif column == 40:
                    char = "#"
                elif column == 41:
                    char = "+"
                elif column == 42:
                    char = "="
                elif column == 43:
                    char = "*"
                elif column == 44:
                    char = "+"
            if row == 30:
                if column == 0:
                    char = "-"
                elif column == 1:
                    char = "="
                elif column in (2,3):
                    char = "-"
                elif 4<= column <=10:
                    char = ":"
                elif column == 11:
                    char = "-"
                elif column == 12:
                    char = ":"
                elif 13<= column <=15:
                    char = "-"
                elif 16<= column <=32:
                    char = ":"
                elif column in (33,34):
                    char = "-"
                elif column == 35:
                    char = "="
                elif 36<= column <=38:
                    char = "*"
                elif column == 39:
                    char = "+"
                elif column == 40:
                    char = "-"
                elif column == 41:
                    char = "="
                elif column == 42:
                    char = "-"
                elif column in (43,44):
                    char = ":"
            if row == 31:
                if column == 0:
                    char = "-"
                elif 1<= column <=9:
                    char = ":"
                elif 10<= column <=14:
                    char = "-"
                elif 15<= column <=37:
                    char = ":"
                elif column == 38:
                    char = "="
                elif column == 39:
                    char = "-"
                elif column in (40,41):
                    char = "="
                elif column == 42:
                    char = "-"
                elif column == 43:
                    char = ":"
                elif column == 44:
                    char = "-"
            if row == 32:
                if column == 0:
                    char = ":"
                elif column in (1,2):
                    char = "-"
                elif 3<= column <=5:
                    char = ":"
                elif 6<= column <=8:
                    char = "-"
                elif 9<= column <=11:
                    char = ":"
                elif 12<= column <=14:
                    char = "-"
                elif 15<= column <=44:
                    char = ":"                                                                                                                                                 

                                      
                        







                                                                                               

                            

                        








                    

                                                                                   





                                                                                    





                                

                   


                                                                     
                                

                                                                                                                                   


                                                               











                   
                  

            
                                                                         

            
         

        

            
    
    
    
    
            print(char,end='')
        
        print()
gen_ascii()