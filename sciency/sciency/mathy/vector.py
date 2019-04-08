class Vector:
    def __init__(self, xp=0, yp=0, zp=0):
        self.x = xp
        self.y = yp
        self.z = zp
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getZ(self):
        return self.z
    def print_vector(self):
        x_str, y_str, z_str = str(self.x), "", ""
        if (self.y > 0):
            y_str = "+{}".format(self.y)
        else:
            y_str = str(self.y)
        if (self.z > 0):
            z_str = "+{}".format(self.z)
        else:
            z_str = str(self.z)
        print("({}i{}j{}k)".format(x_str, y_str, z_str))
    def get_magnitude(self):
        magnitude = pow(pow(self.x, 2)+pow(self.y, 2)+pow(self.z, 2), 0.5)
        return magnitude
    def get_unit_vector(self):
        magnitude = self.get_magnitude()
        unit_vector = Vector((self.x)/(magnitude), (self.y)/(magnitude), (self.z)/(magnitude))
        return unit_vector

def add_vectors(v1, v2):
    x, y, z = v1.getX()+v2.getX(), v1.getY()+v2.getY(), v1.getZ()+v2.getZ()
    resultant_vector = Vector(x, y, z)
    return resultant_vector

def subtract_vectors(v1, v2):
    x, y, z = v1.getX()-v2.getX(), v1.getY()-v2.getY(), v1.getZ()-v2.getZ()
    resultant_vector = Vector(x, y, z)
    return resultant_vector

def get_dot_product(v1, v2):
    dot_product = v1.getX()*v2.getX() + v1.getY()*v2.getY() + v1.getZ()*v2.getZ()
    return dot_product
