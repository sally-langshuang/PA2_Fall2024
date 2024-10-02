import wx
from OpenGL.GL import *
from wx import glcanvas
import numpy as np
from collada import *

from OpenGL.raw.GLU import gluPerspective
from GLProgram import *
from Shapes import *
from Point import *
import ColorType

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __iter__(self):
        return iter((self.r, self.g, self.b))


BLUEGREEN = Color(3 / 255, 106 / 255, 110 / 255)


class Canvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent)
        self.context = glcanvas.GLContext(self)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_click)
        self.Bind(wx.EVT_RIGHT_DOWN, self.on_right_click)
        self.Bind(wx.EVT_MOTION, self.on_mouse_motion)
        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)
        self.angle_x = 0  # 沿 X 轴旋转的角度
        self.angle_y = 0  # 沿 Y 轴旋转的角度

        self.mouse_position = None

        self.init = False

    def InitGL(self):
        self.SetCurrent(self.context)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(*BLUEGREEN, 1.0)
        gl.glEnable(gl.GL_DEPTH_TEST)

    def on_size(self, event):
        print("on size")
        self.SetCurrent(self.context)
        size = self.GetClientSize()
        glViewport(0, 0, size.width, size.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, size.width / size.height, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        self.init = False
        self.Refresh()

    def on_right_click(self, event):
        # 每次右键点击时，沿着 Y 轴旋转立方体
        print("right click")
        self.angle_y += 10
        self.Refresh()

    def on_mouse_motion(self, event):
        if event.Dragging() and event.LeftIsDown():  # 如果鼠标左键按下并拖动
            current_pos = event.GetPosition()  # 获取当前鼠标位置
            if self.last_mouse_pos is not None:
                # 计算鼠标移动的距离
                dx = current_pos.x - self.last_mouse_pos.x
                dy = current_pos.y - self.last_mouse_pos.y

                # 更新旋转角度，dx 影响 Y 轴旋转，dy 影响 X 轴旋转
                self.angle_y += dx * 0.5  # 乘以 0.5 是为了减慢旋转速度
                self.angle_x += dy * 0.5

            # 更新最后一次鼠标位置
            self.last_mouse_pos = current_pos
            self.Refresh()  # 刷新画布以重新绘制
    def OnMouseLeft(self, event):
        """
        Mouse left click event binding

        :param event: left mouse click event
        :return: None
        """
        x = event.GetX()
        y = event.GetY()
        print(f"Mouse left click x {x} y {y}")
        self.mouse_position[0] = x
        self.mouse_position[1] = y
        self.Refresh(True)

    def on_mouse_click(self, event):
        # 每次鼠标点击时，沿着 X 轴旋转立方体
        self.angle += 10
        self.Refresh()
        print("left click angle = ", self.angle)

    def on_paint(self, event):
        print("on paint")
        if not self.init:
            self.InitGL()
            self.init = True
        self.SetCurrent(self.context)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        gl.glClearDepth(1.0)
        glClearColor(*BLUEGREEN, 1.0)

        self.shaderProg = GLProgram()
        self.shaderProg.compile()
        Cube(Point((0, 0, 0)), self.shaderProg , [0.05, 0.05, 2], ColorType.RED)

        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)  # 移动到 z 轴远离观察者
        glRotatef(self.angle, 1.0, 0.0, 0.0)  # 沿 X 轴旋转
        glRotatef(self.angle_y, 0.0, 1.0, 0.0)

        # 绘制立方体
        glBegin(GL_QUADS)
        # 前面
        glColor3f(1.0, 0.0, 0.0)  # 红色
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)

        # 后面
        glColor3f(0.0, 1.0, 0.0)  # 绿色
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, -1.0, -1.0)

        # 上面
        glColor3f(0.0, 0.0, 1.0)  # 蓝色
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)

        # 下面
        glColor3f(1.0, 1.0, 0.0)  # 黄色
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)

        # 左面
        glColor3f(1.0, 0.0, 1.0)  # 紫色
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)

        # 右面
        glColor3f(0.0, 1.0, 1.0)  # 青色
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glEnd()

        # 绘制坐标轴
        glLineWidth(10.0)  # 设置线条宽度
        glBegin(GL_LINES)


        # X 轴（红色）
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(2.0, 0.0, 0.0)

        # Y 轴（绿色）
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 2.0, 0.0)

        # Z 轴（蓝色）
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 2.0)

        glEnd()

        self.SwapBuffers()

def trans():
    theta = np.pi / 2
    myTransformationx = np.array([
        [1, 0, 0, 0],
        [0, np.cos(theta), -np.sin(theta), 0],
        [0, np.sin(theta), np.cos(theta), 0],
        [0, 0, 0, 1],
    ])

    myTransformationy = np.array([
        [np.cos(theta), 0, np.sin(theta), 0],
        [0, 1, 0, 0],
        [-np.sin(theta), 0, np.cos(theta), 0],
        [0, 0, 0, 1],
    ])

    myTransformationz = np.array([
        [np.cos(theta), -np.sin(theta), 0, 0],
        [np.sin(theta), np.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])

    tx, ty, tz = 0.5, 0, 0.5
    movTrans = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1],
    ])

    sx, sy, sz = 1, 1, 1
    scaleTrans = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1],
    ])

    # myTransformation = movTrans
    myTransformation = np.identity(4)
class Frame(wx.Frame):
    def __init__(self, *args, **kw):
        self.size = (500, 500)
        wx.Frame.__init__(self, None, title="my wx frame", size=self.size)
        self.canvas = Canvas(self)


class App(wx.App):
    def OnInit(self):
        frame = Frame()
        frame.Show(True)
        return True


def get_cube():
    geo = Collada("assets/cube0.dae").geometries[0]
    vs = geo.primitives[0].vertex
    geo.primitives[0].indices
    vertices = np.array([])

    for vert in vs:
        vert = np.concatenate((vert, [0., 0., 0.]), axis=0)  # empty normals
        vert = np.concatenate((vert, [0., 0., 0.]), axis=0)  # color
        vert = np.concatenate((vert, [0., 0.]), axis=0)  # empty UV
        vertices = np.append(vertices, vert)
    return vertices


if __name__ == '__main__':
    x = get_cube()
    print("app started")
    app = App()
    app.MainLoop()
    print("app end")
