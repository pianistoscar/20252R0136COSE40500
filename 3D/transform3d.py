class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def translate(self, dx, dy, dz):
        return Vector3D(
            self.x + dx,
            self.y + dy,
            self.z + dz
        )

    def as_tuple(self):
        return (self.x, self.y, self.z)


if __name__ == "__main__":
    v = Vector3D(1, 2, 3)
    v2 = v.translate(3, -1, 2)
    print(v2.as_tuple())
