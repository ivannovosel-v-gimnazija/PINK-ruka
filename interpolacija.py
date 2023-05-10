import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def brzine(vMax, brojTocaka):
    korak = vMax / ((brojTocaka - 1) // 2)
    brzine = list (0 for i in range ((brojTocaka - 1) // 2))
    brzine[0] = korak
    for i in range((brojTocaka - 1) // 2 - 1):
        brzine[i + 1] = brzine[i] + korak
    brzine = brzine + brzine[::-1]
    brzine = [0] + brzine
    if brojTocaka % 2 == 0:
        brzine.insert(brojTocaka // 2, vMax)
    return brzine


def interpolacija (pocX, pocY, krajX, krajY, brojTocaka, vMax):
    tockeX = np.linspace (pocX,krajX,brojTocaka)
    tockeY = np.linspace (pocY,krajY,brojTocaka)
    pomak = (tockeX[1]**2 + tockeY[1]**2)**0.5 - (tockeX[0]**2 + tockeY[0]**2)**0.5
    vrijeme = list (0 for i in range (brojTocaka))
    vrijeme[0] = 0
    for i in range (1, brojTocaka):
        vrijeme[i] = pomak / brzine(vMax, brojTocaka)[i]
    return list(tockeX), list(tockeY), vrijeme
    



    





