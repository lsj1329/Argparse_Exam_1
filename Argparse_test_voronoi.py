import argparse
from PIL import Image
import random
import math

parser = argparse.ArgumentParser()
parser.add_argument('X',type=int,help="You to decide how many times to draw")
parser.add_argument('Y',type=int,help="You to decide how many times to draw")
parser.add_argument('L',type=int,help="You to decide how many times to draw")
args = parser.parse_args()
X = args.X
Y = args.Y
L = args.L

def generate_voronoi_diagram(width, height, num_cells):
  image = Image.new("RGB", (width, height))
  putpixel = image.putpixel
  imgx, imgy = image.size
  nx = []
  ny = []
  nr = []
  ng = []
  nb = []
  for i in range(num_cells):
    nx.append(random.randrange(imgx))
    ny.append(random.randrange(imgy))
    nr.append(random.randrange(256))
    ng.append(random.randrange(256))
    nb.append(random.randrange(256))

  for y in range(imgy):
    for x in range(imgx):
      dmin = math.hypot(imgx, imgy)
      j=-1

      for i in range(num_cells):

        d = math.hypot(nx[i]-x, ny[i]-y)
        if d < dmin:
          dmin = d
          j = i
      putpixel((x, y), (nr[j], ng[j], nb[j]))

  image.save("Voronoi.png", "PNG")
  image.show()



if __name__=="__main__":
  generate_voronoi_diagram(X, Y, L)
