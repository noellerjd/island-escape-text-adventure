print('''
            |                                 |
            |                                 |
            |                                 |
            |            _________            |
            |           |         |           |
            |           |   ___   |           |
            |           I  |___|  |           |
            |           |         |           |
            |           |         |           |
            |           |        _|           |
            |           |       |#|           |  ;,
    -- ___  |           |         |           |   ;'
    H*/   ` |           |         |      _____|    .,`
    */     )|           I         |     \_____\     ;'
    /___.,';|           |         |     \\     \     ."`
    |     ; |___________|_________|______\\     \      ;:
''')
print("Welcome to Rikers Island")
print("Your mission is to escape the island.\n") 

choice_1 = input("You open the cell door, will you go right or left? ")

if choice_1 == "left" or choice_1 == "Left" or choice_1 == "l" or choice_1 == "L":
    print('''
               |
         \ _ /
       -= (_) =-
         /   \         _\/_
           |           //o\  _\/_
    _____ _ __ __ ____ _ | __/o\\ _
  =-=-_-__=_-= _=_=-=_,-'|"'""-|-,_
   =- _=-=- -_=-=_,-"          |
    ''')
    print("You make it out to the shoreline. You can hear the guards are looking for you. ")
    choice_2 = input("Will you try to swim or wait? ")

    if choice_2 == "swim" or choice_2 == "Swim" or choice_2 == "s" or choice_2 == "S":
        print('''
__|  .      .   .  //______________________________| :----------------------.
__|   /|\      _|_|//       ooooooooooooooooooooo  |-|                      |
__|  |/|\|__   ||l|/,-------8                   8 -| |                      |
__|._|/|\|||.l |[=|/,-------8       HOTEL       8 -|-|                      |
__|[+|-|-||||li|[=|---------8                   8 -| |                      |
_-----.|/| //:\_[=|\`-------8                   8 -|-|                      |
/ |  /||//8/ :  8_|\`------ 8ooooooooooooooooooo8 -| |                      |
/=| //||/ |  .  | | \\_____________  ____  _________|-|                      |
==|//||  /   .   \  \\_____________ |X|  | _________| `---==------------==---'
==| ||  /         \ \_____________ |X| \| _________|     ||            ||
==| |~ /     .     \
        ''')
        choice_3 =  input("You manage to swim to the nearest beach. You find a town.\nTheres a road that leads north, a hotel, and a forest to the right. \n \nWill you: \n1. follow the road.\n2. Enter the hotel.\n3. Go into the forest.\n")
        
        if choice_3 == "1":
            print('''
     _______/_____
   D'-.      | /  )
   '(o)'-.....'(O)'
            \n''')
            print("You find a taxi and are able to escape safely!\nYou win!")
        elif choice_3 == "2":
            print('''
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
            ''')
            print("\nYou find police officers already waiting in the hotel. You try to run but they kill you in the process. \nGame Over. Try again!")
        elif choice_3 == "3":
            print('''
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
            ''')
            print("\nYour clothes are soaking wet. You get lost in the forest and freeze to death. \nGame Over. Try again!")
        elif choice_3 != "1" or "2" or "3":
            print('''
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
            ''')
            print("You couldn't make a decision. You stand there until you're caught. (You must choose 1 2 or 3) \nGame Over. Try again!")
        
    else: 
        print('''
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
    ''')
        print("\nThe guards eventually find you and kill you. \nGame Over. Try again!")
else:
    print('''
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
    ''')
    print("\nYou walk right into a guard who shoots you on sight. \nGame Over. Try again!")

