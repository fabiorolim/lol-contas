class Price:
    """
    Price
    """

    def __init__(self, total, i, n, entry=0.00):
        self._total = total
        self._entry = entry
        self._pv = total - entry
        self._i = i / 100
        self._n = n
        self._pmt = self._calc_pmt()
        self.pmts = [self._pmt] * n
        self.amortizations = []
        self.interests = []
        self.out_balances = []

    @property
    def pv(self):
        return self._pv

    @property
    def i(self):
        return self._i

    @property
    def n(self):
        return self._n

    @property
    def pmt(self):
        return self._pmt

    @property
    def total(self):
        return self._total

    @property
    def entry(self):
        return self._entry

    def _calc_pmt(self):
        """
        Calcula o valor da prestação fixa
        :return: prestação fixa
        """
        pmt = self.pv / ((((1 + self.i) ** self.n) - 1) /
                         (((1 + self.i) ** self.n) * self.i))

        return round(pmt, 2)

    def _calc_interest(self):
        return round(self.i * self.pv, 2)

    def _calc_out_balance(self, amortization):
        self._pv -= amortization
        self._pv = round(self._pv, 2)
        return self._pv

    def _calc_amortization(self, interest):
        return round(self.pmt - interest, 2)

    def efective_cost_total(self):
        return round(self.pmt * self.n, 2)

    def generate_lists(self):
        p = 1
        while p <= self.n:
            interest = self._calc_interest()
            self.interests.append(interest)
            amortization = self._calc_amortization(interest)
            self.amortizations.append(amortization)
            out_balance = self._calc_out_balance(amortization)
            self.out_balances.append(out_balance)

            p += 1

    def generate_table(self):
        table = tuple(
            zip(range(1, len(self.pmts) + 1), self.pmts, self.amortizations,
                self.interests, self.out_balances))

        return table


class Sac:
    """
    SAC
    """

    def __init__(self, total, i, n, entry=0.00):
        self._total = total
        self._entry = entry
        self._pv = total - entry
        self._i = i / 100
        self._n = n
        self._a = self._calc_amortization(self._pv, n)
        self.amortizations = [self._a] * self._n
        self.out_balances = []
        self.interests = []
        self.pmts = []

    @property
    def pv(self):
        return self._pv

    @property
    def i(self):
        return self._i

    @property
    def n(self):
        return self._n

    @property
    def a(self):
        return self._a

    @property
    def total(self):
        return self._total

    @property
    def entry(self):
        return self._entry

    def _calc_pmt(self, interest):
        """
        Calcula o valor da prestação decrescente
        :return: prestação
        """
        return round(interest + self.a, 2)

    def _calc_interest(self):
        return round(self.i * self.pv, 2)

    def _calc_out_balance(self):
        self._pv = round(self._pv - self.a, 2)
        return self._pv

    @classmethod
    def _calc_amortization(cls, pv, n):
        return round(pv / n, 2)

    def efective_cost_total(self):
        return round(sum(self.pmts), 2)

    def generate_lists(self):
        p = 1
        while p <= self.n:
            interest = self._calc_interest()
            self.interests.append(interest)
            out_balance = self._calc_out_balance()
            self.out_balances.append(out_balance)
            pmt = self._calc_pmt(interest)
            self.pmts.append(pmt)

            p += 1
        self.interests.append(0.0)

    def generate_table(self):
        table = tuple(
            zip(range(1, len(self.pmts) + 1), self.pmts, self.amortizations,
                self.interests, self.out_balances))

        return table
