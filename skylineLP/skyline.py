import random
from matplotlib import pyplot as plot

class Skyline:
    
    
    #constructor
    def __init__(self):
        self.area = 0
        self.alcada = 0
        self.edificis = []  #llista de tuples
        
    #GETERS
    
    def getArea(self):
        return self.area
    
    def getAlcada(self):
        return self.alcada
    
    def getEdificis(self):
        return self.edificis
    
    #SETERS
        
    def setArea(self, area):
        self.area = area
        
    def setAlcada(self, alcada):
        self.alcada = alcada
        
    def setEdificis(self, edificis):
        seld.edificis = edificis
        
    #CREADORS
    
    #crea un edifici simple
    def crear_simple(self, xmin, alcada, xmax):
        if self.control(alcada, xmin, xmax):
            self.edificis.append( (xmin, alcada, xmax) )
            self.plot_edifici(xmin,alcada,xmax)
            #actualitzo area i alcada
            if (alcada>self.alcada):
                self.alcada = alcada
            self.area += (xmax-xmin)*alcada
                
        #print ("OK")
        
    #crea edificis compostos
    def crear_compost(self, ll_edificis):
        for i in (ll_edificis):
            self.crear_simple(i[0], i[1], i[2])
        
    #crea n edificis aleatoris
    def crear_aleatori(self, n, h, w, xmin, xmax):
        if self.control(h, xmin, xmax):
            i = 0
            while i < n:
                self.crear_1_aleatori(h, w, xmin, xmax)
                i+=1
            
    def crear_1_aleatori(self, h, w, xmin, xmax):
        alcada = random.randint(1,h)
        amplada = random.randint(1,w)
        pos_ini = random.randint(xmin,xmax)
        self.edificis.append( (pos_ini, alcada, pos_ini+amplada ) )
        self.plot_edifici(xmin,alcada,xmax)
        #actualitzo area i alcada
        if (alcada>self.alcada):
            self.alcada = alcada
        self.area += amplada*alcada
        
    #controla que xmax>xmin i que alcada>=0
    def control(self, alcada, xmin, xmax):
        if ( (alcada > 0) and (xmin < xmax) ):
            return True
        return False
        
    #CALCULADORS
    
    #calcula i actualitza la area de tot el skyline. <es pot ficar return per retornarla si fa falta>
    def calcula_area(self):
        area_total = 0
        for edifici in self.edificis:
            area_edifici = (edifici[2]-edifici[0])*edifici[1]
            area_total += area_edifici
        self.area = area_total
        
    #calcula i actualitza la alcada total del skyline
    def calcula_alcada(self):
        alcada_max = 0
        for edifici in self.edificis:
            if alcada_max < edifici[1]:
                alcada_max = edifici[1]
        self.alcada = alcada_max


    #CONSTRUCCIO PLOT
    
    #dibuix d un edifici
    def plot_edifici(self, xmin, alcada, xmax):
        edifici = plot.Rectangle( (xmin,0), width=xmax-xmin, height=alcada, facecolor="red" )
        ax = plot.gca()
        ax.add_patch(edifici)
        plot.axis("scaled")
        plot.savefig('imatge')
        
    #dibuix de tot el skyline
    def plot_general(self):
        for edifici in self.edificis:
            self.plot_edifici(edifici[0], edifici[1], edifici[2])
    
    #OPERACIONS
    
    #desplacament a la dreta del skyline desp posicions
    def desplacament_dreta(self, desp):
        edificisnous = []
        for edifici in self.edificis:
            nou = ( edifici[0]+desp, edifici[1], edifici[2]+desp)
            edificisnous.append(nou)
        self.edificis = edificisnous
        #abans de dibuixar el plot borro el que tenia
        plot.clf()
        plot.savefig('imatge')
        self.plot_general()
        
    #desplacament a la esquerra del skyline desp posicions
    def desplacament_esquerra(self, desp):
        edificisnous = []
        for edifici in self.edificis:
            nou = ( edifici[0]-desp, edifici[1], edifici[2]-desp)
            edificisnous.append(nou)
        self.edificis = edificisnous
        #abans de dibuixar el plot borro el que tenia
        plot.clf()
        plot.savefig('imatge')
        self.plot_general()
        
    #skyline reflectit
    def reflexio(self):
        xmin_tot = self.x_minima()
        xmax_tot = self.x_maxima()
        edificisnous = []
        for edifici in self.edificis:
            nou = ( (xmax_tot - edifici[0] + xmin_tot), edifici[1], (xmax_tot - edifici[2] + xmin_tot) )
            edificisnous.append(nou)
        self.edificis = edificisnous
        #abans de dibuixar el plot borro el que tenia
        plot.clf()
        plot.savefig('imatge')
        self.plot_general()
        
        
    #replicacio n vegades del skyline
    def replicacio(self, mult):
        
        tamany_sky = (self.x_maxima() - self.x_minima() )
        for j in range(len(self.edificis)):
            for i in range(1, mult):
                edifici = self.edificis[j]
                nou = (edifici[0]+tamany_sky*i, edifici[1], edifici[2]+tamany_sky*i)
                self.edificis.append( nou )
        self.area *= mult
        #abans de dibuixar el plot borro el que tenia
        plot.clf()
        plot.savefig('imatge')
        self.plot_general()
        
        
    #et fa la unio entre 2 skylines
    def unio(self, otro):
        sky = Skyline()
        sky.edificis = []
        sky.edificis.extend(self.edificis)
        sky.edificis.extend(otro.edificis)
        sky.alcada = max (self.alcada, otro.alcada)
        sky.area = self.area+otro.area
        return sky
    
    #et fa la interseccio entre 2 skylines 
    #def interseccio(self):
    
        
    #FUNCIONS AUXILIARS
    
    #calcula la x mes petita del skyline
    def x_minima(self):
        x_min = 999999
        for edifici in self.edificis:
            if x_min > edifici[0]:
                x_min = edifici[0]
        return x_min
    
    #calcula la x mes gran del skyline
    def x_maxima(self):
        x_max = -999999
        for edifici in self.edificis:
            if x_max < edifici[2]:
                x_max = edifici[2]
        return x_max
    
        