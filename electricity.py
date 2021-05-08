from cmath import*
from numpy import conj
class elec(object):

    def __init__(self):
        pass
    def parallel(self,x,y):
        self.x,self.y=x,y
        return x*y/(x+y)
    def deg(self,radian):
        self.radian= radian
        return radian*360/(2*pi)
    def rad(self,degree):
        self.degree= degree
        return degree*2*pi/360
    def Smax(self,Rs,Xs,Xms,Xlr,Rr):
        '''Rs,Xs,Xms,Xrr,Rr'''
        Xrr=Xlr+Xms
        Xss=Xs+Xms
        print(Xrr,Xss)
        return Rr*sqrt((Rs**2+Xss**2)/((Xms**2-Xss*Xrr)**2+(Rs*Xrr)**2))
    def Andaze(self,com):
        return polar(com)[0]
    def Phase(self,com):
        return polar(com)[1]
    def MS(self,Rs,Xls,Xms,Rr,Xlr,V):
        s=.06
        wm=(1-s)*4*pi*50/6
        Rf=Rr/(2*s)
        Rb=Rr/(2*(2-s))
        zf= self.parallel(Xms/2,Rf+Xlr/2)
        zb= self.parallel(Xms/2,Rb+Xlr/2)
        zin=Rs+Xls+zf+zb
        Is=V/zin
        Pin=(V*conj(Is)).real
        Irf=Is*((Xms/2)/(Xms/2+Xlr/2+Rf))
        Irb=Is*((Xms/2)/(Xms/2+Xlr/2+Rb))
        Pgf=self.Andaze(Irf)**2*Rf
        Pgb=self.Andaze(Irb)**2*Rb
        Pmech=(1-s)*(Pgf-Pgb)
        Tout=(Pmech-100)/wm
        n=(Pmech-100)/Pin
        print("Pin={0},Irf={1},Irb={2},Pgf={3},Pgb={4},Pmech={5},Tout={6},n={7},zin={8},Iin={9}".format(Pin,polar(Irf),polar(Irb),Pgf,Pgb,Pmech,Tout,n,polar(zin),polar(Is)))
    def Azm(self,Rs,Vbrt,Ibrt,Pbrt,Inl,Vnl,Pnl):
        Rbrt=Pbrt/Ibrt**2
        Rr=Rbrt-Rs
        Zbrt=Vbrt/Ibrt
        Xbrt=sqrt(Zbrt**2-Rbrt**2)
        Xls=Xlr=Xbrt/2
        Rnl=Pnl/Inl**2
        Rrot=Rnl-(Rs+Rr/4)
        Znl=Vnl/Inl
        Xnl=sqrt(Znl**2-Rnl**2)
        Xms=2*(Xnl-Xls-Xlr/2)
        Prot=Rrot*Inl**2
        Protn=Rrot*Ibrt**2
        print("Rbrt={0},Zbrt={1},Xbrt={2},Xls=Xlr={3},Rnl={4},Rrot={5},Rr={6},Znl={7},Xms={8},Prot={9},Protn={10}".format(Rbrt,Zbrt,Xbrt,Xls,Rnl,Rrot,Rr,Znl,Xms,Prot,Protn))
    def Azm2(self,Vbrt,Ibrt,Pbrt,Inl,Vnl,Pnl):
        Rbrt=Pbrt/Ibrt**2
        Rr=Rs=Rbrt/2
        Zbrt=Vbrt/Ibrt
        Xbrt=sqrt(Zbrt**2-Rbrt**2)
        Xls=Xlr=Xbrt/2
        Rnl=Pnl/Inl**2
        Rrot=Rnl-(Rs+Rr/4)
        Znl=Vnl/Inl
        Xnl=sqrt(Znl**2-Rnl**2)
        Xms=2*(Xnl-Xls-Xlr/2)
        Prot=Rrot*Inl**2
        Protn=Rrot*Ibrt**2
        PS_cu_n=Rs*Ibrt**2
        print(f"Ps_cu={PS_cu_n}")
        print("Rbrt={0},Zbrt={1},Xbrt={2},Xls=Xlr={3},Rnl={4},Rrot={5},Rr={6},Znl={7},Xms={8},Xnl={9},Protn={10}".format(Rbrt,Zbrt,Xbrt,Xls,Rnl,Rrot,Rr,Znl,Xms,Xnl,Protn))
    def AzA(self,VA,IA,PA,VM,IM,PM):
        f=50
        Vph=220
        Rm=PM/IM**2
        Zm=VM/IM
        Xm=sqrt(Zm**2-Rm**2)
        Ra=PA/IA**2
        Za=VA/IA
        Xa=sqrt(Za**2-Ra**2)
        Ia=Vph/complex(Ra,Xa)
        Im=Vph/complex(Rm,Xm)
        Ts=self.Andaze(Ia)*self.Andaze(Im)*sin(abs(polar(Ia)[1]-polar(Im)[1]))
        Ra_opt=Xa*(1+cos(polar(Im)[1]))/(-sin(polar(Im)[1]))
        Ra_start=Ra_opt-Ra
        Ia_new=Vph/complex(Ra_opt,Xa)
        Ts2=self.Andaze(Im)*self.Andaze(Ia_new)*sin(abs(polar(Im)[1]-polar(Ia_new)[1]))
        Xc_opt=Xa+Ra*Rm/(Zm+Xm)
        C_opt=1/(Xc_opt*2* pi*f)*10**6
        Ia_c=Vph/complex(Ra,Xa-Xc_opt)
        Ca=1/(2*pi*f*Xa)*10**6
        Ts3= self.Andaze(Ia_c)*self.Andaze(Im)*sin(abs(self.Phase(Ia_c)-self.Phase(Im)))
        Ts4=Vph/Ra*self.Andaze(Im)*sin(abs(self.Phase(Im)))
        print("Rm={0},Zm={1},Xm={2},Ra={3},Za={4},Xa={5},Ia={6},Im={7},Ts={8}".format(Rm,Zm,Xm,Ra,Za,Xa,polar(Ia),polar(Im),Ts))
        print("-----------------------------------------------")
        print("Ra-opt={0},Ra_start={1},Ia_new={2},Ts2={3},Ts2/Ts1={4}".format(Ra_opt,Ra_start,polar(Ia_new),Ts2,Ts2/Ts))
        print("-----------------------------------------------")
        print("Xc_opt={0},Copt={1}microFarad,Ia_c={2},Ts3={3},Ts3/Ts2={4},Ts3/Ts1={5}".format(Xc_opt,C_opt,polar(Ia_c),Ts3,Ts3/Ts2,Ts3/Ts))
        print("-----------------------------------------------")
        print("Ca={0},Ia={1},Ts4={2},Ts4/Ts3={3}".format(Ca,Vph/Ra,Ts4,Ts4/Ts3))
    def emt1(self,VBRTm,IBRTm,PBRTm,VBRTa,IBRTa,PBRTa):
        Rm=PBRTm/IBRTm**2
        Zm=VBRTm/IBRTm
        Xm=sqrt(Zm**2-Rm**2)
        Ra=PBRTa/IBRTa**2
        Za=VBRTa/IBRTa
        Xa=sqrt(Za**2-Ra**2)
        print(f"Rm={Rm},Zm={Zm},Xm={Xm},Ra={Ra},Za={Za},Xa={Xa}")
    def emt2(self,Xm,Rm,Xa,Ra,Vph,f):
        Ia=Vph/complex(Ra,Xa)
        Im=Vph/complex(Rm,Xm)
        Zm=self.Andaze(complex(Rm,Xm))
        Ts1=self.Andaze(Im)*self.Andaze(Ia)*sin(abs(polar(Im)[1]-polar(Ia)[1]))
        Ra_opt=Xa*(1+cos(polar(Im)[1]))/(-sin(polar(Im)[1]))
        Ra_start=Ra_opt-Ra
        Ia_new=Vph/complex(Ra_opt,Xa)
        Ts2=self.Andaze(Im)*self.Andaze(Ia_new)*sin(abs(polar(Im)[1]-polar(Ia_new)[1]))
        Xc_opt=Xa+Ra*Rm/(Zm+Xm)
        C_opt=1/(Xc_opt*2* pi*f)*10**6
        Ia_c=Vph/complex(Ra,Xa-Xc_opt)
        Ts3= self.Andaze(Ia_c)*self.Andaze(Im)*sin(abs(self.Phase(Ia_c)-self.Phase(Im)))
        print(f"Ia={polar(Ia)},Im={polar(Im)},Z,={Zm},Ra_opt={Ra_opt},Ia_new={polar(Ia_new)}\n,Ts1={Ts1},Xc_opt={Xc_opt}")
        print(f"C_opt={C_opt},Ia_c={polar(Ia_c)},Ts2={Ts2},Ra_start={Ra_start},Ts3={Ts3}")
        print(f"Ts3/Ts1={Ts3/Ts1},Ts2/Ts1={Ts2/Ts1}")
    def So(self,R1m,X1m,Xm,R1a,X1a,Rr,xlr):
        s=1
        a=1
        Rf=Rr/(2*s)
        Rb=Rr/(2*(2-s))
        Zf=self.parallel(1J*Xm/2,complex(Rf,xlr/2))
        Zb=self.parallel(1j*Xm/2,complex(Rb,xlr/2))
        print("Zf={0},Zb={1}".format(Zf,Zb))
    def asd(self,Xa,Ra,Xm,Rm):
        Vph=230
        teta=70/360*2*pi
        Ia=Vph/complex(Ra,Xa)
        Im=Vph/complex(Rm,Xm)
        Xc=0
        while(True):
            if(abs(self.Phase(Ia)-self.Phase(Im)))<teta+0.1 and (abs(self.Phase(Ia)-self.Phase(Im)))>teta-0.1:
                print(Xc)
                break
            Ia=Vph/complex(Ra,Xa-Xc)
            Xc+=1
    def electrod(self,ro,L,d):
        return ro/(2*pi*L)*(log(8*L/d)-1)

a=elec()
zf=a.parallel(60j,complex(50,2))
zb=a.parallel(60j,complex(1.54,2))
z=.1+.4j+a.parallel(2.51j,complex(.25/.38,.47))
print(polar(z))
