# Class to manage printing of hierarchical clusters

# Import
from PIL import Image, ImageDraw

class Print:

  @staticmethod
  def print_clust(cluster, n = 0):
    for i in range(n):
      print ' '
    
    if cluster.id < 0:
      print '-'
    else:
      if cluster.name != None:
        print cluster.name
      else:
        print cluster.id
    
    if cluster.left != None:
      Print.print_clust(cluster.left, n = n + 1) 
    if cluster.right != None:
      Print.print_clust(cluster.right, n = n +1)

  @staticmethod
  def get_height(cluster):
    if (cluster.left == None and cluster.right == None):
      return 1
    else:
      return Print.get_height(cluster.left) + Print.get_height(cluster.right)

  @staticmethod
  def get_depth(cluster):
    if (cluster.left == None and cluster.right == None):
      return 0
    else:
      return max(Print.get_depth(cluster.left), Print.get_depth(cluster.right)) + cluster.distance

  @staticmethod
  def draw_dendrogram(cluster, jpeg = "clusters.jpeg"):
    height = Print.get_height(cluster) * 20
    width = 1200
    depth = Print.get_depth(cluster)

    scaling = float(width - 150) / depth

    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw.line((0, height / 2, 10, height / 2), fill = (255, 0, 0))

    Print.draw_node(draw, cluster, 10, (height /2), scaling)
    image_path = "img/" + jpeg
    img.save("server/" + image_path, 'JPEG')
    return image_path

  @staticmethod
  def draw_node(draw, cluster, x, y, scaling):
    print cluster.id
    if cluster.id < 0:
      h1 = Print.get_height(cluster.left) * 20
      h2 = Print.get_height(cluster.right) * 20
      
      top = y - (h1 + h2) / 2
      bottom = y + (h1 + h2) / 2

      line_length = cluster.distance * scaling

      draw.line((x, top + h1 / 2, x, bottom - h2 / 2), fill = (255, 0 ,0))
      draw.line((x, top + h1 / 2, x + line_length, top + h1 / 2), fill = (255, 0 ,0))
      draw.line((x, bottom - h2 / 2, x + line_length, bottom - h2 / 2), fill = (255, 0 ,0))

      Print.draw_node(draw, cluster.left, x + line_length, top + h1 / 2, scaling)
      Print.draw_node(draw, cluster.right, x + line_length, bottom - h2 / 2, scaling)
    else:
      print cluster.name
      draw.text((x + 5, y - 7), cluster.name, (0, 0, 0))
