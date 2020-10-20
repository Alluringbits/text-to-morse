import winsound,time, sys

morse = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"}

dotspeed = 100
def morsefunct():
    try:
        for _ in input("Word: "):
            if str(_) == " ":
                time.sleep(0.4)
            else:
                for line in morse[_.lower()]:
                    if str(line) == "-":
                        winsound.Beep(500, 4*dotspeed)
                    else:
                        winsound.Beep(500, dotspeed)
                        time.sleep(0.1)
            time.sleep(0.15)
    except KeyboardInterrupt:
        sys.exit()
    except:
        print("Incorrect input , please only use latin alphabet letters and numbers.")
        morsefunct()
morsefunct()