from PyQt5.QtCore import QObject

'''
游戏核心类
'''


class GameCore(QObject):
    def __init__(self):
        super(GameCore, self).__init__()
        '''
        记录棋盘信息；None无棋子，black黑棋子，white白棋子
        使用列表生成式，创建二维列表
        '''
        self.chessboard = [[None for i in range(19)] for j in range(19)]

    # 初始化棋盘信息
    def init_game(self):
        for i in range(19):
            for j in range(19):
                self.chessboard[i][j] = None

    # 是否可以悔棋（消除棋子记录chessman x,y
    def regret(self, x, y):
        # 判断当前位置是否有棋子
        if self.chessboard[x][y] == None:
            return False
        else:
            self.chessboard[x][y] = None
            return True

    # 判断输赢，判断8个的棋子是否为五子连珠
    def judge_win(self, x, y, color):
        '''
        :param x:水平坐标i
        :param y:垂直坐标j
        :param color:
        :return:

        '''
        count = 1
        # 水平方向判断，y值不变，x值发生变化
        # 左边
        i = x - 1
        while i >= 0:
            if self.chessboard[y][i] == None or self.chessboard[y][i] != color:
                break
            count += 1
            i -= 1
        # 右边
        i = x + 1
        while i <= 18:
            if self.chessboard[y][i] == None or self.chessboard[y][i] != color:
                break
            count += 1
            i += 1
        if count >= 5:
            return color

        # 垂直方向 x不变，y变化
        # 上边

        # 下边