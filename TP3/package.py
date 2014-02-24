class Package:
    def __init__(self, origin, destination, weight, id):
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.id = id

    def show(self):
        print 'Package {} : {} kg to {}'.format(self.id, self.weight, self.destination)
