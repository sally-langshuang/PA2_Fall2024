import copy

from Component import Component
from Shapes import Sphere, Cone
from Point import Point
import ColorType as CT


class ModelSpider(Component):
    components = None
    contextParent = None

    # v-- z, w -- y , u -- x
    def __init__(self, parent, position, shaderProg, display_obj=None):
        super().__init__(position, display_obj)
        self.contextParent = parent

        upbody = Sphere(Point((-1, -1, -2)), shaderProg, [0.5, 0.5, 0.5], CT.PINK)
        downbody = Sphere(Point((0, 0, 0.7)), shaderProg, [0.7, 0.7, 0.7], CT.PURPLE)

        self.addChild(upbody)
        upbody.addChild(downbody)

        self.componentList = [upbody, downbody]
        self.componentDict = {
            "upbody": upbody,
            "downbody": downbody,
        }


        # left_eye = Sphere(Point((0.25, 0.25, -0.25)), shaderProg, [0.15, 0.15, 0.15], CT.WHITE)
        # left_eye_center = Sphere(Point((0.025, 0.025, -0.025)), shaderProg, [0.12, 0.12, 0.12], CT.NAVY)
        #
        #
        # right_eye = Sphere(Point((-0.25, 0.25, -0.25)), shaderProg, [0.15, 0.15, 0.15], CT.WHITE)
        # right_eye_center = Sphere(Point(((-0.025, 0.025, -0.025))), shaderProg, [0.12, 0.12, 0.12], CT.NAVY)
        #
        # upbody.addChild(left_eye)
        # left_eye.addChild(left_eye_center)
        #
        # upbody.addChild(right_eye)
        # right_eye.addChild(right_eye_center)

        left_eye, right_eye = self.create_cp(upbody, upbody, Sphere, (0.25, 0.15, -0.25),  shaderProg, [0.15, 0.15, 0.15], CT.WHITE, 0, 0, 0, self.componentList, self.componentDict, "eye")

        left_eye_pupil, right_eye_pupil = self.create_cp(left_eye, right_eye, Sphere,(0.025, 0.025, -0.025),shaderProg, [0.12, 0.12, 0.12], CT.NAVY, 0, 0, 0, self.componentList, self.componentDict, "eye_pupil" )

        left_mouth, right_mouth = self.create_cp(upbody, upbody, Cone, (0.1, -0.05, -0.25), shaderProg, [0.05, 0.05, 0.12], CT.ORANGE,
                                                 0, 0, 200, self.componentList, self.componentDict, "mouth")



        # self.componentList = [upbody, downbody, left_eye, left_eye_center, right_eye, right_eye_center, left_mouth]
        # self.componentDict = {
        #     "upbody": upbody,
        #     "downbody": downbody,
        #     "left_eye": left_eye,
        #     "left_eye_center": left_eye_center,
        #     "right_eye": right_eye,
        #     "right_eye_center": right_eye_center,
        #     "left_mouth": left_mouth,
        # }

    def create_cp(self, left_parent, right_parent, shape, coords, shaderProg, size, color, x_u_angle, y_w_angle, z_v_angle, componentList, componentDict, name):
        obj = self.create_obj(left_parent, shape, coords, shaderProg, size, color, x_u_angle, y_w_angle, z_v_angle, componentList, componentDict, "left_" + name)
        m_obj = self.create_mirror(right_parent, shape, coords, shaderProg, size, color, x_u_angle, y_w_angle, z_v_angle, componentList, componentDict, "right_" + name)
        return obj, m_obj

    def create_obj(self, parent, shape, coords, shaderProg, size, color, x_u_angle, y_w_angle, z_v_angle, componentList, componentDict, name):
        co = copy.deepcopy(coords)
        obj = shape(Point(co), shaderProg, size, color)
        if x_u_angle != 0:
            obj.setDefaultAngle(x_u_angle, obj.uAxis)
        if y_w_angle != 0:
            obj.setDefaultAngle(y_w_angle, obj.wAxis)
        if z_v_angle != 0:
            obj.setDefaultAngle(z_v_angle, obj.vAxis)
        parent.addChild(obj)
        componentList.append(obj)
        componentDict[name] = obj
        return obj

    def create_mirror(self, parent, shape, coords, shaderProg, size, color, x_u_angle, y_w_angle, z_v_angle, componentList, componentDict, name):
        co = list(coords)
        co[0] = -co[0]
        x_u_angle, y_w_angle, z_v_angle = -x_u_angle, -y_w_angle, -z_v_angle
        return self.create_obj(parent, shape, co, shaderProg, size, color, x_u_angle, y_w_angle, z_v_angle, componentList, componentDict, name)

