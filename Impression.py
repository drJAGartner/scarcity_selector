import numpy as np

class Impression:
    # define a campaign, pass in a list of tuples to be
    # the cr and ctr for a given campaign 
    def __init__(self, *args):
        self.targets = []
        for a in args[0]:
            self.targets.append(a)

    def n_campaigns(self):
        return len(self.targets) + 1
    
    def get_pred(self, n, var):
        if n > self.n_campaigns():
            print "Trying to get an out of range campaign"
            return None
        if var == 'cr':
            return self.targets[n][0]
        elif var == 'ctr':
            return self.targets[n][1]
        else:
            print "Not a valid variable"
            return None

    def is_success(self, n, var):
        if n > self.n_campaigns():
            print "Trying to get an out of range campaign"
            return None
        if var == 'cr':
            return self.targets[n][0] > np.random.rand()
        elif var == 'ctr':
            return self.targets[n][1] > np.random.rand()
        else:
            print "Not a valid variable"
            return None

