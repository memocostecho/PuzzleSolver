import Puzzle


class DLS(object):    
                    
    @staticmethod
    def dls(nodo,objetivo,profundidad):
       if profundidad>0: 
           if nodo == objetivo:
            return nodo
       for each child in expand(nodo):
           DLS(hijo,goal,depth-1) 
                                
                 
                 
    
            
          

#DLS.dls(nodo, objetivo, profundidad)   
