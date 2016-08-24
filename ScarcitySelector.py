class ScarcitySelector:
    def __init__(self, target_cr, target_ctr, learning_rate, scarcity_rate):
        self.cr = target_cr
        self.ctr = target_ctr
        self.lr = learning_rate
        self.sr = scarcity_rate
        self.pr = 0.5
        self.nm = 0
        self.taken = 0
        self.suc_1 = 0
        self.suc_2 = 0

    def base_opportunity_cost(self, pre_cr, pre_ctr):
        return self.pr*(self.cr/pre_cr) + (1-self.pr)*(self.ctr/pre_ctr)

    def theta(self, in_v):
        if in_v < 0:
            return 0
        else:
            return 1

    def opp_cost(self, pre_m1, pre_m2):
        base = self.base_opportunity_cost(pre_m1, pre_m2)
        oc = base - self.theta(1-base)*self.nm*self.sr
        if base <= 1:
            self.nm += 1
        return oc

    def choose_opportunity(self):
        self.nm = 0
        if self.taken % 200 == 0:
            self.balance_p()
        self.taken += 1

    def success(self, num):
        if num == 1:
            self.suc_1 += 1
        if num == 2:
            self.suc_2 += 1

    def rates(self):
        if self.taken > 0:
            mea_ctr = float(self.suc_1)/float(self.taken)
        else:
            mea_ctr = 0

        if self.suc_1 > 0:
            mea_cr = float(self.suc_2)/float(self.suc_1)
        else:
            mea_cr = 0
        return (mea_ctr, mea_cr)

    def balance_p(self):
        (mea_ctr, mea_cr) = self.rates()
        if mea_cr != 0 and mea_ctr != 0:
            self.pr = self.pr + self.lr*((self.cr/mea_cr)-(self.ctr/mea_ctr))
        elif mea_ctr == 0:
            self.pr -= 0.01
        else:
            self.pr += 0.01
        if self.pr < 0.01:
            self.pr = 0.01
        if self.pr > .99:
            self.pr = 0.99

    def stats(self):
        print "*** stats ***"
        print "\tTarget CTR:", self.ctr, ", target CR:", self.cr, ", current p:", self.pr
        (mea_ctr, mea_cr) = self.rates()
        if self.taken > 0 and self.suc_1 > 0:
            print "\tImpressions:", self.taken, ", CTR:", mea_ctr, ", CR:", mea_cr
        elif self.taken > 0:
            print "\tImpressions:", self.taken, ", CTR:", mea_ctr, "No clicks, CR cannot be measured"
        else:
            print "\tNo Impressions"