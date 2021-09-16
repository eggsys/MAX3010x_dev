import hrcalc 
from Function.sim_cal import *
from Function.test_function import functiontest


class base():
    def __init__(self):        
        print("BASE __INIT__")



class main(base):

    def __init__(self):
        super().__init__()
        #base.__init__(self)
        #base.__init__(self)
        print("init")
        print(main.__mro__)
        self.start()
        
    
    def test(self):
        print("Testing")


    
    def start(self):
        print(" Starting ")
        ##functiontest()
        ir_data = []
        red_data = []


        for x in range(0, 50):
           
            ir_data.append(64781)
            ir_data.append(49148)
            #ir_data.append(68591)
            #ir_data.append(68469)

            #red_data.append(68731)
            #red_data.append(68437)
            red_data.append(68679)
            red_data.append(71055)


        print(len(ir_data))
        bpm, valid_bpm, spo2, valid_spo2 = hrcalc.calc_hr_and_spo2(ir_data, red_data)

        print(bpm, valid_bpm, spo2, valid_spo2)




main = main()

