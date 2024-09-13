# import ros2 python api
import rclpy
from rclpy.node import Node

# import standard message format
from std_msgs.msg import String


# define node class
class StudentSubscriber(Node):
    def __init__(self, node_name: str) -> None:
        super().__init__(node_name)
        # print info
        self.get_logger().info("student node created!")

        # create a topic subscriber
        # parameters:
            # msg_type: the type of message
            # topic: the name of topic
            # qos_profile: a QoSProfile for setting the communication policy or a history depth to store
        self.hello_subscriber = self.create_subscription(msg_type=String, topic="hello_topic", callback=self._subscribe, qos_profile=1)

    def _subscribe(self, hello_message):
        # print info
        self.get_logger().info("received message: {}".format(hello_message.data))


def main():
    # initialize ros2
    rclpy.init()

    # execute callbacks until shutdown
    rclpy.spin(node=StudentSubscriber(node_name="student_receive_node"))

    # shutdown a previously initialization
    rclpy.shutdown()


if __name__ == '__main__':
    main()
