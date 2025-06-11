def somma_elementi(x, y):
    
        sum_list = []
        index = 0
        somma=0
        for i in x:
            somma = i + y[index]
            sum_list.append(somma)
            index +=1
        return print(sum_list)
   
somma_elementi([1,2,-1],[0,-1,0])



        
        
