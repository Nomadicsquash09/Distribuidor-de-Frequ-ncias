# main.py
from math import log10, ceil, floor
from freq_dist import Freq


class Data():
    def __init__(self, *args: float) -> None:
        self._raw_data = sorted(list(args))
        self._data_length = len(self._raw_data)
        self._class_number = self.cls_num(self._data_length)
        self._classes_amp = self.range(
            self._class_number,
            self._raw_data[0],
            self._raw_data[-1]
        )
        self._classes_range = self.classes(self._raw_data, self._classes_amp)
        self._freq_dist = self.frequency_distribution()
        self._tab_data = self._freq_dist.get_tab()

    def cls_num(self, n: int) -> int:
        num = 1 + (3.3 * log10(n))
        num = ceil(num)
        return num

    def classes(self, _list: list[float], _range: float) -> list[float]:
        values = []
        i = _list[0]
        while i <= _list[-1]:
            values.append(i)
            i += _range
        return values

    def range(self, n: int, _min: float, _max: float) -> float:
        ai = (_max - _min) / n
        ai = floor(ai)
        return ai

    def frequency_distribution(self) -> Freq:
        distribution = Freq(
            self._raw_data,
            self._classes_range,
            self._classes_amp
        )
        return distribution

    @property
    def freq_dist(self) -> Freq:
        return self._freq_dist

    @property
    def tabulated_data(self) -> list[str]:
        return self._tab_data


if __name__ == '__main__':
    d1 = Data(
        39, 39, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 40,
        30, 30, 30, 31, 32, 32, 32, 32, 33, 33, 34, 34, 35,
        4, 11, 12, 15, 15, 16, 20, 21, 22, 22, 23, 24, 24,
        35, 35, 36, 36, 37, 37, 37, 37, 37, 37, 27, 38, 38,
        25, 26, 26, 26, 26, 27, 27, 28, 28, 29, 29, 29, 30
    )
    print(d1.freq_dist)
