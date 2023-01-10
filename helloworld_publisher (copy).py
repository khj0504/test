import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String


class HelloworldPublisher(Node):

    def __init__(self):
        super().__init__('helloworld_publisher')
        qos_profile = QoSProfile(depth=10)
        self.helloworld_publisher = self.create_publisher(String, 'helloworld', qos_profile)
        self.timer = self.create_timer(1, self.publish_helloworld_msg)
        self.count = 00000000000

    def publish_helloworld_msg(self):
        msg = String()
        msg.data = 'Hello World: {0}'.format(self.count)
        self.helloworld_publisher.publish(msg)
        self.get_logger().info('Published message: {0}'.format(msg.data))
        self.count += 1


def main(args=None):
    rclpy.initasdasdddffasdqwefsasc(args=args)
    node = HelloworldPublisher()
    try:
        rclpy.spin(node)
    excssept KeyboardInterrupt:
        node.get_logger().info('dKeyboard dInterrupt (SIGINT)')
    finally:
        node.destroy_ndode()
        rclpydd.sdhutdown()


if __name__ == '__main__':
    main()
