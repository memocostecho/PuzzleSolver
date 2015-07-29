import copy
from Tkinter import *
from lib2to3.pytree import convert
from random import sample
from repr import repr



class Puzzle(object):  #es como el constructor de java    

    def __init__(self, value, padre,renglonHueco,columnaHueco,movimientoAnterior):
        self.value = value        
        self.padre = padre
        self.renglonHueco = renglonHueco
        self.columnaHueco = columnaHueco
        self.movimientoAnterior= movimientoAnterior 
              
        
        
    
# def PuzzleHeuristicFactory(self,value,padre,renglonHueco,columnaHueco,movimientoAnterior,heu):
   
    def setheuristic(self,heuristic):
        self.heuristic = heuristic
        
    def setCosto(self,costo):
        self.costo=costo
    
    def setPiezaAMover(self,piezaAMover):
        self.piezaAMover = piezaAMover    
    
    
    
    
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
        
        random =sample(range(4), 4) 
        #random=[randint(1,4) for _ in range(4)]
        #print(random)
        
        for numero in random:           
            if numero== 3 and tablero.renglonHueco>0   and not tablero.movimientoAnterior=="down" :         #si la orden fue down quiere decir que no debemos ir para arriba regresariamos         
                matrizAux = copy.deepcopy(tablero.value)        
                matrizAux[tablero.renglonHueco][tablero.columnaHueco]=matrizAux[tablero.renglonHueco-1][tablero.columnaHueco]
                matrizAux[tablero.renglonHueco-1][tablero.columnaHueco]="X "        
                movimientos.append(Puzzle(matrizAux,tablero,tablero.renglonHueco-1,tablero.columnaHueco,"up"))
            
            
            if numero==0  and tablero.columnaHueco<3 and not tablero.movimientoAnterior=="left":          #si la orden fue down quiere decir que no debemos ir para arriba regresariamos         
                matrizAux = copy.deepcopy(tablero.value)        
                matrizAux[tablero.renglonHueco][tablero.columnaHueco]=matrizAux[tablero.renglonHueco][tablero.columnaHueco+1]
                matrizAux[tablero.renglonHueco][tablero.columnaHueco+1]="X "        
                movimientos.append(Puzzle(matrizAux,tablero,tablero.renglonHueco,tablero.columnaHueco+1,"right")) 
             
            
            if numero==1 and tablero.renglonHueco<3 and not tablero.movimientoAnterior=="up"   :        #si la orden fue down quiere decir que no debemos ir para arriba regresariamos         
                matrizAux = copy.deepcopy(tablero.value)        
                matrizAux[tablero.renglonHueco][tablero.columnaHueco]=matrizAux[tablero.renglonHueco+1][tablero.columnaHueco]
                matrizAux[tablero.renglonHueco+1][tablero.columnaHueco]="X "        
                movimientos.append(Puzzle(matrizAux,tablero,tablero.renglonHueco+1,tablero.columnaHueco,"down")) 
            
                    
            
            if numero==2 and tablero.columnaHueco>0 and not tablero.movimientoAnterior=="right":        #si la orden fue down quiere decir que no debemos ir para arriba regresariamos                                
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
                    #print(distanciaRenglon + distanciaColumna)                                           
                    heuristica+= distanciaRenglon + distanciaColumna                                                   
                columnas+=1            
            renglones+=1                    
        return heuristica     
            

    @staticmethod   
    def drawRec(window,canvas,number,coord,color):
        canvas.create_rectangle(coord, fill=color,tag="pieza%s"%number)
        canvas.create_text((coord[0]+coord[2])/2,(coord[1]+coord[3])/2,text=number,tag="pieza%s"%number)
    
    #crea el puzzle
    @staticmethod
    def drawPuzzle(window,canvas,tablero): 
        matrix = tablero  #matriz inicial
        coord = 0, 0, 120, 120  #coordenadas para el dibujado de cada pieza
        count = 0
        color="red"
        #esto lee la matriz
        for row in matrix:
            if(isinstance(row, list)): 
                #print ("imprimiendo renglon %d" %count)
                for element in row:
                    #print (element)
                    if element == '*':
                        color='yellow'
                    else:
                        color='red'
                    Puzzle.drawRec(window, canvas, element, coord, color)
                    coord = [coord[0]+120,coord[1],coord[2]+120,coord[3]]
                count+=1
                coord = [0,coord[1]+120,120,coord[3]+120]   
            #else:
                #print ("esto no es un renglon no me sirve")
    
    
    @staticmethod
    def moveUp(canvas,id_pieza):
        dx = 0  #delta de desplazamiento
        dy =-3
        # canvas.delete('pieza*') #se elimina el hueco
        beforeMoveCoords = canvas.coords(id_pieza) #se guardan las coords del bloque antes de ser movido
        while True:
            canvas.move(id_pieza, dx, dy)
            canvas.after(20)
            canvas.update()
            # print (canvas.coords(id_pieza)[1])
            if canvas.coords(id_pieza)[1] == beforeMoveCoords[1]-120:
                break
    
    @staticmethod
    def moveDown(canvas,id_pieza):
        dx = 0  #delta de desplazamiento
        dy =3
        #canvas.delete('pieza*') #se elimina el hueco
        beforeMoveCoords = canvas.coords(id_pieza) #se guardan las coords del bloque antes de ser movido
        while True:
            canvas.move(id_pieza, dx, dy)
            canvas.after(20)
            canvas.update()
            #print (canvas.coords(id_pieza)[1])
            if canvas.coords(id_pieza)[1] == beforeMoveCoords[1]+120:
                break
    
    @staticmethod    
    def moveRigth(canvas,id_pieza):
        dx = 3  #delta de desplazamiento
        dy =0
        canvas.delete('pieza*') #se elimina el hueco
        beforeMoveCoords = canvas.coords(id_pieza) #se guardan las coords del bloque antes de ser movido
        while True:
            canvas.move(id_pieza, dx, dy)
            canvas.after(20)
            canvas.update()
            #print (canvas.coords(id_pieza)[0])
            if canvas.coords(id_pieza)[0] == beforeMoveCoords[0]+120:
                break
     
    @staticmethod    
    def moveLeft(canvas,id_pieza):
        dx = -3  #delta de desplazamiento
        dy =0
        canvas.delete('pieza*') #se elimina el hueco
        beforeMoveCoords = canvas.coords(id_pieza) #se guardan las coords del bloque antes de ser movido
        while True:
            canvas.move(id_pieza, dx, dy)
            canvas.after(20)
            canvas.update()
            #print (canvas.coords(id_pieza)[0])
            if canvas.coords(id_pieza)[0] == beforeMoveCoords[0]-120:
                break
       
    @staticmethod
    def animaResultado(resultado,tableroInicial):
        delay=5
        root = Tk()
    
