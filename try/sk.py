import wx

from CanvasBase import CanvasBase
class MySketch(wx.Panel):
    def __init__(self, parent):
        super(MySketch, self).__init__(parent)

        # 初始化绘图相关的变量
        self.pen_color = wx.Colour(0, 0, 0)  # 默认的笔颜色为黑色
        self.pen_width = 5  # 笔的粗细

        # 创建一个空的点列表来保存用户绘图的轨迹
        self.lines = []
        self.current_line = []

        # 绑定鼠标事件
        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)  # 鼠标按下
        self.Bind(wx.EVT_MOTION, self.on_mouse_move)  # 鼠标移动
        self.Bind(wx.EVT_LEFT_UP, self.on_left_up)  # 鼠标释放
        self.Bind(wx.EVT_PAINT, self.on_paint)  # 绘制事件

    def on_left_down(self, event):
        """当用户按下鼠标左键时，开始记录当前绘图线条"""
        self.current_line = [(event.GetPosition(), self.pen_color, self.pen_width)]
        self.CaptureMouse()  # 捕捉鼠标事件

    def on_mouse_move(self, event):
        """当用户拖动鼠标时，记录轨迹并绘制"""
        if event.Dragging() and event.LeftIsDown():
            pos = event.GetPosition()
            self.current_line.append((pos, self.pen_color, self.pen_width))
            self.Refresh()  # 刷新界面，触发重绘

    def on_left_up(self, event):
        """当用户释放鼠标左键时，保存绘制的线条"""
        if self.HasCapture():
            self.lines.append(self.current_line)
            self.current_line = []
            self.ReleaseMouse()

    def on_paint(self, event):
        """当需要重绘时，绘制所有已保存的线条"""
        dc = wx.PaintDC(self)  # 创建绘制上下文
        dc.Clear()  # 清除面板

        # 绘制保存的所有线条
        for line in self.lines:
            self.draw_line(dc, line)

        # 绘制当前正在绘制的线条
        if self.current_line:
            self.draw_line(dc, self.current_line)

    def draw_line(self, dc, line):
        """绘制一条线"""
        for i in range(len(line) - 1):
            pos1, color1, width1 = line[i]
            pos2, color2, width2 = line[i + 1]

            pen = wx.Pen(color1, width1)
            dc.SetPen(pen)
            dc.DrawLine(pos1, pos2)

if __name__ == "__main__":
    app = wx.App(False)
    frame = wx.Frame(None, size=(500, 500), title="Test",
                     style=wx.DEFAULT_FRAME_STYLE | wx.FULL_REPAINT_ON_RESIZE)  # Disable Resize: ^ wx.RESIZE_BORDER
    canvas = MySketch(frame)

    frame.Show()
    app.MainLoop()
    print("abc")