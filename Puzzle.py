import copy



class Puzzle(object):  #es como el constructor de java    

    def __init__(self, value, padre,renglonHueco,columnaHueco,movimientoAnterior):
        self.value = value        
        self.padre = padre
        self.renglonHueco = renglonHueco
        self.columnaHueco = columnaHueco
        self.movimientoAnterior= movimientoAnterior
            

    def __repr__(self):   # es como el metodo toString de java        
        ret =""# repr(self.value)+"\n"
        for renglon in self.value:
            ret += repr(renglon)+"\n"
        return ret     
    
    @staticmethod
    def comparePuzzle(matrixA,matrixB):
        for (a,b) in zip(matrixA,matrixB):
            for (c,d) in zip(a,b):
                if(c!=d):
                    return False
        return True
      
    @staticmethod
    def comparePuzzles(matriz,matrices = []):
        counter = 0;
        for matrix in matrices:                
            if(Puzzle.comparePuzzle(matriz, matrix.value)):
                return counter
            counter+1
        return -1
    
    #regresa los posibles movimientos para un estado del Puzzle...(hijos)
    @staticmethod
    def returnMoves(tablero):  #aqui se esta haciendo estatico pero se hara dinamico y no se pasara ahi la pos.
        
        movimientos = []  #aqui se guardaran los hijos resultantes para depsues regresarlos
                  
        if tablero.renglonHueco>0   and not tablero.movimientoAnterior=="down":         #si la orden fue down quiere decir que no debemos ir para arriba regresariamos         
            matrizAux = copy.deepcopy(tablero.value)        
            matrizAux[tablero.renglonHueco][tablero.columnaHueco]=matrizAux[tablero.renglonHueco-1][tablero.columnaHueco]
            matrizAux[tablero.renglonHueco-1][tablero.columnaHueco]="X "        
            movimientos.append(Puzzle(matrizAux,tablero,tablero.renglonHueco-1,tablero.columnaHueco,"up"))
        
        
        if tablero.columnaHueco<3 and not tablero.movimientoAnterior=="left":          #si la orden fue down quiere decir que no debemos ir para arriba regresariamos         
            matrizAux = copy.deepcopy(tablero.value)        
            matrizAux[tablero.renglonHueco][tablero.columnaHueco]=matrizAux[tablero.renglonHueco][tablero.columnaHueco+1]
            matrizAux[tablero.renglonHueco][tablero.columnaHueco+1]="X "        
            movimientos.append(Puzzle(matrizAux,tablero,tablero.renglonHueco,tablero.columnaHueco+1,"right")) 
         
        
        if tablero.renglonHueco<3 and not tablero.movimientoAnterior=="up"   :        #si la orden fue down quiere decir que no debemos ir para arriba regresariamos         
            matrizAux = copy.deepcopy(tablero.value)        
            matrizAux[tablero.renglonHueco][tablero.columnaHueco]=matrizAux[tablero.renglonHueco+1][tablero.columnaHueco]
            matrizAux[tablero.renglonHueco+1][tablero.columnaHueco]="X "        
            movimientos.append(Puzzle(matrizAux,tablero,tablero.renglonHueco+1,tablero.columnaHueco,"down")) 
        
        
        
        
        if tablero.columnaHueco>0 and not tablero.movimientoAnterior=="right":        #si la orden fue down quiere decir que no debemos ir para arriba regresariamos                                
            matrizAux = copy.deepcopy(tablero.value)
            matrizAux[tablero.renglonHueco][tablero.columnaHueco]=matrizAux[tablero.renglonHueco][tablero.columnaHueco-1]
            matrizAux[tablero.renglonHueco][tablero.columnaHueco-1]="X "        
            movimientos.append(Puzzle(matrizAux,tablero,tablero.renglonHueco,tablero.columnaHueco-1,"left"))   
       
        return  movimientos
    
                                    
    
    #City block distance heuristica para matrices de 4x4 es decir la distancia del tablero que reciba a la configuracion que debe de ser...
    @staticmethod                                                         
    def calculaHeuristica(tablero):      
        renglones = 0         
        heuristica = 0
        for renglon in tablero: 
            columnas = 0           
            for elemento in renglon:                
                if elemento!="X ":  
                    tempo = float(elemento)
                    tempo2=0                  
                    while tempo>4:
                        tempo-=4
                        tempo2+=1 
                    modulo =tempo%5          
                    distanciaRenglon = abs(modulo-columnas-1)                                    
                    distanciaColumna = abs(tempo2-renglones) #se divide entre uno mas para dar el numero de renglon en el que debe estar
                    print(distanciaRenglon + distanciaColumna)                                           
                    heuristica+= distanciaRenglon + distanciaColumna                                                   
                columnas+=1            
            renglones+=1                    
        return heuristica     
            
                      
         
            
        
tableroInicial=[['2 ','3 ','4 ','X '],['1 ','6 ','7 ','8 '],['5 ','10','11','12'],['9 ','13','14','15']]                                                           
print(Puzzle.calculaHeuristica(tableroInicial))                                                                                               
                 
                                                         
                                
        
    
    