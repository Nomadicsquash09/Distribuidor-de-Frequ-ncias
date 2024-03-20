class Freq():
    def __init__(self, _list: list[float], _classes: list[float], _amp: float):
        self._data = _list
        self._classes_amp = _amp
        self._classes_range = _classes
        self._classes = self.classes()
        self._count_list = self.count()
        self._fri = self.fri()
        self._fi = self.fi()
        self._xi = self.xi()
        self._pi = self.pi()

    def classes(self) -> list[tuple]:
        cls_list = []
        for i in range(len(self._classes_range)):
            obj = f'{self._classes_range[i]} |- ' \
                f'{self._classes_range[i] + self._classes_amp}'
            cls_list.append(obj)

        return cls_list

    def count(self) -> list[float]:
        count_list = []
        for i in range(len(self._classes_range)):
            counter = sum(1 for data_point in self._data
                          if self._classes_range[i] <= data_point <
                          self._classes_range[i] + self._classes_amp)
            count_list.append(counter)
        return count_list

    def fri(self) -> list[float]:
        fri_list = []
        for item in self._count_list:
            perc = round(item / len(self._data), 4)
            fri_list.append(perc)
        return fri_list

    def fi(
            self,
            num: float = 0,
            counter: int = 0,
            fi_list: list[float] = None  # type: ignore
            ) -> list[float]:

        if fi_list is None:
            fi_list = []

        if counter < len(self._count_list):
            num += self._count_list[counter]
            fi_list.append(num)
            counter += 1
            return self.fi(num, counter, fi_list)
        else:
            return fi_list

    def xi(self) -> list[float]:
        xi_list = []
        for i in range(len(self._classes)):
            class_lim = self._classes_range[i] + self._classes_amp
            xi_list.append(
                round(
                    (self._classes_range[i] + class_lim) / 2,
                    4
                    )
            )
        return xi_list

    def pi(self):
        pi_list = []
        for item in self._fri:
            pi_list.append(
                round(item * 100, 4)
            )
        return pi_list

    def __repr__(self) -> str:
        repr_string = ""
        for i in range(len(self._classes)):
            string = '{:<3} | {:^16} | {:^5} | {:^8}'\
                ' | {:^5} | {:^8} | {:^8}\n'.format(
                    i + 1,
                    self._classes[i],
                    self._count_list[i],
                    self._fri[i],
                    self._fi[i],
                    self._xi[i],
                    self._pi[i]
                )
            repr_string += string

        return repr_string
