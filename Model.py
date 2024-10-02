import copy

from Component import Component
from Shapes import *
from Point import Point
import ColorType as CT


class ModelSpider(Component):
    components = None
    contextParent = None

    # v-- z, w -- y , u -- x
    def __init__(self, parent, position, shaderProg, display_obj=None):
        super().__init__(position, display_obj)
        self.contextParent = parent

        upbody = Sphere(Point((1, 1, 0)), shaderProg, [0.5, 0.5, 0.5], CT.PINK)
        downbody = Sphere(Point((0, 0, 0.5)), shaderProg, [0.4, 0.5, 0.4], CT.PINK)
        tailbody = Sphere(Point((0, 0, 1.3)), shaderProg, [1, 0.8, 1.2], CT.SOFTRED)

        self.addChild(upbody)
        upbody.addChild(downbody)
        downbody.addChild(tailbody)

        self.componentList = [upbody, downbody, tailbody]
        self.componentDict = {
            "upbody": upbody,
            "downbody": downbody,
            "tailbody": tailbody,
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

        left_eye, right_eye = self.create_cp(upbody, upbody, Sphere, (0.25, 0.15, -0.25), shaderProg,
                                             [0.15, 0.15, 0.15], CT.WHITE, 0, 0, 0, self.componentList,
                                             self.componentDict, "eye")

        left_eye_pupil, right_eye_pupil = self.create_cp(left_eye, right_eye, Sphere, (0.025, 0.025, -0.025),
                                                         shaderProg, [0.12, 0.12, 0.12], CT.NAVY, 0, 0, 0,
                                                         self.componentList, self.componentDict, "eye_pupil")

        left_mouth, right_mouth = self.create_cp(upbody, upbody, Cone, (0.1, -0.05, -0.25), shaderProg,
                                                 [0.05, 0.05, 0.11], CT.YELLOW,
                                                 0, 200, 0, self.componentList, self.componentDict, "mouth")

        left_leg_1_1, righ_leg_1_1 = self.create_cp(upbody, upbody, Cylinder, (0.4, 0.5, 0.3), shaderProg,
                                                [0.05, 0.05, 0.2], CT.DODGERBLUE, 45, -45, -0, self.componentList,
                                                self.componentDict, "leg1_1")
        left_leg_1_2, right_leg_1_2 = self.create_cp(left_leg_1_1, righ_leg_1_1, Cylinder, (0.02, -1.0, -0.14), shaderProg, [0.05, 0.05, 0.60], CT.DEEPSKYBLUE, -60, 0, 20, self.componentList, self.componentDict, "leg1_2")
        lef_leg_1_3, right_leg_1_3 = self.create_cp(left_leg_1_2, right_leg_1_2, Cone, (0.00, 0, -0.33), shaderProg,
                                                [0.05, 0.05, 0.25], CT.CYAN, -20, 200, 0, self.componentList,
                                                self.componentDict, "leg1_3")

        left_leg_2_1, righ_leg_2_1 = self.create_cp(upbody, upbody, Cylinder, (0.65, 0.55, 0.55), shaderProg,
                                                [0.05, 0.05, 0.30], CT.DODGERBLUE, 35, -55, -0, self.componentList,
                                                self.componentDict, "leg2_1")
        left_leg_2_2, right_leg_2_2 = self.create_cp(left_leg_2_1, righ_leg_2_1, Cylinder, (-0.03, 0.05, 0.40), shaderProg,
                                                 [0.05, 0.05, 0.57], CT.DEEPSKYBLUE,-210, 30, 0, self.componentList,
                                                 self.componentDict, "leg2_2")

        lef_leg_2_3, right_leg_2_3 = self.create_cp(left_leg_2_2, right_leg_2_2, Cone, (0, 0,0.8), shaderProg,
                                                    [0.05, 0.05, 0.25], CT.CYAN, -20, 20, 0, self.componentList,
                                                    self.componentDict, "leg2_3")

        left_leg_3_1, righ_leg_3_1 = self.create_cp(upbody, upbody, Cylinder, (0.75, 0.35, 0.85), shaderProg,
                                                    [0.05, 0.05, 0.30], CT.DODGERBLUE, 15, -75, -0, self.componentList,
                                                    self.componentDict, "leg2_1")
        left_leg_3_2, right_leg_3_2 = self.create_cp(left_leg_3_1, righ_leg_3_1, Cylinder, (-0.03, 0.05, 0.40),
                                                     shaderProg,
                                                     [0.05, 0.05, 0.57], CT.DEEPSKYBLUE, -210, 30, 0,
                                                     self.componentList,
                                                     self.componentDict, "leg2_2")

        lef_leg_3_3, right_leg_3_3 = self.create_cp(left_leg_3_2, right_leg_3_2, Cone, (0, 0, 0.8), shaderProg,
                                                    [0.05, 0.05, 0.25], CT.CYAN, -20, 20, 0, self.componentList,
                                                    self.componentDict, "leg2_3")

        #
        # test = Cylinder(Point((0, 0, 0)), shaderProg, [0.5, 0.5, 0.9], CT.BLUE)
        # test.setDefaultAngle(0, test.wAxis)
        # self.componentList.append(test)
        # self.componentDict["test"] = test
        # self.addChild(test)


    def create_cp(self, left_parent, right_parent, shape, coords, shaderProg, size, color, u_angle, v_angle, w_angle,
                  componentList, componentDict, name):
        obj = self.create_obj(left_parent, shape, coords, shaderProg, size, color, u_angle, v_angle, w_angle,
                              componentList, componentDict, "left_" + name)
        m_obj = self.create_mirror(right_parent, shape, coords, shaderProg, size, color, u_angle, v_angle, w_angle,
                                   componentList, componentDict, "right_" + name)
        return obj, m_obj

    def create_obj(self, parent, shape, coords, shaderProg, size, color, u_angle, v_angle, w_angle, componentList,
                   componentDict, name):
        co = copy.deepcopy(coords)
        obj = shape(Point(co), shaderProg, size, color)
        if u_angle != 0:
            obj.setDefaultAngle(u_angle, obj.uAxis)
        if v_angle != 0:
            obj.setDefaultAngle(v_angle, obj.vAxis)
        if w_angle != 0:
            obj.setDefaultAngle(w_angle, obj.wAxis)
        parent.addChild(obj)
        componentList.append(obj)
        componentDict[name] = obj
        return obj

    def create_mirror(self, parent, shape, coords, shaderProg, size, color, u_angle, w_angle, v_angle, componentList,
                      componentDict, name):
        co = list(coords)
        co[0] = -co[0]
        u_angle, w_angle, v_angle = u_angle, -w_angle, -v_angle
        return self.create_obj(parent, shape, co, shaderProg, size, color, u_angle, w_angle, v_angle, componentList,
                               componentDict, name)
