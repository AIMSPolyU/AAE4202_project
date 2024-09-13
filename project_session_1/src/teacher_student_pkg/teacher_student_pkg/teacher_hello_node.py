# import ros2 python api
import rclpy
from rclpy.node import Node
# import standard message format
from std_msgs.msg import String

# define node class
class TeacherPublisher(Node):
    def __init__(self, node_name: str) -> None:
        super().__init__(node_name)
        # print info
        self.get_logger().info("teacher node created!")

        # create a topic publisher
        # parameters:
            # msg_type: the type of message
            # topic: the name of topic
            # qos_profile: a QoSProfile for setting the communication policy or a history depth to store
        self.hello_publisher = self.create_publisher(msg_type=String, topic="hello_topic", qos_profile=10)

        # create a timer
        # parameters:
            # timer_period_sec: the period of the timer
            # callback: a user-defined callback function that is called when the timer expires
        self.timer = self.create_timer(timer_period_sec=1.0, callback=self._publish)

        # create a counter
        self.counter = 1

    def _publish(self):
        # create hello message
        hello_message = String()
        hello_message.data = "Hello, welcome to AAE4202 {}".format(self.counter)

        # publish hello message
        self.hello_publisher.publish(msg=hello_message)
        # print info
        self.get_logger().info("publish: {}".format(hello_message.data))

        self.counter += 1

def main():
    # initialize ros2
    rclpy.init()

    # execute callbacks until shutdown
    rclpy.spin(node=TeacherPublisher(node_name="teacher_hello_node"))

    # shutdown a previously initialization
    rclpy.shutdown()

if __name__ == '__main__':
    main()
