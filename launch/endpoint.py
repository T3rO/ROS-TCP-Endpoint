from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    ros_ip = DeclareLaunchArgument(
        "tcp_ip", 
        default_value="0.0.0.0"
    )

    ros_tcp_port = DeclareLaunchArgument(
        "tcp_port", 
        default_value="10000"
    )

    return LaunchDescription(
        [
            ros_ip,
            ros_tcp_port,
            Node(
                package="ros_tcp_endpoint",
                executable="default_server_endpoint",
                emulate_tty=True,
                parameters=[{
                    "ROS_IP": LaunchConfiguration('tcp_ip'),
                    "ROS_TCP_PORT": LaunchConfiguration('tcp_port')
                }],
            )
        ]
    )
