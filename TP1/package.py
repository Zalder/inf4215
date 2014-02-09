class Package:
    def __init__(self, destination, weight, id):
        self.destination = destination
        self.weight = weight
        self.id = id

    def show(self):
        print 'Package {} : {} kg to {}'.format(self.id, self.weight, self.destination)
