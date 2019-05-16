#gaslaw function library
import tkMessageBox

def download_images():
    # In order to fetch the image online
    try:
        import urllib.request as url
    except ImportError:
        import urllib as url
    url.urlretrieve("https://thumbs.gfycat.com/ForsakenValidGiraffe-max-1mb.gif", "balloon.gif")

def errorMessage(a):
    tkMessageBox.showinfo("Warning!", "Error: [ %s ] is not a valid input. \n\nAs these inputs only accepts numbers" % a )
    #print "[",a,"]","is not a number"

def errorMessageZero():
    tkMessageBox.showinfo("Warning!", "Error: [ 0 ] (Zero) is an invalid input")
    #print "Zero is an invalid input"

def errorMessageEmpty():
    tkMessageBox.showinfo("Warning!", "Error: Empty Input(s) detected")
    #print "Empty input(s) is an invalid input"

def isnumber(a, b, c, d):
##    print type(a)
##    print type(b)
##    print type(c)
##    print type(d)
##    print a
##    print b
##    print c
##    print d

    def empty(a, b, c, d):
        if a == "0":
            if str(b).strip() == "" or str(c).strip() == "" or str(d).strip() == "":
                #print "Error nothing in the string"
                return False
            else:
                #print "All good"
                return True

        elif b == "0":
            if str(a).strip() == "" or str(c).strip() == "" or str(d).strip() == "":
                #print "Error nothing in the string"
                return False
            else:
                #print "All good"
                return True

        elif c == "0":
            if str(a).strip() == "" or str(b).strip() == "" or str(d).strip() == "":
                #print "Error nothing in the string"
                return False
            else:
                #print "All good"
                return True

        elif d == "0":
            if str(a).strip() == "" or str(b).strip() == "" or str(c).strip() == "":
                #print "Error nothing in the string"
                return False
            else:
                #print "All good"
                return True

        else:
            #print "empty error"
            return False

    if empty(a, b, c, d) == False:
        errorMessageEmpty()
        return False
    else:
        #print "empty pass"
        pass
    
    try:
        float(a)
    except ValueError:
          try:
              float(a)
          except ValueError:
              errorMessage(a)
              #print "[ a ]","is not a number"
              return False
    try:
        float(b)
    except ValueError:
          try:
              float(b)
          except ValueError:
              errorMessage(b)
              #print "[ b ]","is not a number"
              return False
    try:
        float(c)
    except ValueError:
          try:
              float(c)
          except ValueError:
              errorMessage(c)
              #print "[ c ]","is not a number"
              return False
    try:
        float(d)
    except ValueError:
          try:
              float(d)
          except ValueError:
             errorMessage(d)
             #print "[ d ]","is not a number"
             return False
    if float(a) == 0:
      if float(b) > 0 and float(c) > 0 and float(d) > 0:
          return True
      else:
          errorMessageZero()
          return False
    if float(b) == 0:
      if float(a) > 0 and float(c) > 0 and float(d) > 0:
          return True
      else:
          errorMessageZero()
          return False
    if float(c) == 0:
      if float(a) > 0 and float(b) > 0 and float(d) > 0:
          return True
      else:
          errorMessageZero()
          return False
    if float(d) == 0:
      if float(a) > 0 and float(b) > 0 and float(c) > 0:
          return True
      else:
          errorMessageZero()
          return False

def pvpvCalc(a, p1, v1, p2, v2, R):
    if a == "p1":
        if isnumber("0", v1, p2, v2) == True:
            pres1 = ((abs(float(p2))*abs(float(v2)))/(abs(float(v1))))
            #print pres1
            return str(pres1)+ " Pa"
        else:
            #print "Error one"
            return
    elif a == "v1":
        if isnumber(p1, "0", p2, v2) == True:
            vol1 = ((abs(float(p2))*abs(float(v2)))/(abs(float(p1))))
            #print vol1
            return str(vol1)+ " m3"
        else:
            #print "Error two"
            return
    elif a == "p2":
        if isnumber(p1, v1, "0", v2) == True:
            pres2 = ((abs(float(p1))*abs(float(v1)))/(abs(float(v2))))
            #print pres2
            return str(pres2)+ " Pa"
        else:
            #print "Error three"
            return
    elif a == "v2":
        if isnumber(p1, v1, p2, "0") == True:
            vol2 = ((abs(float(p1))*abs(float(v1)))/(abs(float(p2))))
            #print vol2
            return str(vol2)+ " m3"
        else:
            #print "Error four"
            return
    else:
        return "pvpv Error"

