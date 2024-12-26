
"""this is a Node to read and receive
ultrasonic distance sensor values (us100 default but others like: HR-SR04 ultrasonic 
sensor are optional)
"""
# the ros2 run name is : sub
# import the standard ros2 modules

import rclpy
from rclpy.node import Node
from std_msgs.msg import  Float32,String # using the Float32 to read and subscribe sensor value

# for this node i use the gpiozero library to control the pwm value.
# more info about gpiozero is in this link https://gpiozero.readthedocs.io/en/latest/index.html#

from gpiozero import PWMLED # PWMLED is used to control the led.

led = PWMLED(21) # the led

class PwmSubscriber(Node): # the node class thats running the node 
    
    def __init__(self):
        super().__init__('Pwmsub')
        self.subscription = self.create_subscription(      # create subscription
            Float32,'sensor_topic'
            ,self.listener_callback,10)
        self.subscription 
        
    def listener_callback(self,msg): # listens msgdata
        self.get_logger().info('i receive sensor values cm  of"%f"' % msg.data) # logs msg.data
        
        val  = msg.data # converts msg.data int a pwm value
        led.value = val/100 # led value is substracted to make the led work
        print("pwm value is: ",led.value) # prints pwm value.
        print(val  ,"cm") # prints sensor value  in cm.
# now it spins the node.
def main(args=None):
    rclpy.init(args=args)
    
    pwmsub = PwmSubscriber()
    
    rclpy.spin(pwmsub)
    
    pwmsub.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
        

            