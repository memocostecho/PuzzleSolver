import Puzzle
import Queue



class AStar(object):    
                    
    @staticmethod
    def AStar(tableroInicial, tableroFinal):
        
        f = open('resultado.txt', 'w')
                
        agenda = Queue.PriorityQueue()
        root = Puzzle.Puzzle(tableroInicial,None,2,2,"inicial")
        root.setheuristic(Puzzle.Puzzle.calculaHeuristica(root.value))
        root.setCosto(0)
        agenda.put((root.heuristic+root.costo,root)) 
        #print(root.heuristic)
        #print(Puzzle.Puzzle.calculaHeuristica(tableroInicial))                                             
        expandido = agenda.get()[1] 
        #print(expandido.heuristic)
        #print(expandido.heuristic)   
        expansion = Puzzle.Puzzle.returnMoves(expandido)
        nodosExpandidos = {str(expandido.value):expandido}
       
        for hijo in expansion:
            hijo.setheuristic(Puzzle.Puzzle.calculaHeuristica(hijo.value))
            hijo.setCosto(1)
            #hijo.setheuristic(Puzzle.Puzzle.calculaHeuristica(hijo.value)+expandido.heuristic)                        
            agenda.put((hijo.heuristic+hijo.costo,hijo))                                                                     
        while Puzzle.Puzzle.comparePuzzles(tableroFinal,expansion)==-1: #si es igual a cero quiere decir que no son iguales por lo tanto seguimos buscando                    
            expandido = agenda.get()[1]             
            if not nodosExpandidos.__contains__(str(expandido.value)):
                #print(expandido.heuristic)                
                expansion = Puzzle.Puzzle.returnMoves(expandido)
                nodosExpandidos[str(expandido.value)] = expandido                                
                for hijo in expansion:
                    #hijo.setheuristic(Puzzle.Puzzle.calculaHeuristica(hijo.value))
                    #hijo.setheuristic(Puzzle.Puzzle.calculaHeuristica(hijo.value)+expandido.heuristic)                                    
                    hijo.setheuristic(Puzzle.Puzzle.calculaHeuristica(hijo.value))
                    hijo.setCosto(expandido.costo+1)
                    agenda.put((hijo.heuristic+hijo.costo,hijo))                                        
                                    
            
          
        
        resultado = [Puzzle.Puzzle(tableroFinal,expandido,3,3,"Final?"),expandido] 
        parcial  = expandido.padre
             
       
        while parcial.padre!=None: 
            resultado.append(parcial)
            parcial =parcial.padre 
       
        resultado.append(parcial)               
            
        resultado.reverse()
                        
        for tablerin in resultado:                      
            f.write(repr(tablerin)+"\n")
        
        print ("Termine bien A*")
                                                            
        f.write("numero de movimientos:"+str(resultado.__len__()-1))    
        
        Puzzle.Puzzle.animaResultado(resultado, tableroInicial)
         
                
    
tableroInicial=[['1 ','2 ','3 ','4 '],['5 ','6 ','7 ','8 '],['9 ','15','X ','10'],['11','12','13','14']]
        
tableroFinal = [['1 ','2 ','3 ','4 '],['5 ','6 ','7 ','8 '],['9 ','10','11','12'],['13','14','15','X ']]            
     
     
     
         
AStar.AStar(tableroInicial, tableroFinal)
    
