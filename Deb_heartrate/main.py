from Function.get_heartrate import *
import time
class main():
    def __init__(self):
        super().__init__()
        
        
        
        print("Main init")
        #hr_rsult = get_hr()

        start_time = time.time()
        hr_rsult = runAll()
        print("--- %s seconds ---" % (time.time() - start_time))

        print(hr_rsult)
        print("Heart Rate :: %s seconds ---" % (hr_rsult[2]))
        

    

    def start(self):
        print(" start ")






if __name__ == '__main__':
    main()