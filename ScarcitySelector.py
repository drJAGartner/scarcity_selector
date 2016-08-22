class ScarcitySelector:
    def __init__(self, target_m1, target_m2, learning_rate, scarcity_rate):
        self.tm1 = target_m1
        self.tm2 = target_m2
        self.lr = learning_rate
        self.sr = scarcity_rate
        self.pr = 0.5
        self.nm = 0
        self.taken = 0
        self.suc_1 = 0
        self.suc_2 = 0

    def base_opportunity_cost(self, pre_m1, pre_m2):
        return self.pr*(self.tm1/pre_m1) + (1-self.pr)*(self.tm2/pre_m2)

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
        self.taken += 1

    def success(self, num):
        if num == 1:
            self.suc_1 += 1
        if num == 2:
            self.suc_2 += 1

    def balance_p(self):
        mea_m1 = self.suc_1/self.taken
        mea_m2 = self.suc_2/self.suc_1
        self.pr = self.pr + self.lr*((self.tm1/mea_m1)-(self.tm2/mea_m2))