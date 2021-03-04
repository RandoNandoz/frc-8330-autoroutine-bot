"""
Team 8330's auto-magical auto-routine robot.
"""
import wpilib
import wpilib.drive


class Robot(wpilib.TimedRobot):

    def robotInit(self) -> None:
        # Create the motor controller objects.
        self.right_motor_back = wpilib.PWMVictorSPX(0)
        self.right_motor_front = wpilib.PWMVictorSPX(1)
        self.left_motor_front = wpilib.PWMVictorSPX(2)
        self.left_motor_back = wpilib.PWMVictorSPX(3)
        self.arm_motor = wpilib.PWMVictorSPX(4)
        self.arm_abc = wpilib.PWMVictorSPX(5)

        # Create SpeedControllers as we're using a gearbox.
        self.right_speed_ctrl_group = wpilib.SpeedControllerGroup(self.right_motor_back, self.right_motor_front)
        self.left_speed_ctrl_group = wpilib.SpeedControllerGroup(self.left_motor_back, self.left_motor_front)

        # Drive class
        self.diff_drive = wpilib.drive.DifferentialDrive(self.left_speed_ctrl_group, self.right_speed_ctrl_group)

        # Timer class.
        self.timer = wpilib.Timer()

    def autonomousInit(self) -> None:
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self) -> None:
        print(self.timer.get())
        if self.timer.get() > 5 and :
            # self.arm_motor.set(1)
            self.arm_abc.set(0.5)
        else:
            self.diff_drive.curvatureDrive(-0.2, 0, False)
            self.arm_abc.set(-0.5)

if __name__ == "__main__":
    wpilib.run(Robot)
