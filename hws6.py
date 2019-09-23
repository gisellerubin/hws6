import prompt as prompt

numb_ofmoves= 0
num_life=3

while True:
    way= input("You are in the magic maze, which way to go?, [N,S,W,E]")

    try:
        if way== "S":
         way2= input("Congrats, 1st Step Done, Which way to go now?[N,S,W,E]")
         numb_ofmoves=numb_ofmoves+1

         try:
             if way2 == "S":
                 way3 = input("Congrats, 2nd Step Done, Which way to go now?[N,S,W,E]")
                 numb_ofmoves=numb_ofmoves+1

                 try:
                     if way3 == "N":
                         way4 = input("Congrats, 3rd Step Done, Which way to go now?[N,S,W,E]")
                         numb_ofmoves=numb_ofmoves+1

                         try:
                                 if way4 == "W":
                                     way5 = input("Congrats, 4th Step Done, Which way to go now?[N,S,W,E]")
                                     numb_ofmoves=numb_ofmoves+1

                                     try:
                                         if way5 == "E":
                                             way6 = input("Congrats, 5th Step Done, Which way to go now?[N,S,W,E]")
                                             numb_ofmoves=numb_ofmoves+1

                                             try:
                                                 if way6 == "S":
                                                     way7 = input("You have escaped the maze in:"+ str (numb_ofmoves)+"moves")




                                             except ValueError:
                                                 if way6 != "S":
                                                     input("Wrong way, train again" , way)
                                                     numb_ofmoves = numb_ofmoves + 1



                                     except ValueError:
                                         if way5 != "E":
                                             input("Wrong way, train again" , way)
                                             numb_ofmoves = numb_ofmoves + 1



                         except ValueError:
                                 if way4 != "W":
                                         input("Wrong way, train again" , way)
                                         numb_ofmoves=numb_ofmoves+1


                 except ValueError:
                        if way3 != "N":
                                 input("Wrong way, train again" , way)
                                 numb_ofmoves = numb_ofmoves + 1




         except ValueError:
             if way2 != "S":
                 input("Wrong way, train again" , way)
                 numb_ofmoves=numb_ofmoves+1





    except ValueError:
          if way != "S":

             message= "Wrong way, train again" + way
             input(message)
             numb_ofmoves=numb_ofmoves+1


