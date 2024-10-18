import math
import System.Drawing
import System.Windows.Forms

#
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(133, 23)
        self._button1.TabIndex = 0
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(151, 12)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(133, 23)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(290, 12)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(133, 23)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # listBox1
        # 
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(12, 44)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(538, 407)
        self._listBox1.TabIndex = 3
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(562, 463)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog122a"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "Number\t\tSquare\t\tSquare Root"
        self._listBox1.Items.Add(heading)
        # range(stop), range(start, stop), range(start, stop, step)
        for num in range(1, 50+1) : 
            nsqrd = num**2
            nsqrt = math.sqrt(num)
            line = str(num) + "\t\t" + str(nsqrd) + "\t\t" + str(round(nsqrt,4))
            self._listBox1.Items.Add(line)
        

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()
       

    def Button3Click(self, sender, e):
        Application.Exit()