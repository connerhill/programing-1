import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Vladimir Script", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Aquamarine
        self._button1.Location = System.Drawing.Point(12, 218)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(147, 67)
        self._button1.TabIndex = 0
        self._button1.Text = "show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Vladimir Script", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Aquamarine
        self._button2.Location = System.Drawing.Point(12, 291)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(147, 67)
        self._button2.TabIndex = 1
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Vladimir Script", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Aquamarine
        self._button3.Location = System.Drawing.Point(12, 364)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(147, 67)
        self._button3.TabIndex = 2
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Vladimir Script", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Aquamarine
        self._label2.Location = System.Drawing.Point(262, 59)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(691, 50)
        self._label2.TabIndex = 12
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Vladimir Script", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Aquamarine
        self._label1.Location = System.Drawing.Point(262, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(691, 50)
        self._label1.TabIndex = 13
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Vladimir Script", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.Aquamarine
        self._label3.Location = System.Drawing.Point(262, 109)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(691, 50)
        self._label3.TabIndex = 14
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Vladimir Script", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.Aquamarine
        self._label4.Location = System.Drawing.Point(262, 159)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(691, 50)
        self._label4.TabIndex = 15
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Vladimir Script", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.Aquamarine
        self._label5.Location = System.Drawing.Point(262, 209)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(691, 50)
        self._label5.TabIndex = 16
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Vladimir Script", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.Aquamarine
        self._label6.Location = System.Drawing.Point(262, 259)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(691, 50)
        self._label6.TabIndex = 17
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Vladimir Script", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.Color.Aquamarine
        self._label7.Location = System.Drawing.Point(262, 308)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(691, 50)
        self._label7.TabIndex = 18
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Vladimir Script", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.ForeColor = System.Drawing.Color.Aquamarine
        self._label8.Location = System.Drawing.Point(262, 358)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(691, 50)
        self._label8.TabIndex = 19
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(965, 443)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "schedule"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text= "First hour: english, room :809"
        self._label2.Text= "Second hour: computer programming, room: 608"
        self._label3.Text= "Third hour: study hall, s aud"
        self._label4.Text= "Fourth hour: algebra, room 109"
        self._label5.Text= "Fifth hour: biology, room 106"
        self._label6.Text= "Sixth hour: art, room 131"
        self._label7.Text= "Seventh hour: freshman seminar, room 607"
        self._label8.Text= "Eighth hour: world studies, 301"

    def Button2Click(self, sender, e):
        self._label1.Text= " "
        self._label2.Text= " "
        self._label3.Text= " "
        self._label4.Text= " "
        self._label5.Text= " "
        self._label6.Text= " "
        self._label7.Text= " "
        self._label8.Text= " "

    def Button3Click(self, sender, e):
        Application.Exit()