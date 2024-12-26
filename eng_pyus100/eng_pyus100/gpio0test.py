
"""this is a Node to read and publish
ultrasonic distance sensor values (us100 default but others like: HR-SR04 ultrasonic sensor)
"""
# the ros2 run name is : sense
# import the standard ros2 module and subclass
import rclpy
from rclpy.node import Node

from std_msgs.msg import  Float32,String # using the Float32 to read and publish sensor value
# for this node i use the gpiozero library to control the distance sensor
# more info about gpiozero is in this link https://gpiozero.readthedocs.io/en/latest/index.html#
from gpiozero import DistanceSensor # The DistanceSensor class is  used to control the sensor
from time import sleep


class Us100Publisher(Node): # the node class thats running the node 
    def __init__(self):
        super().__init__('Us100_publisher')
        self.publishers_ = self.create_publisher(Float32, 'sensor_topic', 10) # create publisher
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        
        sensor = DistanceSensor(echo=4, trigger=17) # sets the echo and triggering pin.
        sense = sensor.distance  * 100
        msg = Float32()
        msg.data = sense
        
        self.publishers_.publish(msg) # publish the msg of the node
        print(sense,"cm") # just a print function for testing.
        self.get_logger().info('Publishing: "%s"' % msg.data) # logs msg data
        self.i += 1
        
# now it starts running the node
def main(args=None):
    rclpy.init(args=args)
    us100pub = Us100Publisher()
    
    rclpy.spin(us100pub)
if __name__ =='__main__':
    main()
        
        
        
