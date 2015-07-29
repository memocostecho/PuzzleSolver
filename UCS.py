import Puzzle
import Queue


class UCS(object):    
        
    
    
    
    @staticmethod
    def ucs(tableroInicial, tableroFinal):
        
        f = open('resultado.txt', 'w')
                
        agenda = Queue.PriorityQueue()
        root = Puzzle.Puzzle(tableroInicial,None,2,2,"inicial")
        #root.setheuristic(Puzzle.Puzzle.calculaHeuristica(root.value))
        agenda.put((0,root)) 
        #print(root.heuristic)
        #print(Puzzle.Puzzle.calculaHeuristica(tableroInicial))                                             
        expandido = agenda.get()[1] #el [1 ] indica que obtienes el nodo y no la prioridad.
        #print(expandido.heuristic)
        #print(expandido.heuristic)   
        expansion = Puzzle.Puzzle.returnMoves(expandido)
        nodosExpandidos = {str(expandido.value):expandido}
       
        for hijo in expansion:
            #hijo.setheuristic(Puzzle.Puzzle.calculaHeuristica(hijo.value))
            #hijo.setheuristic(Puzzle.Puzzle.calculaHeuristica(hijo.value)+expandido.heuristic)                        
            agenda.put((1,hijo))                                                                     
        while Puzzle.Puzzle.comparePuzzles(tableroFinal,expansion)==-1: #si es igual a cero quiere decir que no son iguales por lo tanto seguimos buscando                    
            expandido = agenda.get()[1]
            pesoExpandido=agenda.get()[0]
            #print(pesoExpandido)             
            if not nodosExpandidos.__contains__(str(expandido.value)):
#                 print(expandido.heuristic)                
                expansion = Puzzle.Puzzle.returnMoves(expandido)
                nodosExpandidos[str(expandido.value)] = expandido                                
                for hijo in expansion:
                    hijo.setheuristic(Puzzle.Puzzle.calculaHeuristica(hijo.value))
                    #hijo.setheuristic(Puzzle.Puzzle.calculaHeuristica(hijo.value)+expandido.heuristic)                                    
                    #hijo.setheuristic(Puzzle.Puzzle.calculaHeuristica(hijo.value)+expandido.heuristic)
                    agenda.put((1+pesoExpandido,hijo))                                        
                                    
            
        print("terminado por UCS esta es la respuesta:")  
        
        resultado = [Puzzle.Puzzle(tableroFinal,expandido,3,3,"Final?"),expandido] 
        parcial  = expandido.padre
             
       
        while parcial.padre!=None: 
            resultado.append(parcial)
            parcial =parcial.padre 
       
        resultado.append(parcial)               
            
        resultado.reverse()
        
        Puzzle.Puzzle.animaResultado(resultado, tableroInicial)
        
        for tablerin in resultado:                      
            f.write(repr(tablerin)+"\n")
                         
        f.write("numero de movimientos:"+str(resultado.__len__()-1))    
                
         
                
    
tableroInicial=[['1 ','2 ','3 ','4 '],['5 ','6 ','7 ','8 '],['9 ','15','X ','10'],['11','12','13','14']]
        
tableroFinal = [['1 ','2 ','3 ','4 '],['5 ','6 ','7 ','8 '],['9 ','10','11','12'],['13','14','15','X ']]            
     
     
     
         
UCS.ucs(tableroInicial, tableroFinal)

"""

priorityQueu = Queue.PriorityQueue()
priorityQueu.put((1,100))
priorityQueu.put((0,1))
priorityQueu.put((-1,3))



priorityQueu.put((-1000,"muy antes"))

while not priorityQueu.empty():
    item = priorityQueu.get()
    print('%s' % item[1])
"""
    
