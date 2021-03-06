# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
#from ...output import Output,OutputMove,OutputFigure,ofR,ofB,ofK,ofN,ofP,ofQ
from .. import *
# For now, the only real output considered will be an NXT-based machine.
import nxt.locator
from nxt.motor import Motor,PORT_A,PORT_B,PORT_C
class Reality(Output):
	def __init__(self,kostkaid="00:16:53:07:F8:5B",homepos=(0,0),pos=(0,0)):
		self.kostkaid = kostkaid
                self.homepos=homepos
                self.pos=pos
	def __enter__(self):
		self.brick = nxt.locator.find_one_brick(self.kostkaid)
		self.motfile = Motor(self.brick,PORT_A)
		self.motrank = Motor(self.brick,PORT_B)
		self.motz = Motor(self.brick,PORT_C)
		return self
	def __exit__(self, exc_type, exc_val, exc_tb):
            self.motx.idle()
            self.moty.idle()
            self.motz.idle()
            print exc_type,exc_val,exc_tb
        def goto(self,loc): print "goto ",loc
        def lift(self,hchwyt,hlift): print "lifing from ",hchwyt," to ",hlift
        def place(self,ileopuscic): print "opuszczanie o ",ileopuscic," , placing"
        def home(self): print "----homing----" ; self.goto(self.HOMEpos)
class RealMove(OutputMove):
	PROPERMACHINE = Reality
	def __init__(self,maszyna,typ,skad,dokad):
		assert isinstance(maszyna,reality),"not isinstance(maszyna,reality)"
		move.__init__(self,maszyna,typ,skad,dokad)
class RealFigure(OutputFigure):
	PROPERMACHINE = Reality
	def __init__(self,maszyna,figheight,pullheight):
		assert isinstance(maszyna,reality),"not isinstance(maszyna,reality)"
		figure.__init__(self,maszyna,figheight,pullheight)
class RealSquare(OutputSquare):
    def __init__(self,maszyna,loc):
        OutputSquare.__init__(self,maszyna)
        self.loc=loc
class RealBoardSquare(RealSquare, OutputBoardSquare):
    def __init__(self,maszyna,bsqpos,loc):
        RealSquare.__init__(self,maszyna,loc)
        OutputBoardSquare.__init__(self,maszyna,bsqpos)
class RealResCapdSquare(RealSquare, OutputResCapdSquare):
    def __init__(self,maszyna,num,loc):
        RealSquare.__init__(self,maszyna,loc)
        OutputResCapdSquare.__init__(self,maszyna,num)
class RealReserveSquare(RealResCapdSquare): pass
class RealWhiteReserveSquare(RealReserveSquare): pass
class RealBlackReserveSquare(RealReserveSquare): pass
class RealCapturedSquare(RealResCapdSquare): pass
class RealCapturedWhiteSquare(RealCapturedSquare): pass
class RealCapturedBlackSquare(RealCapturedSquare): pass
class rfR(ofR, RealFigure):
	FHE = 1; PHE = 2
        def __init__(self,maszyna):
            RealFigure.__init__(self,maszyna,self.FHE,self.PHE)
class rfN(ofN, RealFigure):
	FHE = 1; PHE = 2
        def __init__(self,maszyna):
            RealFigure.__init__(self,maszyna,self.FHE,self.PHE)
class rfB(ofB, RealFigure):
	FHE = 1; PHE = 2
        def __init__(self,maszyna):
            RealFigure.__init__(self,maszyna,self.FHE,self.PHE)
class rfQ(ofQ, RealFigure):
	FHE = 1; PHE = 2
        def __init__(self,maszyna):
            RealFigure.__init__(self,maszyna,self.FHE,self.PHE)
class rfK(ofK, RealFigure):
	FHE = 1; PHE = 2
        def __init__(self,maszyna):
            RealFigure.__init__(self,maszyna,self.FHE,self.PHE)
class rfP(ofP, RealFigure):
	FHE = 1; PHE = 2
        def __init__(self,maszyna):
            RealFigure.__init__(self,maszyna,self.FHE,self.PHE)
