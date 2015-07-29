import Puzzle


class DFS(object):    
        
    
    @staticmethod
    def dfs(tableroInicial, tableroFinal):
        
        f = open('resultado.txt', 'w')                                                
        agenda = [Puzzle.Puzzle(tableroInicial,None,1,3,"inicial")]             
        expandido = agenda.pop()    
        expansion = Puzzle.Puzzle.returnMoves(expandido)
        nodosExpandidos = {str(expandido.value):expandido}
       
        for hijo in expansion:
            agenda.append(hijo)                                        
                 
        while Puzzle.Puzzle.comparePuzzles(tableroFinal,expansion)==-1: #si es igual a cero quiere decir que no son iguales por lo tanto seguimos buscando                    
            expandido = agenda.pop()
            if not nodosExpandidos.__contains__(str(expandido.value)):                
                expansion = Puzzle.Puzzle.returnMoves(expandido)
                nodosExpandidos[str(expandido.value)] = expandido                                
                for hijo in expansion:
                    agenda.append(hijo)                    
                                    
            
        print("terminado por dFS esta es la respuesta:")  
        
        resultado = [Puzzle.Puzzle(tableroFinal,expandido,2,2,"Final?"),expandido] 
        parcial  = expandido.padre
             
       
        while parcial.padre!=None: 
            resultado.append(parcial)
            parcial =parcial.padre 
       
        resultado.append(parcial)               
            
        resultado.reverse()
        
        for tablerin in resultado:                      
            f.write(repr(tablerin)+"\n")
                         
        f.write("numero de movimientos:"+str(resultado.__len__()-1))    
        
        Puzzle.Puzzle.animaResultado(resultado, tableroInicial)        
         
                
    
# tableroInicial=[['2 ','3 ','4 ','X '],['1 ','6 ','7 ','8 '],['5 ','10','11','12'],['9 ','13','14','15']]

tableroInicial=[['1 ','2 ','3 ','4 '],['5 ','6 ','7 ','X '],['9 ','10','11','8 '],['13','14','15','12']]        
tableroFinal = [['1 ','2 ','3 ','4 '],['5 ','6 ','7 ','8 '],['9 ','10','11','12'],['13','14','15','X ']]            
          

DFS.dfs(tableroInicial,tableroFinal)

    
