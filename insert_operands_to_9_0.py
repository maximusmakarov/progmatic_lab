class Solution:
    _numbers_operands = 9  # количество промежутков
    _mark = [''] * _numbers_operands
    _operators = {
        0: '',
        1: '-',
        2: '+',
    }
    base = len(_operators)  # количество операторов
    _quantity = base ** _numbers_operands  # 3 ** 9
    __slots__ = ['_trinity']

    def _trinity_operands(self, num):
        self._trinity = ''
        while num > 0:
            self._trinity = str(num % self.base) + self._trinity
            num //= self.base
        self._trinity = tuple(self._trinity)

    def _get_expression(self, iter_n):
        evaluation_expression = ''
        self._trinity_operands(iter_n)
        for digit in range(1, 10):
            operation = digit - 1
            digit *= (-1)
            if operation < len(self._trinity):
                match int(self._trinity[digit]):
                    case 0:
                        self._mark[digit] = self._operators[0]
                    case 1:
                        self._mark[digit] = self._operators[1]
                    case 2:
                        self._mark[digit] = self._operators[2]
            else:
                self._mark[digit] = ''

        for i in range(9):
            evaluation_expression += f'{9 - i}{self._mark[i]}'
        evaluation_expression += '0'

        return evaluation_expression

    def __call__(self, expected_result):
        results = {
            self._get_expression(i) for i in range(self._quantity) if eval(self._get_expression(i)) == expected_result
        }

        if results:
            return f'Результат {expected_result} дают выражения {results}'
        else:
            return f'К сожалению не существует выражения, результатом которого являлось бы число {expected_result}.'


if __name__ == '__main__':
    sol = Solution()
    print(sol(200))
