import numpy as np
from ScarcitySelector import ScarcitySelector
from Impression import Impression


def sim1():
    n_camp = 3
    targets = [(.005, .01) for i in range(n_camp)]
    print "Targets:"
    for t in targets:
        print "\t", t
    print "Create selectors for all objects for all targets"
    selectors = [ScarcitySelector(i[0], i[1], .5, .05) for i in targets]

    print "Simulating 1000000 Potential opportunities"
    for i in range(1000000):
        preds = [(np.random.rand()*.012, np.random.rand()*.02) for ii in range(n_camp)]
        imps = Impression(preds)
        l_oc = [selectors[ii].base_opportunity_cost(preds[ii][0], preds[ii][1]) for ii in range(n_camp)]
        lowest = l_oc.index(min(l_oc))

        if l_oc[lowest] <= 1:
            selectors[lowest].choose_opportunity()
            b_click = imps.is_success(lowest, 'ctr')
            if b_click is True:
                selectors[lowest].success(1)
                b_conv = imps.is_success(lowest, 'cr')
                if b_conv is True:
                    selectors[lowest].success(2)

    for s in selectors:
        s.stats()

    return zip(targets, map(lambda x: x.rates(), selectors))

def sim2():
    n_camp = 3
    targets = [(.005, .01), (.0055, .01), (.005, .011)]

    print "Targets:"
    for t in targets:
        print "\t", t
    print "Create selectors for all objects for all targets"
    selectors = [ScarcitySelector(i[0], i[1], .5, .05) for i in targets]

    print "Simulating Potential opportunities"
    for i in range(1000000):
        cps = (np.random.rand()*.012, np.random.rand()*.02)
        preds = [cps for ii in range(n_camp)]
        imps = Impression(preds)
        l_oc = [selectors[ii].base_opportunity_cost(preds[ii][0], preds[ii][1]) for ii in range(n_camp)]
        lowest = l_oc.index(min(l_oc))

        if l_oc[lowest] <= 1:
            selectors[lowest].choose_opportunity()
            b_click = imps.is_success(lowest, 'ctr')
            if b_click is True:
                selectors[lowest].success(1)
                b_conv = imps.is_success(lowest, 'cr')
                if b_conv is True:
                    selectors[lowest].success(2)

    for s in selectors:
        s.stats()

    return zip(targets, map(lambda x: x.rates(), selectors))


#def sim2():

if __name__ == '__main__':
    print 'Simulation 1, 3 random campaigns'
    sim1()
    print 'Simulation 2, 3 correlated campaigns'
    sim2()

