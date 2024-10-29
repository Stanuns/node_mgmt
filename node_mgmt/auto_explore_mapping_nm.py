import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from app_msgs.msg import AutoExploreMappingTrigger

class AutoExploreMappingExt(Node):
    def __init__(self):
        super().__init__('auto_explore_mapping_ext')
        self.subscription = self.create_subscription(
            AutoExploreMappingTrigger,
            '/auto_explore_mapping/trigger',
            self.aemapping_trigger,
            10)
        self.subscription

    def aemapping_trigger(self, msg):
        if msg.to_state == 1: ## 开始自动建图
            pass
        elif msg.to_state == 4: ## 停止自动建图
            pass
        elif msg.to_state == 5: ## 保存当前地图
            pass



def main(args=None):
    rclpy.init(args=args)
    auto_explore_mapping_ext = AutoExploreMappingExt()
    rclpy.spin(auto_explore_mapping_ext)
    auto_explore_mapping_ext.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
