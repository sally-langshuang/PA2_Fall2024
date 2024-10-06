import copy

import ColorType
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
        # floor = self.create_obj(downbody, Cube, [0, -0.7, 0.7], shaderProg,[6, 0.001, 6],CT.GRAY, 0, 0, 0,self.componentList, self.componentDict, "floor" )



        left_eye, right_eye = self.create_cp(upbody, upbody, Sphere, (0.24, 0.15, -0.07), shaderProg,
                                             [0.15, 0.15, 0.15], CT.WHITE, (30, -45, 0), self.componentList,
                                             self.componentDict, "eye")



        left_eye_pupil, right_eye_pupil = self.create_cp(left_eye, right_eye, Sphere, (0, 0, -0.04),
                                                         shaderProg, [0.12, 0.12, 0.12], CT.NAVY, (0, 0, 0),
                                                         self.componentList, self.componentDict, "eye_pupil")

        left_mouth, right_mouth = self.create_cp(upbody, upbody, Cone, (0.06, -0.05, -0.09), shaderProg,
                                                 [0.04, 0.04, 0.08], CT.YELLOW,
                                                 (0, 200, 0), self.componentList, self.componentDict, "mouth")
        leg_radis = 0.05
        joint_radis = 0.05
        leg_x = 0.1
        leg_y = 0.12
        leg_z = 0.078
        leg_z_delta = 0.12

        legs_len = [0.5, 0.6, 0.4]
        uvws = [
            [
                [55, 155, -0],
                [68, -23, 0],
                [30, 0, 0],
            ],
            [
                [65, 125, -20],
                [48, -23, 0],
                [30, -10, 0],
            ],
            [
                [95, 135, -80],
                [48, -23, 0],
                [30, -10, 0],
            ],
            [
                [115, 155, -110],
                [78, -23, 0],
                [50, -10, 0],
            ],
        ]
        leg_colors = [
            ColorType.DEEPSKYBLUE,
            ColorType.SEAGREEN,
            ColorType.CYAN
        ]

        def leg_i(i, left_parent, right_parent, uvws):
            n = len(uvws)
            last_leg_len = 0.3
            for j in range(n):
                uvw = uvws[j]
                if j != n - 1:
                    s = Cylinder
                else:
                    s = Cone

                coords = [0, 0, last_leg_len ]
                if j == 0:
                    coords[0] += leg_x
                    coords[1] += leg_y
                    coords[2] += leg_z + leg_z_delta * i
                # print(f"{i} {j}, {last_leg_len}, joint_pos: {coords}, leg_pos:{(0, 0, legs_len[j])}")

                left_joint_i_j, right_joint_i_j = self.create_cp(left_parent, right_parent, Sphere, coords,
                                                                 shaderProg,
                                                                 [joint_radis, joint_radis, joint_radis], leg_colors[j],
                                                                 uvw, self.componentList,
                                                                 self.componentDict, f"joint_{i}_{j}")
                self.joint_range(left_joint_i_j)
                self.joint_range(right_joint_i_j)

                left_leg_i_j, right_leg_i_j = self.create_cp(left_joint_i_j, right_joint_i_j, s, (0, 0, legs_len[j]), shaderProg,
                                                            [leg_radis, leg_radis, legs_len[j]], leg_colors[j], (0, 0, 0),
                                                            self.componentList,
                                                            self.componentDict, f"leg_{i}_{j}")


                left_parent, right_parent = left_leg_i_j, right_leg_i_j
                last_leg_len = legs_len[j]

        for i in range(len(uvws)):
            leg_i(i, upbody, upbody, uvws[i])



        # left_leg_2_1, righ_leg_2_1 = self.create_cp(upbody, upbody, Cylinder, (0.1, leg_y, 0.840), shaderProg,
        #                                             [leg_radis, leg_radis, leg1_l], CT.DODGERBLUE, 65, 125, -20,
        #                                             self.componentList,
        #                                             self.componentDict, "leg_2_1")
        # left_leg_2_2, right_leg_2_2 = self.create_cp(left_leg_2_1, righ_leg_2_1, Cylinder, (0, 0, leg1_l + leg2_l),
        #                                              shaderProg, [leg_radis, leg_radis, leg2_l], CT.DEEPSKYBLUE, 48,-23, 0,
        #                                              self.componentList, self.componentDict, "leg_2_2")
        # lef_leg_2_3, right_leg_2_3 = self.create_cp(left_leg_2_2, right_leg_2_2, Cone, (0.00, 0, leg2_l+leg3_l), shaderProg,
        #                                             [leg_radis, leg_radis, leg3_l], CT.CYAN, 30, -10, 0,
        #                                             self.componentList,
        #                                             self.componentDict, "leg_2_3")
        #
        # left_leg_3_1, righ_leg_3_1 = self.create_cp(upbody, upbody, Cylinder, (0.1, leg_y, 0.96), shaderProg,
        #                                             [leg_radis, leg_radis, leg1_l], CT.DODGERBLUE, 95, 135, -80,
        #                                             self.componentList,
        #                                             self.componentDict, "leg_3_1")
        # left_leg_3_2, right_leg_3_2 = self.create_cp(left_leg_3_1, righ_leg_3_1, Cylinder, (0, 0, leg1_l + leg2_l),
        #                                              shaderProg, [leg_radis, leg_radis, leg2_l], CT.DEEPSKYBLUE, 48,-23, 0,
        #                                              self.componentList, self.componentDict, "leg_3_2")
        # lef_leg_3_3, right_leg_3_3 = self.create_cp(left_leg_3_2, right_leg_3_2, Cone, (0.00, 0, leg2_l+leg3_l), shaderProg,
        #                                             [leg_radis, leg_radis, leg3_l], CT.CYAN, 30, -10, 0,
        #                                             self.componentList,
        #                                             self.componentDict, "leg_3_3")
        #
        # left_leg_4_1, righ_leg_4_1 = self.create_cp(upbody, upbody, Cylinder, (0.1, leg_y, 1.08), shaderProg,
        #                                             [leg_radis, leg_radis, leg1_l], CT.DODGERBLUE, 115, 155, -110,
        #                                             self.componentList,
        #                                             self.componentDict, "leg_4_1")
        # left_leg_4_2, right_leg_4_2 = self.create_cp(left_leg_4_1, righ_leg_4_1, Cylinder, (0, 0, leg1_l + leg2_l),
        #                                              shaderProg, [leg_radis, leg_radis, leg2_l], CT.DEEPSKYBLUE, 78, -23, 0,
        #                                              self.componentList, self.componentDict, "leg_4_2")
        # lef_leg_4_3, right_leg_4_3 = self.create_cp(left_leg_4_2, right_leg_4_2, Cone, (0.00, 0,leg2_l+leg3_l), shaderProg,
        #                                             [leg_radis, leg_radis, leg3_l], CT.CYAN, 50, -10, 0,
        #                                             self.componentList,
        #                                             self.componentDict, "leg_4_3")

    @staticmethod
    def joint_range(joint):
        size = 60
        joint.uRange = [max(joint.uRange[0], joint.uAngle - size), min(joint.uRange[1], joint.uAngle + size)]
        joint.vRange = [max(joint.vRange[0], joint.vAngle - size), min(joint.vRange[1], joint.vAngle + size)]
        joint.wRange = [max(joint.wRange[0], joint.wAngle - size), min(joint.wRange[1], joint.wAngle + size)]

    def create_cp(self, left_parent, right_parent, shape, coords, shaderProg, size, color, uvw,
                  componentList, componentDict, name):
        u_angle, v_angle, w_angle = uvw
        obj = self.create_obj(left_parent, shape, coords, shaderProg, size, color, uvw,
                              componentList, componentDict, "left_" + name)
        m_obj = self.create_mirror(right_parent, shape, coords, shaderProg, size, color, uvw,
                                   componentList, componentDict, "right_" + name)
        return obj, m_obj


    def create_obj(self, parent, shape, coords, shaderProg, size, color, uvw, componentList,
                   componentDict, name):
        u_angle, v_angle, w_angle = uvw
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

    def create_mirror(self, parent, shape, coords, shaderProg, size, color, uvw, componentList,
                      componentDict, name):
        co = list(coords)
        co[0] = -co[0]
        u_angle, w_angle, v_angle = uvw
        u_angle, w_angle, v_angle = u_angle, -w_angle, -v_angle
        return self.create_obj(parent, shape, co, shaderProg, size, color, (u_angle, w_angle, v_angle), componentList,
                               componentDict, name)
