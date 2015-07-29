import Puzzle
import DLS


class ID(object):    
    
    solucion = None 
    resultado=None   
                        
    @staticmethod
    def id(puzzle,tableroFinal):   #recibe un puzzle y se compara contra un tablero nada mas (matriz)        
        profundidad=0      
        DLS.DLS.dls(puzzle, tableroFinal, profundidad)
        ID.solucion = DLS.DLS.solucion
        print(ID.solucion)
        while ID.solucion == None:
            profundidad=profundidad+1
            ID.solucion = DLS.DLS.dls(puzzle, tableroFinal, profundidad) 
            print(ID.solucion) 
            print(profundidad)                      
       
        
        return ID.solucion
        


                   
tableroInicial=[['1 ','2 ','3 ','4 '],['5 ','6 ','7 ','X '],['9 ','10','11','8 '],['13','14','15','12']]
tableroFinal = [['1 ','2 ','3 ','4 '],['5 ','6 ','7 ','8 '],['9 ','10','11','12'],['13','14','15','X ']]        

                
ID.id(Puzzle.Puzzle(tableroInicial,None,1,3,"inicial"), tableroFinal)
#print (ID.resultado) 
  
