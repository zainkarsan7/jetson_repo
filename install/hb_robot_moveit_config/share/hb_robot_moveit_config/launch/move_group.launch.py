from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    pkg_share = os.path.join(
        os.getenv('AMENT_PREFIX_PATH').split(':')[0],
        'share', 'hb_robot_moveit_config'
    )

    urdf_file = os.path.join(pkg_share, 'urdf', 'hb_robot.urdf')
    srdf_file = os.path.join(pkg_share, 'config', 'hb_robot.srdf')

    return LaunchDescription([
        Node(
            package='moveit_ros_move_group',
            executable='move_group',
            output='screen',
            parameters=[{
                'robot_description': open(urdf_file).read(),
                'robot_description_semantic': open(srdf_file).read(),
                'robot_description_kinematics': os.path.join(pkg_share, 'config', 'kinematics.yaml'),
                'ompl_planning_config': os.path.join(pkg_share, 'config', 'ompl_planning.yaml'),
                'robot_description_planning': os.path.join(pkg_share, 'config', 'joint_limits.yaml'),
            }]
        )
    ])
