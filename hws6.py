import prompt as prompt

numb_ofmoves= 0
num_life=3

while True:
    if numb_ofmoves ==10:
        num_life= num_life-1
        print("You have lost a life, you now have: "+ str (num_life))
    if numb_ofmoves == 20:
        num_life = num_life - 1
        print("You have lost a life, you now have: " + str(num_life))
    if numb_ofmoves == 30:

        print("You have died")
        break

    way= input("You are in the magic maze, which way to go?, [N,S,W,E]")



    if way== "S":
             way2= input("Congrats, 1st Step Done, Which way to go now?[N,S,W,E]")
             numb_ofmoves=numb_ofmoves+1


             if way2 == "S":
                     way3 = input("Congrats, 2nd Step Done, Which way to go now?[N,S,W,E]")
                     numb_ofmoves=numb_ofmoves+1


                     if way3 == "N":
                             way4 = input("Congrats, 3rd Step Done, Which way to go now?[N,S,W,E]")
                             numb_ofmoves=numb_ofmoves+1


                             if way4 == "W":
                                 way5 = input("Congrats, 4th Step Done, Which way to go now?[N,S,W,E]")
                                 numb_ofmoves=numb_ofmoves+1


                                 if way5 == "E":
                                             way6 = input("Congrats, 5th Step Done, Which way to go now?[N,S,W,E]")
                                             numb_ofmoves=numb_ofmoves+1


                                             if way6 == "S":
                                                    way7 = input("You have escaped the maze in: "+ str (numb_ofmoves)+"moves")





                                             if way6 != "S":
                                                 print ("Wrong way, train again: " + way)
                                                 numb_ofmoves = numb_ofmoves + 1




                                 if way5 != "E":
                                     print ("Wrong way, train again: " + way)
                                     numb_ofmoves = numb_ofmoves + 1




                             if way4 != "W":
                                 print ("Wrong way, train again: " + way)
                                 numb_ofmoves=numb_ofmoves+1



                     if way3 != "N":
                         print ("Wrong way, train again: " + way)

                         numb_ofmoves = numb_ofmoves + 1





             if way2 != "S":
                 print("Wrong way, train again: " + way)

                 numb_ofmoves=numb_ofmoves + 1






    else:

            print("Wrong way, train again: " + way)

            numb_ofmoves=numb_ofmoves+1


