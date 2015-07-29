import Puzzle
from collections import deque


class BFS(object):    
                    
    @staticmethod
    def bfs(tableroInicial,tableroFinal):                                            
        agenda = deque([Puzzle.Puzzle(tableroInicial,None,1,2,"inicial")])        
        expandido = agenda.popleft()    
        expansion = Puzzle.Puzzle.returnMoves(expandido)
        nodosExpandidos = {str(expandido.value):expandido}        
        for hijo in expansion:
            agenda.append(hijo)                            
            print(hijo.value)  
                 
        while Puzzle.Puzzle.comparePuzzles(tableroFinal,expansion)==-1: #si es igual a cero quiere decir que no son iguales por lo tanto seguimos buscando        
        
            expandido = agenda.popleft()
            if not nodosExpandidos.__contains__(str(expandido.value)):                
                expansion = Puzzle.Puzzle.returnMoves(expandido)
                nodosExpandidos[str(expandido.value)] = expandido                
               
                for hijo in expansion:
                    agenda.append(hijo)                    
                                      
            
            
        print("terminado por BFS esta es la respuesta:")  
        
        resultado = [Puzzle.Puzzle(tableroFinal,expandido,3,3,"Final?"),expandido] 
        parcial  = expandido.padre
             
       
        while parcial.padre!=None: 
            resultado.append(parcial)
            parcial =parcial.padre            
            
        resultado.append(parcial)
        
        resultado.reverse()
       
        Puzzle.Puzzle.animaResultado(resultado, tableroInicial)
        
            
        print("numero de movimientos:"+str(resultado.__len__()))    
                
                 
    
tableroInicial=[['1 ','2 ','7 ','3 '],['5 ','6 ','X ','4 '],['9 ','10','11','8 '],['13','14','15','12']]
tableroFinal = [['1 ','2 ','3 ','4 '],['5 ','6 ','7 ','8 '],['9 ','10','11','12'],['13','14','15','X ']]            
          

BFS.bfs(tableroInicial,tableroFinal)
    
