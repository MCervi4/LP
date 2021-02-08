# Generated from Skyline.g by ANTLR 4.5.1
from antlr4 import *

from skyline import Skyline

if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    #inicialitzo la classe amb una taula de simbols
    def __init__(self):
        self.ts = {}
        
    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        #print ("ROOT")
        
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by SkylineParser#asig.
    def visitAsig(self, ctx:SkylineParser.AsigContext):
        #print ("ASIG")
        
        nom = ctx.VAR().getText()
        sky = self.visit(ctx.getChild(2))
        
        self.ts[nom] = sky
        return  sky


    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        #print ("EXPR")
        numfills = ctx.getChildCount()
        
        #creacio o VAR
        if (numfills == 1):
            if (ctx.VAR()): #VAR
                #print ("VAR")
                nom = ctx.VAR().getText()
                return self.ts[nom]
            else: #creacio
                #print ("EXPR_CREACIO")
                return self.visit(ctx.getChild(0))
        #reflexio (-a)
        elif (numfills == 2):
            #print ("REFLEXIO")
            s = self.visit(ctx.getChild(1))
            s.reflexio()
            return s
        #parentesis o operacio entre 2 expr
        else:
            l = [n for n in ctx.getChildren()]
            if (l[0].getText() == '('): #parentesis
                #print ("PARENTESIS")
                return self.visit(ctx.getChild(1))
            else: #operacions
                
                #print ("OPERACIO")
                if (ctx.PER()): #PER
                    #print ("PER")
                    if (ctx.NUM()): #expr PER NUM
                        #print ("PER NUM")
                        mult = int( ctx.NUM().getText() )
                        s = self.visit(ctx.getChild(0))
                        
                        s.replicacio(mult)
                        return s
                    else: #expr PER expr
                        #rint ("PER expr")
                        #aqui aniria la interseccio
                        pass
                        
                elif (ctx.MES()): #MES
                    #print ("MES")
                    
                    if (ctx.NUM()): #expr MES NUM
                        #print ("MES NUM")
                        desp = int( ctx.NUM().getText() )
                        s = self.visit(ctx.getChild(0))
                        
                        s.desplacament_dreta(desp)
                        return s
                    else: #expr MES expr
                        #print ("MES expr")
                        #aqui aniria la unio
                        pass
                
                else: #MENYS (expr MENYS NUM)
                    #print ("MENYS")
                    desp = int( ctx.NUM().getText() )
                    s = self.visit(ctx.getChild(0))
                    s.desplacament_esquerra(desp)
                    return s
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#creacio_simple.
    def visitCreacio_simple(self, ctx:SkylineParser.Creacio_simpleContext):
        #print ("CREACIO_SIMPLE")
        l = [n for n in ctx.getChildren()]
        sky = Skyline()
        sky.crear_simple (int(l[1].getText()), int(l[3].getText()), int(l[5].getText()))
        #ar=sky.getArea()
        #al=sky.getAlcada()
        #print(ar, al)
        return sky


    # Visit a parse tree produced by SkylineParser#creacio.
    def visitCreacio(self, ctx:SkylineParser.CreacioContext):
        l = [n for n in ctx.getChildren()]
        #print ("CREACIO")
        if (l[0].getText() == '['): #creacio composta
            #print ("COMPOSTA")
            num_creacions = (ctx.getChildCount() - 2 ) / 2
            for i in range(0, num_creacions-1):
                s = self.visit(ctx.getChild(1*i+1))
        elif (l[0].getText() == '{'): #creacio aleatoria
            #print ("ALEATORIA")
            l = [n for n in ctx.getChildren()]
            sky = Skyline()
            sky.crear_aleatori (int(l[1].getText()), int(l[3].getText()), int(l[5].getText()), int(l[7].getText()), int(l[9].getText()))
            return sky
        else: #creacio simple
            #print ("SIMPLE")
            return self.visit(ctx.getChild(0))
        return self.visitChildren(ctx)



del SkylineParser