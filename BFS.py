import Puzzle
from collections import deque


class BFS(object):    
                    
    @staticmethod
    def dfs():
        
        tableroInicial=[['10','7 ','3 ','6 '],['14','13','4 ','11'],['X ','1 ','9 ','8 '],['2 ','15','12','5 ']]
        tableroFinal = [['1 ','2 ','3 ','4 '],['5 ','6 ','7 ','8 '],['9 ','10','11','12'],['13','14','15','X ']]    
                                
        agenda = deque([Puzzle.Puzzle(tableroInicial,None,2,0,"inicial")])        
        expandido = agenda.popleft()    
        expansion = Puzzle.Puzzle.returnMoves(expandido)
        nodosExpandidos = {str(expandido.value):expandido}
        print("hijos")
        for hijo in expansion:
            agenda.append(hijo)                            
            print(hijo.value)  
                 
        while Puzzle.Puzzle.comparePuzzles(tableroFinal,expansion)==-1: #si es igual a cero quiere decir que no son iguales por lo tanto seguimos buscando        
        
            expandido = agenda.popleft()
            if not nodosExpandidos.__contains__(str(expandido.value)):                
                expansion = Puzzle.Puzzle.returnMoves(expandido)
                nodosExpandidos[str(expandido.value)] = expandido                
                print("hijos")
                for hijo in expansion:
                    agenda.append(hijo)                    
                    print(hijo.value)                      
            
            """else:                
                break""" 
        print("terminado por BFS esta es la respuesta:")  
        
        resultado = [Puzzle.Puzzle(tableroFinal,expandido,3,3,"Final?"),expandido] 
        parcial  = expandido.padre
             
       
        while parcial.padre!=None: 
            resultado.append(parcial)
            parcial =parcial.padre            
            
        resultado.reverse()
       
        for tablerin in resultado:
           
            pass
            #print (tablerin)
            
        print("numero de movimientos:"+str(resultado.__len__()))    
                
                 
    
            
          

BFS.dfs()
    