def vtvtCalc(a, cv1, ct1, cv2, ct2, R):
    if a == "v1":
        if isnumber("0", ct1, cv2, ct2) == True:
            cvol1 = ((abs(float(cv2))/abs(float(ct2)))*(abs(float(ct1))))
            #print cvol1
            return str(cvol1)+ "m^3"
        else:
            #print "Error one"
            return
    elif a == "t1":
        if isnumber(cv1, "0", cv2, ct2) == True:
            ctemp1 = (abs(float(cv1))*abs(float(ct2)))/(abs(float(cv2)))
            #print ctemp1
            return str(ctemp1)+ "K"
        else:
            #print "Error two"
            return
    elif a == "v2":
        if isnumber(cv1, ct1, "0", ct2) == True:
            cvol2 = ((abs(float(cv1))/abs(float(ct1)))*(abs(float(ct2))))
            #print cvol2
            return str(cvol2)+ "m^3"
        else:
            #print "Error three"
            return
    elif a == "t2":
        if isnumber(cv1, ct1, cv2, "0") == True:
            ctemp2 = ((abs(float(cv2))*abs(float(ct1)))/(abs(float(cv1))))
            #print ctemp2
            return str(ctemp2)+ "K"
        else:
            #print "Error four"
            return
    else:
        return "vtvt Error"

def ptptCalc(a, lp1, lt1, lp2, lt2, R):
    if a == "p1":
        if isnumber("0", lt1, lp2, lt2) == True:
            lpres1 = ((abs(float(lp2))/abs(float(lt2)))*(abs(float(lt1))))
            #print lpres1
            return str(lpres1)+ "Pa"
        else:
            #print "Error one"
            return
    elif a == "t1":
        if isnumber(lp1, "0", lp2, lt2) == True:
            ltemp1 = ((abs(float(lp1))*abs(float(lt2)))/(abs(float(lp2))))
            #print ltemp1
            return str(ltemp1)+ "K"
        else:
            #print "Error two"
            return
    elif a == "p2":
        if isnumber(lp1, lt1, "0", lt2) == True:
            lpres2 = ((abs(float(lp1))/abs(float(lt1)))*(abs(float(lt2))))
            #print lpres2
            return str(lpres2)+ "Pa"
        else:
            #print "Error three"
            return
    elif a == "t2":
        if isnumber(lp1, lt1, lp2, "0") == True:
            ltemp2 = ((abs(float(lp2))*abs(float(lt1)))/(abs(float(lp1))))
            #print ltemp2
            return str(ltemp2)+ "K"
        else:
            #print "Error four"
            return
    else:
        return "ptpt Error"

def pvnrtCalc(a, p, v, n, t, R):
    if a == "P":
        if isnumber("0", v, n, t) == True:
            pres = (abs(float(n))*8.314*abs(float(t)))/(abs(float(v)))
            #print pres
            return str(pres)+ "Pa"
        else:
            #print "Error one"
            return
    elif a == "V":
        if isnumber(p, "0", n, t) == True:
            vol = (abs(float(n))*8.314*abs(float(t)))/(abs(float(p)))
            #print vol
            return str(vol)+ "m^3"
        else:
            #print "Error two"
            return
    elif a == "n":
        if isnumber(p, v, "0", t) == True:
            mole = (abs(float(p))*abs(float(v)))/(abs(float(p))*8.314)
            #print mole
            return str(mole)+ "Moles"
        else:
            #print "Error three"
            return
    elif a == "T":
        if isnumber(p, v, n, "0") == True:
            temp = (abs(float(p))*abs(float(v)))/(abs(float(n))*8.314)
            #print temp
            return str(temp)+ "K"
        else:
            #print "Error four"
            return
    else:
        return "pvnrt Error"

