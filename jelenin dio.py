def ispisiGCODE():
      f = open('output_0001.ngc', 'r')
      Lines = f.readlines()
      koordinate = []
      for t in range(len(Lines)):
            linija = Lines[t]
            linija = linija.split()
            if len(linija) != 0:
                  if linija[0] == 'G01' and linija[1][0] == 'X': 
                        xy = []
                        x = float(linija[1][1:5])
                        y = float(linija[2][1:5])
                        xy.append(x)
                        xy.append(y)
                        xy.append('G01')
                        koordinate.append(xy)
                  elif linija[0] == 'G02':
                        xy = []
                        centerpoint = []
                        x = float(linija[1][1:5])
                        y = float(linija[2][1:5])
                        i = float(linija[4][1:5])
                        j = float(linija[5][1:5])
                        centerpoint.append(i)
                        centerpoint.append(j)
                        xy.append(x)
                        xy.append(y)
                        xy.append('G02')
                        xy.append(centerpoint)
                        koordinate.append(xy)
                  elif linija[0] == 'G03':
                        xy = []
                        centerpoint = []
                        x = float(linija[1][1:5])
                        y = float(linija[2][1:5])
                        i = float(linija[4][1:5])
                        j = float(linija[5][1:5])
                        centerpoint.append(i)
                        centerpoint.append(j)
                        xy.append(x)
                        xy.append(y)
                        xy.append('G03')
                        xy.append(centerpoint)
                        koordinate.append(xy)
      return koordinate


