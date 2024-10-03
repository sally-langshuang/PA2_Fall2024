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

        downbody = Sphere(Point((1, 1, 0)), shaderProg, [0.3, 0.3, 0.4], CT.PINK)
        upbody = Sphere(Point((0, 0, -0.4)), shaderProg, [0.3, 0.3, 0.3], CT.PINK)

        tailbody = Sphere(Point((0, 0, 0.88)), shaderProg, [0.55, 0.4,0.6], CT.SOFTRED)

        self.addChild(downbody)
        downbody.addChild(upbody)
        downbody.addChild(tailbody)

        self.componentList = [upbody, downbody, tailbody]
        self.componentDict = {
            "upbody": upbody,
            "downbody": downbody,
            "tailbody": tailbody,
        }
        floor = self.create_obj(downbody, Cube, [0, -0.7, 0.7], shaderProg,[6, 0.001, 6],CT.GRAY, 0, 0, 0,self.componentList, self.componentDict, "floor" )



        left_eye, right_eye = self.create_cp(upbody, upbody, Sphere, (0.24, 0.15, -0.07), shaderProg,
                                             [0.15, 0.15, 0.15], CT.WHITE, 30, -45, 0, self.componentList,
                                             self.componentDict, "eye")



        left_eye_pupil, right_eye_pupil = self.create_cp(left_eye, right_eye, Sphere, (0, 0, -0.04),
                                                         shaderProg, [0.12, 0.12, 0.12], CT.NAVY, 0, 0, 0,
                                                         self.componentList, self.componentDict, "eye_pupil")

        left_mouth, right_mouth = self.create_cp(upbody, upbody, Cone, (0.06, -0.05, -0.09), shaderProg,
                                                 [0.04, 0.04, 0.08], CT.YELLOW,
                                                 0, 200, 0, self.componentList, self.componentDict, "mouth")
        leg1_l = 0.4
        leg2_l = 0.6
        leg3_l = 0.3
        leg_radis = 0.05
        leg_y = 0.12
        left_leg_1_1, righ_leg_1_1 = self.create_cp(upbody, upbody, Cylinder, (0.1, leg_y, 0.678), shaderProg,
                                                    [leg_radis, leg_radis, leg1_l], CT.DODGERBLUE, 55, 155, -0, self.componentList,
                                                    self.componentDict, "leg_1_1")
        left_leg_1_2, right_leg_1_2 = self.create_cp(left_leg_1_1, righ_leg_1_1, Cylinder, (0, 0, leg1_l + leg2_l),
                                                     shaderProg, [leg_radis, leg_radis, leg2_l], CT.DEEPSKYBLUE, 68, -23, 0,
                                                     self.componentList, self.componentDict, "leg_1_2")
        lef_leg_1_3, right_leg_1_3 = self.create_cp(left_leg_1_2, right_leg_1_2, Cone, (0.00, 0, leg2_l+leg3_l), shaderProg,
                                                    [leg_radis, leg_radis, leg3_l], CT.CYAN, 30, 0, 0, self.componentList,
                                                    self.componentDict, "leg_1_3")

        left_leg_2_1, righ_leg_2_1 = self.create_cp(upbody, upbody, Cylinder, (0.1, leg_y, 0.840), shaderProg,
                                                    [leg_radis, leg_radis, leg1_l], CT.DODGERBLUE, 65, 125, -20,
                                                    self.componentList,
                                                    self.componentDict, "leg_2_1")
        left_leg_2_2, right_leg_2_2 = self.create_cp(left_leg_2_1, righ_leg_2_1, Cylinder, (0, 0, leg1_l + leg2_l),
                                                     shaderProg, [leg_radis, leg_radis, leg2_l], CT.DEEPSKYBLUE, 48,
                                                     -23, 0,
                                                     self.componentList, self.componentDict, "leg_2_2")
        lef_leg_2_3, right_leg_2_3 = self.create_cp(left_leg_2_2, right_leg_2_2, Cone, (0.00, 0, leg2_l+leg3_l), shaderProg,
                                                    [leg_radis, leg_radis, leg3_l], CT.CYAN, 30, -10, 0,
                                                    self.componentList,
                                                    self.componentDict, "leg_2_3")

        left_leg_3_1, righ_leg_3_1 = self.create_cp(upbody, upbody, Cylinder, (0.1, leg_y, 0.96), shaderProg,
                                                    [leg_radis, leg_radis, leg1_l], CT.DODGERBLUE, 95, 135, -80,
                                                    self.componentList,
                                                    self.componentDict, "leg_3_1")
        left_leg_3_2, right_leg_3_2 = self.create_cp(left_leg_3_1, righ_leg_3_1, Cylinder, (0, 0, leg1_l + leg2_l),
                                                     shaderProg, [leg_radis, leg_radis, leg2_l], CT.DEEPSKYBLUE, 48,
                                                     -23, 0,
                                                     self.componentList, self.componentDict, "leg_3_2")
        lef_leg_3_3, right_leg_3_3 = self.create_cp(left_leg_3_2, right_leg_3_2, Cone, (0.00, 0, leg2_l+leg3_l), shaderProg,
                                                    [leg_radis, leg_radis, leg3_l], CT.CYAN, 30, -10, 0,
                                                    self.componentList,
                                                    self.componentDict, "leg_3_3")

        left_leg_4_1, righ_leg_4_1 = self.create_cp(upbody, upbody, Cylinder, (0.1, leg_y, 1.08), shaderProg,
                                                    [leg_radis, leg_radis, leg1_l], CT.DODGERBLUE, 115, 155, -110,
                                                    self.componentList,
                                                    self.componentDict, "leg_4_1")
        left_leg_4_2, right_leg_4_2 = self.create_cp(left_leg_4_1, righ_leg_4_1, Cylinder, (0, 0, leg1_l + leg2_l),
                                                     shaderProg, [leg_radis, leg_radis, leg2_l], CT.DEEPSKYBLUE, 78,
                                                     -23, 0,
                                                     self.componentList, self.componentDict, "leg_4_2")
        lef_leg_4_3, right_leg_4_3 = self.create_cp(left_leg_4_2, right_leg_4_2, Cone, (0.00, 0,leg2_l+leg3_l), shaderProg,
                                                    [leg_radis, leg_radis, leg3_l], CT.CYAN, 50, -10, 0,
                                                    self.componentList,
                                                    self.componentDict, "leg_4_3")


    


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
