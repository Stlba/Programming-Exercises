"""-------------------------------------"""

import math

"""-------------------------------------"""

# __MAIN__
def eval_one():

    
    #                EVAL FUNCTION
    #-----------------------------------------------#
    
    
    # Array to store variables and calculations
    data_input = []
    
    
    # Input results
    inputR = ""
    
    # Evaluation Function 
    def eval_two():
        
        # Results from user input
        inputR = input("Please feed me numbers\n\n> ")
        #            ▼
        
        # Results after calculation
        if inputR == "done":
            data_input.append("done")
            return
        #            ▼     

        # Export to Array
        elif inputR != "done":  
            
            inputE = eval(inputR)
            #            ▼        
            # Append user input and eval to data_input array
            data_input.append(inputR)
            data_input.append(inputE)
            #            ▼        
            # Print [userinput = calculation]
            print(f"{data_input[-2]} = {data_input[-1]}")

        
    #                 ITERATION
    #-----------------------------------------------#
   
   
    # While inputR isn't equal to "polse
    while inputR != "polse":
        
        # Run eval_two
        eval_two()
        
        # if data_input array last item is "done, then True
        if data_input[-1] == "done":
            
            # If array is equal to or less than 1, then True
            if len(data_input) <= 1:
                inputF = input("You haven't done any evaluaton yet. Are you sure? (Yes/No)")
                if inputF.lower() == "yes":
                    print("Exiting now")
                    return
                else:
                   eval_one() 
            
            # If data_input array length is greater than 1, then True
            if len(data_input) > 1:
                print(f"Your latest calculation was: {data_input[-3]} = {data_input[-2]}")
                return
    
            

eval_one()
