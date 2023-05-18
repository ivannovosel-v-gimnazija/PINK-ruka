def ispisiGCODE():
      f = open('output_0001.ngc', 'r')
      Lines = f.readlines()
      for i in range(14):
            Lines.remove(Lines[i])
      koordinate = []
      for i in range(len(Lines)):
            linija = Lines[i]
            if linija[0:3] == 'G01':
                  xy = []
                  x = float(linija[5:8])
                  y = float(linija[17:20])
                  xy.append(x)
                  xy.append(y)
                  xy.append('G01')
                  koordinate.append(xy)
            elif linija[0:3] == 'G02':
                  xy = []
                  x = float(linija[5:8])
                  y = float(linija[17:20])
                  xy.append(x)
                  xy.append(y)
                  xy.append('G02')
                  koordinate.append(xy)
            elif linija[0:3] == 'G03':
                  xy = []
                  x = float(linija[5:8])
                  y = float(linija[17:20])
                  xy.append(x)
                  xy.append(y)
                  xy.append('G03')
                  koordinate.append(xy)
      return koordinate