#parametros de la ventana
        root.title("Puzzle")
        root.geometry("500x500+500+1300")

        C = Canvas(root,width=480,height=480,bg="gray")#
        C.pack()  #pone el canvas en la ventana
        Puzzle.drawPuzzle(root, C,tableroInicial)
        C.delete("piezaX")
                
        for tablerin in resultado:                                                                      
            #if((resultado.index(tablerin)-1)>=0):
            tablerinAnterior=resultado[resultado.index(tablerin)-1]
            
            if(tablerin.movimientoAnterior == "Final?"):
                if(tablerinAnterior.renglonHueco==2): #quiere decir que esta en el penultimo renglon entonces moveremos a la derecha.
                    tablerin.movimientoAnterior="down"
                if(tablerinAnterior.columnaHueco==2): #quiere decir que esta en la penultima columna entonces moveremos a la derecha.
                    tablerin.movimientoAnterior="right"    
            
            if (tablerin.movimientoAnterior == "up"):
                huecoPasado = [resultado[resultado.index(tablerin)-1].renglonHueco,resultado[resultado.index(tablerin)-1].columnaHueco]                                
                Puzzle.moveDown(C,"pieza%s"%int(tablerinAnterior.value[huecoPasado[0]-1][huecoPasado[1]]))                                                
                C.after(delay)
                                                
            elif(tablerin.movimientoAnterior == "down"):                
               
                
                huecoPasado = [resultado[resultado.index(tablerin)-1].renglonHueco,resultado[resultado.index(tablerin)-1].columnaHueco]
                
                
                                             
                Puzzle.moveUp(C,"pieza%s"%int(tablerinAnterior.value[huecoPasado[0]+1][huecoPasado[1]]))                                                
                C.after(delay) 
                
            elif(tablerin.movimientoAnterior == "right"):                
                huecoPasado = [resultado[resultado.index(tablerin)-1].renglonHueco,resultado[resultado.index(tablerin)-1].columnaHueco]                                
                Puzzle.moveLeft(C,"pieza%s"%int(tablerinAnterior.value[huecoPasado[0]][huecoPasado[1]+1]))                                                
                C.after(delay) 
            
            elif(tablerin.movimientoAnterior == "left"):                
                huecoPasado = [resultado[resultado.index(tablerin)-1].renglonHueco,resultado[resultado.index(tablerin)-1].columnaHueco]                                
                Puzzle.moveRigth(C,"pieza%s"%int(tablerinAnterior.value[huecoPasado[0]][huecoPasado[1]-1]))                                                
                C.after(delay) 
                
           
        root.mainloop()  
             
                
            
    #tableroInicial=[['2 ','3 ','4 ','X '],['1 ','6 ','7 ','8 '],['5 ','10','11','12'],['9 ','13','14','15']]                                                           
    #print(Puzzle.calculaHeuristica(tableroInicial))                                                                                               
                     
                                                             
                                    
            
        
        