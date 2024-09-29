import numpy
import wx
from OpenGL.raw.GLU import gluPerspective
from Tools.scripts.gprof2html import trailer
from wx import glcanvas
from OpenGL.GL import *
import OpenGL.GL.shaders as shaders


class OpenGLCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, wx.ID_ANY, size=(1120, 630))
        self.init = False
        self.context = glcanvas.GLContext(self)
        self.SetCurrent(self.context)
        glClearColor(3/255, 106/255, 110/255 ,1.0)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.on_size)

    def OnPaint(self, event):
        self.OnDraw(event)

    def on_size(self, event):
        size = self.GetClientSize()
        glViewport(0, 0, size.width, size.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, size.width / size.height, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        self.Refresh()

    def OnDraw(self,event):
        self.SetCurrent(self.context)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)  # 移动到 z 轴远离观察者

        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)  # 红色
        glVertex3f(-1.0, -1.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)  # 绿色
        glVertex3f(1.0, -1.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)  # 蓝色
        glVertex3f(0.0, 1.0, 0.0)
        glEnd()

        self.SwapBuffers()


class OpenGLCanvas2(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent)
        self.context = glcanvas.GLContext(self)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_click)

        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)
        self.angle = 0  # 立方体的旋转角度

    def on_size(self, event):
        self.SetCurrent(self.context)
        size = self.GetClientSize()
        glViewport(0, 0, size.width, size.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, size.width / size.height, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        self.Refresh()

    def on_mouse_click(self, event):
        # 每次鼠标点击时，沿着 X 轴旋转立方体
        self.angle += 10
        self.Refresh()

    def on_paint(self, event):
        self.SetCurrent(self.context)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)  # 移动到 z 轴远离观察者
        glRotatef(self.angle, 1.0, 0.0, 0.0)  # 沿 X 轴旋转

        # 绘制立方体
        glBegin(GL_QUADS)
        # 前面
        glColor3f(1.0, 0.0, 0.0)  # 红色
        glVertex3f(-1.0, -1.0,  1.0)
        glVertex3f( 1.0, -1.0,  1.0)
        glVertex3f( 1.0,  1.0,  1.0)
        glVertex3f(-1.0,  1.0,  1.0)

        # 后面
        glColor3f(0.0, 1.0, 0.0)  # 绿色
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0,  1.0, -1.0)
        glVertex3f( 1.0,  1.0, -1.0)
        glVertex3f( 1.0, -1.0, -1.0)

        # 上面
        glColor3f(0.0, 0.0, 1.0)  # 蓝色
        glVertex3f(-1.0,  1.0, -1.0)
        glVertex3f(-1.0,  1.0,  1.0)
        glVertex3f( 1.0,  1.0,  1.0)
        glVertex3f( 1.0,  1.0, -1.0)

        # 下面
        glColor3f(1.0, 1.0, 0.0)  # 黄色
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f( 1.0, -1.0, -1.0)
        glVertex3f( 1.0, -1.0,  1.0)
        glVertex3f(-1.0, -1.0,  1.0)

        # 左面
        glColor3f(1.0, 0.0, 1.0)  # 紫色
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0,  1.0)
        glVertex3f(-1.0,  1.0,  1.0)
        glVertex3f(-1.0,  1.0, -1.0)

        # 右面
        glColor3f(0.0, 1.0, 1.0)  # 青色
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(1.0,  1.0, -1.0)
        glVertex3f(1.0,  1.0,  1.0)
        glVertex3f(1.0, -1.0,  1.0)
        glEnd()

        self.SwapBuffers()


class My(glcanvas.GLCanvas):
    fps = 120
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent)
        self.init = False
        self.Bind(wx.EVT_TIMER, self.OnPaint)
        self.context = glcanvas.GLContext(self)
        self.timer = wx.Timer(self, 1)  # TIMER_ID set to 1
        self.timer.Start(int(1000 / self.fps), oneShot=wx.TIMER_CONTINUOUS)

    def OnPaint(self, event=None):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

    def InitGL(self):
        self.SetCurrent(self.context)
        OpenGL.GL.glMatrixMode(OpenGL.GL.GL_MODELVIEW)
        self.size = self.GetClientSize()

    def OnDraw(self):
        pass

class Component:
    def __init__(self):
        pass
class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        self.size = (1280, 720)
        wx.Frame.__init__(self, None, title="my wx frame", size=self.size)
        self.canvas = My(self)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None)
        frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
    pass