def BText():
    return u"""Boyle's Law: P\u2081V\u2081 = P\u2082V\u2082
Key:
P\u2081 = Pressure 1, V\u2081 = Volume 1, P\u2082 = Pressure 2, V\u2082 = Volume 2\n
This law states that the pressure of a given mass of an ideal gas is inversely proportional to its volume at constant temperature. 
Mathematically, Boyle's law can be stated as P is directly proportional to 1/V (P \u221D 1/V) or PV = k where  P is the pressure of the gas, V is the volume and k is a constant.
Boyle's law is based on experiments with air, which Robert Boyle considered to be a fluid of particles at rest inbetween small invisible springs. This is no longer the held
wisdom but was a good approximation for the time. Eventually, it was Boyle's assistant Robert Hooke who built the apparatus to test the theory which we know today."""
def CText():
    return u"""Charles Law: V\u2081/T\u2081 = V\u2082/T\u2082
Key:
V\u2081 = Volume 1, T\u2081 = Temperature 1, V\u2082 = Volume 2, T\u2082 = Temperature 2 \n
This law states that the volume of an ideal gas at constant pressure is directly proportional to the absolute temperature.
Mathematically, this can be written as V is directly proportional to T (V \u221D T) , which implies V/T = k or V = kT Where T is temperature, V is volume and k is some non zero constant.
The law was named after Jaques Charles where it was discovered in his unpublished work from 1780s. John Dalton, later on, was the first to show experimentally that the
law generally applied to all gases. The law does imply that at some volume, T will be equal to absolute, 0 Kelvin or -273.15 Celcius, but the law has been proven to fail at some low temperature."""
def LText():
    return u"""Gay-Lussac's Law: P\u2081/T\u2081 = P\u2082/T\u2082
Key:
P\u2081 = Pressure 1, T\u2081 = Temperature 1 ,P\u2082 = Pressure 2, T\u2082 = Temperature 2\n
This law states that the pressure of a given mass of a gas varies directly with the absolute temperature of the gas, when the volume is kept constant. Mathematically, it can be written as P/T = k (P \u221D T),
Where P is pressure, T is temperature and K is a non zero constant. When comparing the same substances under different sets of conditions, it can be written mathematically as P\u2081/T\u2081 = P\u2082/T\u2082  or P\u2081 \u00D7 T\u2082 = P\u2082 \u00D7 T\u2081. 
Guillaume Amontons discovered the law before Gay-Lussac, but given the relative technology available to both men, Amontons was only able to work with air as a gas, whereas Gay-Lussac was able to experiment with multiple types of
common gases, such as oxygen, nitrogen, and hydrogen. Gay-Lussac did attribute his findings to Jacques Charles because he used much of Charles unpublished data from 1787. Hence, the law became known as Charles
law or the Law of Charles and Gay-Lussac."""
def IText():
    return u"""Ideal Gas Law: PV = nRT
Key:
P = Pressure, V = Volume, n = number of moles, R = gas constant which is 8.3144598m\u00B3⋅Pa⋅K\u207B \u00B9⋅mol\u207B \u00B9, T = Temperature\n
The ideal gas law, also called the general gas equation, is the equation of state of a hypothetical ideal gas. It is a good approximation of the behavior of many gases under many conditions, although it has several
limitations. It was first stated by Emile Clapeyron in 1834 as a combination of the empirical Boyle's law, Charles law, Avogadro's law, and Gay-Lussac's law. The law is often written mathematically as PV=nRT
Where P is pressure, V is volume, n is the number of molecules of the gas, R is the Ideal Gas Constant, and T is temperature. The equation of state given here (PV=nRT) applies only to an ideal gas, or as an
approximation to a real gas that behaves sufficiently like an ideal gas. There are in fact many different forms of the equation of state. Since the ideal gas law neglects both molecular size and inter-molecular
attractions, it is most accurate for monatomic gases at high temperatures and low pressures."""

