import Puzzle

class DLS(object):    
    
    solucion = None    
                        
    @staticmethod
    def dls(puzzle,tableroFinal,profundidad):   #recibe un puzzle y se compara contra un tablero nada mas (matriz)        
        
        if profundidad>0: 
            if Puzzle.Puzzle.comparePuzzle(puzzle.value,tableroFinal):                
                DLS.solucion =  puzzle               
                return DLS.solucion                         
            expansion  =  Puzzle.Puzzle.returnMoves(puzzle)
            for hijo in expansion:
                DLS.dls(hijo,tableroFinal,profundidad-1)                                 
        return DLS.solucion
                   
#tableroInicial=[['1 ','2 ','3 ','4 '],['5 ','6 ','7 ','X '],['9 ','10','11','8 '],['13','14','15','12']]
#tableroFinal = [['1 ','2 ','3 ','4 '],['5 ','6 ','7 ','8 '],['9 ','10','11','12'],['13','14','15','X ']]        

                
#DLS.dls(Puzzle.Puzzle(tableroInicial,None,1,3,"inicial"), tableroFinal, 5)
#print (DLS.solucion) 
  
