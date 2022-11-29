class  Matrix():
    '''
    这里是矩阵类，看我从0开始硬搓矩阵
    虽然我不喜欢写注释，文档但是这次我不得不写
    '''
    def __init__(self, line:int, row:int, data:list) :
        '''这里是矩阵的基本设置'''
        self.data = data  # 这里储存矩阵的数据，列表
        self.line = line  # 矩阵的行，int
        self.row = row  # 矩阵的列，int

    '''以下是有关矩阵的输出'''

    def get_index(self, line_get:int, row_get:int, isPrint = False):
        '''
        根据矩阵下标获得对应数字
        :param line_get: 行
        :param row_get: 列
        :param isPrint: True 为打印该数字 默认为False
        :return: 返回下标对应数字
        '''
        if line_get > self.line or row_get > self.row:
            print('下标超出范围！')
            return False
        data_get = self.data[(line_get - 1) * self.row + row_get - 1]
        if isPrint:
            print(data_get)
        return data_get


    def get_number(self, number:int, isPrint = False):
        '''
        根据编号获得数字
        :param number: 编号
        :param isPrint: True 为打印该数字 默认为False
        :return: 返回下标对应数字
        '''
        if number > self.line * self.row:
            print('编号超出范围！')
            return False
        data_get = self.data[number - 1]
        if isPrint:
            print(data_get)
        return data_get

    def print_matrix(self):
        '''
        按照矩阵格式打印矩阵
        '''
        for i in range(self.line):
            for j in range(self.row):
                print(self.data[i  * self.row + j],end = '  ')
            print('\n')

    '''以下是矩阵有关运算'''

    def sum(self, a_matrix, b_matrix, isPrint = False):
        '''
        矩阵加法运算 c = a + b
        :param a_matrix: 矩阵a
        :param b_matrix: 矩阵b
        :param isPrint: True 为打印该矩阵 默认为False
        :return: 矩阵c
        '''
        if a_matrix.line != b_matrix.line or a_matrix.row != b_matrix.row:
            print('相加的两个矩阵不是同形矩阵，无法运算！')
            return False
        c_matrix_line, c_matrix_row = a_matrix.line, a_matrix.row
        all_number = c_matrix_line * c_matrix_row
        # 列表推导式，求矩阵加法
        c_matrix_data = [a_matrix.data[number] + b_matrix.data[number] for number in range(all_number)]
        c_matrix = Matrix(c_matrix_line, c_matrix_row, c_matrix_data)  # 生成矩阵c
        if isPrint:
            c_matrix.print_matrix()
        return c_matrix

    def sub(self, a_matrix, b_matrix, isPrint = False):
        '''
        矩阵减法运算 c = a - b
        :param a_matrix: 矩阵a
        :param b_matrix: 矩阵b
        :param isPrint: True 为打印该矩阵 默认为False
        :return: 矩阵c
        '''
        if a_matrix.line != b_matrix.line or a_matrix.row != b_matrix.row:
            print('相减的两个矩阵不是同形矩阵，无法运算！')
            return False
        c_matrix_line, c_matrix_row = a_matrix.line, a_matrix.row
        all_number = c_matrix_line * c_matrix_row
        # 列表推导式，求矩阵减法
        c_matrix_data = [a_matrix.data[number] - b_matrix.data[number] for number in range(all_number)]
        c_matrix = Matrix(c_matrix_line, c_matrix_row, c_matrix_data)  # 生成矩阵c
        if isPrint:
            c_matrix.print_matrix()
        return c_matrix

    def number_multiply(self, digital:int, isPrint = False):
        '''
        矩阵的数乘 c = digital * self
        :param digital: 所乘的数字
        :param a_matrix: 矩阵a
        :param isPrint: True 为打印该矩阵 默认为False
        :return: 返回矩阵c
        '''
        c_matrix_line, c_matrix_row = self.line, self.row
        all_number = c_matrix_line * c_matrix_row
        # 列表推导式，求矩阵数乘
        c_matrix_data = [self.data[number] * digital for number in range(all_number)]
        self.data = c_matrix_data
        c_matrix = Matrix(c_matrix_line, c_matrix_row, c_matrix_data)  # 生成矩阵c
        if isPrint:
            c_matrix.print_matrix()
        return c_matrix

    def multiply(self, a_matrix, b_matrix,isPrint = False):
        '''
        矩阵的乘法
        :param a_matrix: 矩阵a
        :param b_matrix: 矩阵b
        :param isPrint: True 为打印该矩阵 默认为False
        :return: 矩阵c
        '''
        if a_matrix.row != b_matrix.line:
            print('相乘的两个矩阵行列不匹配，无法运算！')
            return False
        c_matrix_line, c_matrix_row = a_matrix.line, b_matrix.row
        all_number = c_matrix_line * c_matrix_row
        c_matrix_data = [0 for i in range(all_number)] # 初始化c
        ans = 0  # 初始化和
        for i in range(a_matrix.line):# 行
            for j in range(b_matrix.row):# 列
                for k in range(a_matrix.row):
                    ans = ans + a_matrix.data[i * a_matrix.row + k] * b_matrix.data[k * b_matrix.row + j]
                c_matrix_data[i * c_matrix_row + j] = ans
                ans = 0  # 重置为0
        c_matrix = Matrix(c_matrix_line, c_matrix_row, c_matrix_data)  # 生成矩阵c
        if isPrint:
            c_matrix.print_matrix()
        return c_matrix

    def transpose(self, isPrint = False):
        '''
        矩阵的转置
        :param isPrint: True 为打印该矩阵 默认为False
        '''
        data = tuple(self.data) # 注意 这里要是不用元组，则是浅拷贝，下面程序执行时会导致data数值发生变化
        # 转置
        for i in range(self.line):
            for j in range(self.row):
               self.data[j * self.line + i] = data[i * self.row + j]
        self.line, self.row = self.row, self.line
        if isPrint:
            self.print_matrix()