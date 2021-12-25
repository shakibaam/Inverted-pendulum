# -*- coding: utf-8 -*-

# python imports
from math import degrees

# pyfuzzy imports
from fuzzy.storage.fcl.Reader import Reader
import numpy as np



class FuzzyController:

    def __init__(self, fcl_path):
        self.system = Reader().load_from_file(fcl_path)

    def cp_fuzzification(self, cp):

        # left_far
        left_far_membership = 0
        if cp == -10:
            left_far_membership = 1
        elif cp >= -10 and cp <= -5:
            left_far_membership = -0.2 * cp - 1
        elif cp<-10 :
            left_far_membership = -1


        # left_near
        left_near_membership = 0
        if cp >= -10 and cp <= -2.5:
            left_near_membership = 0.13333333333333333 * cp + 1.3333333333333333
        elif cp >= -2.5 and cp <= 0:
            left_near_membership = -0.4 * cp


        # stop
        stop_membership = 0
        if cp >= -2.5 and cp <= 0:
            stop_membership = 0.4 * cp + 1
        elif cp >= 0 and cp <= 2.5:
            stop_membership = -0.4 * cp + 1


        # right_near
        right_near_membership = 0
        if cp >= 0 and cp <= 2.5:
            right_near_membership = 0.4 * cp
        elif cp >= 2.5 and cp <= 10:
            right_near_membership = -0.13333333333333333 * cp + 1.3333333333333333


        # right_far
        right_far_membership = 0
        if cp >= 5 and cp <= 10:
            right_far_membership = 0.2 * cp - 1
        elif cp == 10:
            right_far_membership = 1
        elif cp>10 :
            right_far_membership = 1

        return left_far_membership, left_near_membership, stop_membership, right_near_membership, right_far_membership

    def cv_fuzzification(self, cv):
        # left_fast
        lef_fast_membership = 0
        if cv == -5:
            lef_fast_membership = 1
        elif cv >= -5 and cv <= -2.5:
            lef_fast_membership = -0.4 * cv - 1
        elif cv<-5 :
            lef_fast_membership = 1
        # elif cv < -5 or cv > -2.5:
        #     lef_fast_membership = 0

        # left_slow
        lef_slow_membership = 0
        if cv >= -5 and cv <= -1:
            lef_slow_membership = 0.25 * cv + 1.25
        elif cv >= -1 and cv <= 0:
            lef_slow_membership = -cv
        # elif cv < -5 or cv > 0:
        #     lef_slow_membership = 0

        # stop
        stop_membership = 0
        if cv >= -1 and cv <= 0:
            stop_membership = cv + 1
        elif cv >= 0 and cv <= 1:
            stop_membership = -cv + 1
        # elif cv < -1 or cv > 1:
        #     stop_membership = 0

        # right_slow
        right_slow_membership = 0
        if cv >= 0 and cv <= 1:
            right_slow_membership = cv
        elif cv >= 1 and cv <= 5:
            right_slow_membership = -0.25 * cv + 1.25
        # elif cv < 0 or cv > 5:
        #     right_slow_membership = 0

        # right_fast
        right_fast_membership = 0
        if cv >= 2.5 and cv <= 5:
            right_fast_membership = 0.4 * cv - 1
        elif cv == 5:
            right_fast_membership = 1
        elif cv>5 :
            right_fast_membership = 1
        # elif cv < 2.5 or cv > 5:
        #     right_fast_membership = 0
        return lef_fast_membership, lef_slow_membership, stop_membership, right_slow_membership, right_fast_membership

    def pa_fuzzification(self, pa):
        # up_more_right
        up_more_right = 0
        if pa >= 0 and pa <= 30:
            up_more_right = 0.03333333333333333 * pa
        elif pa >= 30 and pa <= 60:
            up_more_right = -0.03333333333333333 * pa + 2
        # elif pa<0 :
        #     up_more_right = 1
        # elif pa < 0 or pa > 60:
        #     up_more_right = 0

        # up_right
        up_right = 0
        if pa >= 30 and pa <= 60:
            up_right = 0.03333333333333333 * pa - 1
        elif pa >= 60 and pa <= 90:
            up_right = -0.03333333333333333 * pa + 3
        # elif pa >= 90 or pa <= 30:
        #     up_right = 0

        # up
        up = 0
        if pa >= 60 and pa <= 90:
            up = 0.03333333333333333 * pa - 2
        elif pa >= 90 and pa <= 120:
            up = -0.03333333333333333 * pa + 4
        # elif pa < 60 or pa > 120:
        #     up = 0

        # up_left
        up_left = 0
        if pa >= 90 and pa <= 120:
            up_left = 0.03333333333333333 * pa - 3
        elif pa >= 120 and pa <= 150:
            up_left = -0.03333333333333333 * pa + 5
        # elif pa < 90 or pa > 150:
        #     up_left = 0

        # up_more_left
        up_more_left = 0
        if pa >= 120 and pa <= 150:
            up_more_left = 0.03333333333333333 * pa - 4
        elif pa >= 150 and pa <= 180:
            up_more_left = -0.03333333333333333 * pa + 6
        # elif pa > 180 or pa < 120:
        #     up_more_left = 0

        # down_more_left
        down_more_left = 0
        if pa >= 180 and pa <= 210:
            down_more_left = 0.03333333333333333 * pa - 6
        elif pa >= 210 and pa <= 240:
            down_more_left = -0.03333333333333333 * pa + 8
        # elif pa < 180 or pa > 240:
        #     down_more_left = 0

        # down_left
        down_left = 0
        if pa >= 210 and pa <= 240:
            down_left = 0.03333333333333333 * pa - 7
        elif pa >= 240 and pa <= 270:
            down_left = -0.03333333333333333 * pa + 9
        # elif pa < 210 or pa > 270:
        #     down_left = 0

        # down
        down = 0
        if pa >= 240 and pa <= 270:
            down = 0.03333333333333333 * pa - 8
        elif pa >= 270 and pa <= 300:
            down = -0.03333333333333333 * pa + 10
        # elif pa < 240 or pa > 300:
        #     down = 0

        # down_right
        down_right = 0
        if pa >= 270 and pa <= 300:
            down_right = 0.03333333333333333 * pa - 9
        elif pa >= 300 and pa <= 330:
            down_right = -0.03333333333333333 * pa + 11
        # elif pa < 270 and pa > 330:
        #     down_right = 0

        # down_more_right
        down_more_right = 0
        if pa >= 300 and pa <= 330:
            down_more_right = 0.03333333333333333 * pa - 10
        elif pa >= 330 and pa <= 360:
            down_more_right = -0.03333333333333333 * pa + 12
        elif pa>360 :
            down_more_right = 1
        # elif pa < 300 or pa > 360:
        #     down_more_right = 0

        return up_more_right, up_right, up, up_left, up_more_left, down_more_left, down_left, down, down_right, down_more_right

    def pv_fuzzification(self, pv):
        # cw_fast
        cw_fast = 0
        if pv == -200:
            cw_fast = 1
        elif pv >= -200 and pv <= -100:
            cw_fast = -0.01 * pv - 1
        elif pv<-200 :
            cw_fast = 1
        # elif pv < -200 or pv > -100:
        #     cw_fast = 0

        # cw_slow
        cw_slow = 0
        if pv >= -200 and pv <= -100:
            cw_slow = 0.01 * pv + 2
        elif pv >= -100 and pv <= 0:
            cw_slow = -0.01 * pv
        # elif pv < -200 or pv > 0:
        #     cw_slow = 0

        # stop
        stop = 0
        if pv >= -100 and pv <= 0:
            stop = 0.01 * pv + 1
        elif pv >= 0 and pv <= 100:
            stop = -0.01 * pv + 1
        # elif pv < -100 or pv > 100:
        #     stop = 0

        # ccw_slow
        ccw_slow = 0
        if pv >= 0 and pv <= 100:
            ccw_slow = 0.01 * pv
        elif pv >= 100 and pv <= 200:
            ccw_slow = -0.01 * pv + 2
        # elif pv < 0 or pv > 200:
        #     ccw_slow = 0

        # ccw_fast
        ccw_fast = 0
        if pv >= 100 and pv <= 200:
            ccw_fast = 0.01 * pv - 1
        elif pv == 200:
            ccw_fast = 1
        elif pv>200 :
            ccw_fast = 1
        # elif pv < 100 or pv > 200:
        #     ccw_fast = 0

        return cw_fast, cw_slow, stop, ccw_slow, ccw_fast

    def force_fuzzification(self, force):
        # left_fast
        left_fast = 0
        if force >= -100 and force <= -80:
            left_fast = 0.05 * force + 1
        elif force >= -80 and force <= -60:
            left_fast = -0.05 * force - 3
        elif force<-100 :
            left_fast = 1
        # elif force < -100 or force > -60:
        #     left_fast = 0

        # left_slow
        left_slow = 0
        if force >= -80 and force <= -60:
            left_slow = 0.05 * force + 4
        elif force >= -60 and force <= 0:
            left_slow = -0.016666666666666666 * force
        # elif force < -80 or force > 0:
        #     left_slow = 0

        # stop
        stop = 0
        if force >= -60 and force <= 0:
            stop = 0.016666666666666666 * force + 1
        elif force >= 0 and force <= 60:
            stop = -0.016666666666666666 * force + 1
        # elif force < -60 or force < 60:
        #     stop = 0

        # right_slow
        right_slow = 0
        if force >= 0 and force <= 60:
            right_slow = 0.016666666666666666 * force
        elif force >= 60 and force <= 80:
            right_slow = -0.05 * force + 4
        # elif force < 0 or force > 80:
        #     right_slow = 0

        # right_fast
        right_fast = 0
        if force >= 60 and force <= 80:
            right_fast = 0.05 * force - 3
        elif force >= 80 and force <= 100:
            right_fast = -0.05 * force + 5
        elif force>100 :
            right_fast = 1
        # elif force < 60 or force > 100:
        #     right_fast = 0

        return left_fast, left_slow, stop, right_slow, right_fast

    def left_fast_inference(self, pa, pv):
        cw_fast, cw_slow, cw_stop, ccw_slow, ccw_fast = pv
        up_more_right, up_right, up, up_left, up_more_left, down_more_left, dow_left, down, down_right, down_more_right = pa

        Rule3 = min(up_more_left, cw_slow)
        Rule4 = min(up_more_left, ccw_slow)
        Rule8 = min(up_more_left, ccw_fast)
        Rule11 = min(down_more_left, cw_slow)
        Rule19 = min(dow_left, cw_slow)
        Rule20 = min(dow_left, ccw_slow)
        Rule29 = min(up_left, ccw_slow)
        Rule30 = min(up_left, cw_stop)
        Rule31 = min(up_right, ccw_fast)
        Rule34 = min(up_left, ccw_fast)
        Rule39 = min(up, ccw_fast)

        left_fast_memebrship = max(Rule3, Rule4, Rule8, Rule11, Rule19, Rule20, Rule29, Rule30, Rule31, Rule34, Rule39)
        return left_fast_memebrship

    def left_slow_inference(self, pa, pv):
        cw_fast, cw_slow, cw_stop, ccw_slow, ccw_fast = pv
        up_more_right, up_right, up, up_left, up_more_left, down_more_left, down_left, down, down_right, down_more_right = pa
        Rule5 = min(up_more_right , ccw_fast)
        Rule24 = min(down_left , ccw_fast)
        Rule28 = min(up_left , cw_slow)
        Rule38 = min(up , ccw_slow)

        left_slow_membership = max(Rule5 , Rule24 , Rule28 , Rule38)
        return left_slow_membership

    def stop_inference(self , pa , pv):
        cw_fast, cw_slow, cw_stop, ccw_slow, ccw_fast = pv
        up_more_right, up_right, up, up_left, up_more_left, down_more_left, dow_left, down, down_right, down_more_right = pa
        Rule0 = max(min(up , cw_stop) , min(up_right , ccw_slow) , min(up_left , cw_slow))
        Rule10 = min(down_more_right , cw_slow)
        Rule12 = min(down_more_left , ccw_slow)
        Rule13 = min(down_more_right , ccw_fast)
        Rule14 = min(down_more_right , cw_fast)
        Rule15 = min(down_more_left , cw_fast)
        Rule16 = min(down_more_left , ccw_fast)
        Rule21 = min(down_right , ccw_fast)
        Rule23 = min(dow_left , cw_fast)
        Rule36 = min(down , cw_fast)
        Rule37 = min(down , ccw_fast)
        Rule42 = min(up , cw_stop)

        stop_membership = max(Rule0 , Rule10 , Rule12 ,Rule13 , Rule14 , Rule15 , Rule16 , Rule21 , Rule23 , Rule36 , Rule37 , Rule42)
        return stop_membership

    def right_slow_inference(self , pa ,pv):
        cw_fast, cw_slow, cw_stop, ccw_slow, ccw_fast = pv
        up_more_right, up_right, up, up_left, up_more_left, down_more_left, dow_left, down, down_right, down_more_right = pa
        Rule7 = min(up_more_left , cw_fast)
        Rule22 = min(down_right , cw_fast)
        Rule25 = min(up_right , ccw_slow)
        Rule40 = min(up , cw_slow)

        right_slow_memebership = max(Rule7 , Rule22 , Rule25 , Rule40)
        return right_slow_memebership

    def right_fast_inference(self , pa ,pv):
        cw_fast, cw_slow, cw_stop, ccw_slow, ccw_fast = pv
        up_more_right, up_right, up, up_left, up_more_left, down_more_left, dow_left, down, down_right, down_more_right = pa

        Rule1 = min(up_more_right , ccw_slow)
        Rule2 = min(up_more_right , cw_slow)
        Rule6 = min(up_more_right , cw_fast)
        Rule9 = min(down_more_right , ccw_slow)
        Rule17 = min(down_right , ccw_slow)
        Rule18 = min(down_right , cw_slow)
        Rule26 = min(up_right , cw_slow)
        Rule27 = min(up_right , cw_stop)
        Rule32 = min(up_right , cw_fast)
        Rule33 = min(up_left , cw_fast)
        Rule35 = min(down , cw_stop)
        Rule41 = min(up , cw_fast)

        right_fast_membership = max(Rule1 , Rule2 , Rule6 , Rule9 , Rule17 , Rule18 , Rule26 , Rule27 , Rule32, Rule33 , Rule35 , Rule41)
        return right_fast_membership


    def defuzzification(self , stop_power , left_fast_power ,left_slow_power , right_fast_power , right_slow_power):
        points = np.linspace(-100 , 100 , 5000)
        points_answers = []
        for p in points :
            left_fast, left_slow, stop, right_slow, right_fast = self.force_fuzzification(p)

            if left_fast>left_fast_power :
                left_fast = left_fast_power
            if left_slow>left_slow_power :
                left_slow = left_slow_power
            if  stop>stop_power :
                stop = stop_power
            if right_slow>right_slow_power :
                right_slow = right_slow_power
            if right_fast > right_fast_power :
                right_fast = right_fast_power
            answer = max(left_fast, left_slow, stop, right_slow, right_fast)
            points_answers.append(answer)

        dx = points[1] - points[0]

        sum1 = 0
        sum2 = 0
        # print (points)
        # print (points_answers)
        for i in range(len(points)) :
            sum1 += (points_answers[i] * points[i] * dx)
            sum2 += (points_answers[i] * dx)
        if (sum2 == 0) : return 0
        force = sum1/sum2
        return force









    def _make_input(self, world):
        return dict(
            cp=world.x,
            cv=world.v,
            pa=degrees(world.theta),
            pv=degrees(world.omega)
        )

    def _make_output(self):
        return dict(
            force=0.
        )

    def decide(self, world):
        inputs = self._make_input(world)
        print (inputs)

        cp = inputs["cp"]
        cv = inputs["cv"]
        pa = inputs["pa"]
        pv = inputs["pv"]

        pa_fuzzy = self.pa_fuzzification(pa)
        pv_fuzzy = self.pv_fuzzification(pv)
        print("pa  {}  pv  {}".format(pa , pv))

        stop_power = self.stop_inference(pa_fuzzy , pv_fuzzy)
        left_fast_power = self.left_fast_inference(pa_fuzzy , pv_fuzzy)
        left_slow_power = self.left_slow_inference(pa_fuzzy , pv_fuzzy)
        right_fast_power = self.right_fast_inference(pa_fuzzy , pv_fuzzy)
        right_slow_power = self.right_slow_inference(pa_fuzzy , pv_fuzzy)
        print (stop_power , left_fast_power , left_slow_power , right_fast_power , right_slow_power)
        force = self.defuzzification(stop_power , left_fast_power , left_slow_power , right_fast_power , right_slow_power)
        return force



        # output = self._make_output()
        # self.system.calculate(self._make_input(world), output)
        # return output['force']
