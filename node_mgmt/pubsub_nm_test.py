import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class PubSubNMTest(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, '/pubsub_nm', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        self.subscription = self.create_subscription(
            String,
            '/start_stop_pubsub_nm',
            self.startstop_callback,
            10)
        self.subscription

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
    
    def startstop_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    pubsub_nm_test = PubSubNMTest()

    rclpy.spin(pubsub_nm_test)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    pubsub_nm_test.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()