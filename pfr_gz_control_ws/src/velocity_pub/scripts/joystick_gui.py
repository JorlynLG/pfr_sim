#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
import tkinter as tk

class JoyPublisher(Node):
    def __init__(self):
        super().__init__('joy_publisher')
        self.publisher_ = self.create_publisher(Joy, 'joy', 10)
        self.joy_msg = Joy()
        self.joy_msg.axes = [0.0] * 4  # Initialize axes
        self.joy_msg.buttons = [0] * 4  # Initialize buttons
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        self.publisher_.publish(self.joy_msg)
        self.get_logger().info(f'Publishing: {self.joy_msg}')

    def update_axes(self, axes):
        self.joy_msg.axes = axes

    def update_buttons(self, buttons):
        self.joy_msg.buttons = buttons

class JoystickGUI:
    def __init__(self, master):
        self.master = master
        master.title("Virtual Joystick")

        self.publisher = JoyPublisher()

        # Create sliders for axes
        self.axis1 = tk.Scale(master, from_=-1, to=1, resolution=0.1, label='Linear-X', orient=tk.HORIZONTAL)
        self.axis1.pack()

        self.axis2 = tk.Scale(master, from_=-1, to=1, resolution=0.1, label='Linear-Y', orient=tk.HORIZONTAL)
        self.axis2.pack()
        
        self.axis3 = tk.Scale(master, from_=-1, to=1, resolution=0.1, label='Angular', orient=tk.HORIZONTAL)
        self.axis3.pack()

        # Create buttons
        self.button1 = tk.Button(master, text="In-Phase", command=self.toggle_button1)
        self.button1.pack()

        self.button2 = tk.Button(master, text="Opposite Phase", command=self.toggle_button2)
        self.button2.pack()

        self.button3 = tk.Button(master, text="Pivot Turn", command=self.toggle_button3)
        self.button3.pack()

        self.button4 = tk.Button(master, text="None", command=self.toggle_button4)
        self.button4.pack()

               # Initialize button states
        self.button1_state = 0
        self.button2_state = 0
        self.button3_state = 0
        self.button3_state = 1

        # Start the publishing loop
        self.update()

    def toggle_button1(self):
        self.button1_state = 1
        self.publisher.update_buttons([self.button1_state, 0, 0, 0, 0])

    def toggle_button2(self):
        self.button2_state = 1
        self.publisher.update_buttons([0, self.button2_state, 0, 0, 0])
  
    def toggle_button3(self):
        self.button3_state = 1
        self.publisher.update_buttons([0, 0, self.button3_state, 0, 0])

    def toggle_button4(self):
        self.button4_state = 1
        self.publisher.update_buttons([0, 0, 0, self.button4_state, 0])


    def update(self):
        # Update the joystick axes
        axes = [self.axis1.get(), self.axis2.get(), self.axis3.get(), 0, 0]
        self.publisher.update_axes(axes)

        # Publish the joystick message
        self.publisher.timer_callback()  # Directly call the publish method

        # Schedule the next update
        self.master.after(100, self.update)

def main(args=None):
    rclpy.init(args=args)
    root = tk.Tk()
    gui = JoystickGUI(root)
    root.mainloop()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
