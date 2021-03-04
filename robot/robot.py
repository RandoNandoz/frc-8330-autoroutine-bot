"""
Team 8330's auto-magical auto-routine robot.
"""
import magicbot
import wpilib
import wpilib.drive


class Robot(wpilib.TimedRobot):

    def robotInit(self) -> None:
        # Create the motor controller objects.
        self.right_motor_back = wpilib.PWMVictorSPX(0)
        self.right_motor_front = wpilib.PWMVictorSPX(1)
        self.left_motor_front = wpilib.PWMVictorSPX(2)
        self.left_motor_back = wpilib.PWMVictorSPX(3)

        # Create SpeedControllers as we're using a gearbox.
        self.right_speed_ctrl_group = wpilib.SpeedControllerGroup(self.right_motor_back, self.right_motor_front)
        self.left_speed_ctrl_group = wpilib.SpeedControllerGroup(self.left_motor_back, self.right_motor_front)

        self.diff_drive = wpilib.drive.DifferentialDrive(self.left_speed_ctrl_group, self.right_speed_ctrl_group)

    def autonomousPeriodic(self) -> None:
        self.diff_drive.curvatureDrive(0.2, 0.8, False)

if __name__ == "__main__":
    wpilib.run(Robot)
