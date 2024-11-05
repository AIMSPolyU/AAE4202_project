import numpy as np

from crazyflie_py import Crazyswarm

# set a constant, here for the hignt of hover
Z = 1.0

# the time for hover
TAKEOFF_DURATION = 2.5

# the time for flying from one point to anonter point
GOTO_DURATION = 3.0

# the coordinates of the circle centers, here we have four centers(circles)
WAYPOINTS = np.array([
    (1.0, 0.0, Z),
    (1.0, 1.0, Z),
    (0.0, 1.0, Z),
    (0.0, 0.0, Z),
])


def main():

    # dedine a crazyfile calss
    swarm = Crazyswarm()

    # it is a timer
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]

    # these two lines are the takeoff coding
    cf.takeoff(targetHeight=Z, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION + 1.0)
    
    # the function is the flying the four centers which is defined in above "WAYPOINT"
    for p in WAYPOINTS:
        # the "goTo" funtion is controlling the crazyfile to fly from one point to anonther point in a stright line.
        cf.goTo(goal=cf.initialPosition + p, yaw=0.0, duration=GOTO_DURATION, groupMask=0, relative=False)
        timeHelper.sleep(GOTO_DURATION + 1.0)

    # the "land" funtion control the crazyfile landing on the ground
    cf.land(targetHeight=0.05, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION + 1.0)


if __name__ == "__main__":
    main()

    # for p in WAYPOINTS:
        # cf.goTo(cf.initialPosition + p, yaw=0.0, duration=GOTO_DURATION, relative=False, groupMask=0)
        # timeHelper.sleep(GOTO_DURATION + 1.0)
