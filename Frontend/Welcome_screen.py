import time
import sys

def animation():
    def anim1():

        frame = ["....", "."]

        for i in frame:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.25)


        def anm2():

            sys.stdout.write(frame[1])
            sys.stdout.flush()
            time.sleep(0.25)
            sys.stdout.write("\b \b")
            sys.stdout.flush()
            time.sleep(0.25)

        for i in range(3):
            anm2()

        print("\t", end= "")

    def anim2():
        frames = [
            "⠋",
            "⠙",
            "⠹",
            "⠸",
            "⠼",
            "⠴",
            "⠦",
            "⠧",
        ]
            
        for i in range(3):

            for i in frames:
                sys.stdout.write("\b"+i)
                sys.stdout.flush()
                time.sleep(0.1)
            
        print("\t", end= "")
            

    def anim3():

        frames= ['D', 'A', 'P', 'I', 'S', '-','0','.','1',' ','W', 'E', 'L', 'C', 'O', 'M', 'E', 'S', ' ', 'T', 'H', 'E', ' ', 'U', 'S', 'E', 'R']
        for i in frames:

            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.10)

        print("\t", end= "")

    def anim4():

        frames= ['(', '^', '_', '^', ')']
        for j in range(2):
            for i in frames:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.15)

        print("\t", end= "")

    def anim5():

        frames = [
            "⠋",
            "⠙",
            "⠹",
            "⠸",
            "⠼",
            "⠴",
            "⠦",
            "⠧",
    ]
            
        for i in range(3):

            for i in range(len(frames)-1, 0, -1):
                sys.stdout.write("\b"+frames[i])
                sys.stdout.flush()
                time.sleep(0.1)
            
        print("\t", end= "")

    anim1()
    anim2()
    anim3()
    anim4()
    anim5()
        
        
